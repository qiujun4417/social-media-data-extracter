# 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制项目代码到容器中
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 运行爬虫命令
CMD scrapy crawl caixukun
