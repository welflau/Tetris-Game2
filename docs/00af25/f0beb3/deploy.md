# 部署文档 - 设计文档整合与输出

## 本地预览

- 预览地址: http://localhost:9819
- 直接在浏览器中打开即可查看效果

## 部署步骤

1. 构建镜像: `docker build -t app .`
2. 启动服务: `docker-compose up -d`
3. 健康检查: `curl http://localhost:8000/api/health`
