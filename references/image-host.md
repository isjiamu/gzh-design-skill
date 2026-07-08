# 本地图片自动上传图床 —— 解决"本地图粘不进公众号"

## 为什么需要

公众号编辑器粘贴 HTML 时，`<img src="https://公网URL">` 会被微信**自动抓取并转存**到它自己的 CDN；但**本地路径**（`./images/x.png`、`/Users/.../图.png`）微信访问不到 → 粘进去图裂。

所以：**本地图必须先上传到图床（七牛/OSS/COS…）换成公网 URL**，再进排版。远程 `http(s)` 图片本来就是公网的，不用管。

## 工作流（叠加在排版之前）

```
解析 Markdown → 收集所有 ![](...) 的 src
  ├─ http/https 远程图 → 原样保留
  └─ 本地路径图 → scripts/upload_image.py 上传 → 拿回公网 URL → 替换 src
装配 HTML（此时图全是公网 URL）→ 粘进公众号，微信自动转存，图不裂 ✅
```

**Agent 具体做法**：排版第 0 步识别到本地图后，一次性调用：

```bash
<SKILL_ROOT>/scripts/upload_image.py 图1.png ./images/图2.jpg …
# 输出每行「本地路径<TAB>公网URL」，据此把 Markdown/产物里的本地 src 换成 URL
```

- 传远程 URL 进去会**原样返回**（方便一把梭全丢进去，不用自己区分）。
- 同一张图按**内容 hash** 命名，重复上传只会得到同一个 URL（幂等），并有本地缓存 `~/.gzh-design/upload-cache.json`，重排同一篇文章不重复上传。
- **未配置图床**时脚本报错退出码 2 并给出提示——此时**转告用户去配置（见下）或手动上传后把 URL 填回 Markdown**，不要静默把本地路径塞进产物。

## 配置图床（密钥绝不进仓库）

密钥是机密，**只存在本地**，两种方式，环境变量优先：

### 方式 A：环境变量

```bash
export GZH_IMAGE_HOST=qiniu          # 可选，默认 qiniu
export QINIU_ACCESS_KEY=你的AK
export QINIU_SECRET_KEY=你的SK
export QINIU_BUCKET=你的空间名
export QINIU_DOMAIN=https://cdn.你的域名.com   # 七牛空间绑定的加速域名
# export QINIU_UP_HOST=https://up.qiniup.com   # 可选，区域上传报错时按七牛控制台改
```

### 方式 B：本地配置文件 `~/.gzh-design/image-host.json`（已被 .gitignore 忽略）

```json
{
  "host": "qiniu",
  "qiniu": {
    "access_key": "你的AK",
    "secret_key": "你的SK",
    "bucket": "你的空间名",
    "domain": "https://cdn.你的域名.com"
  }
}
```

配好后自检：`scripts/upload_image.py --check`（只查配置，不上传）。

### 七牛云怎么拿这几个值（首次配置）

1. 注册七牛云 → 实名认证（对象存储有免费额度）。
2. 新建一个**存储空间（Bucket）**，选公开空间。
3. 给空间**绑定一个加速域名**（七牛测试域名有时效，正式用建议绑自己的域名）→ 这就是 `QINIU_DOMAIN`。
4. 个人中心 → 密钥管理 → 拿 **AccessKey / SecretKey**。

> 其它图床同理：阿里云 OSS、腾讯云 COS 都是"建 Bucket + 绑域名 + 拿 AK/SK"。

## 支持的图床 & 扩展

- **七牛（qiniu）**：已实现（原生 API，无需装 SDK）。
- **阿里 OSS / 腾讯 COS / 其它**：架构已留好适配器接口。加一个新图床 = 在 `scripts/upload_image.py` 里加一个 `xxx_put(cfg, key, filepath) -> url` 函数，并在 `upload_one()` 的分发处加一个分支；配置在 `load_config()` 里加读取。欢迎 PR。

## 安全须知

- **密钥永远不进仓库**：只放环境变量或 `~/.gzh-design/image-host.json`（在 skill 外的用户目录，且 .gitignore 已忽略同名文件）。
- 上传的是**公开图床**，图片会公网可访问——别传隐私/未公开的图。
- 用**内容 hash 命名**，不暴露原始文件名。
