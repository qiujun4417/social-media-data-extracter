# 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制项目代码到容器中
COPY requirements.txt /app/requirements.txt
COPY pip.conf /app/pip.conf
COPY . /app

# 安装依赖
RUN pip install -i https://mirrors.aliyun.com/pypi/simple -U pip
RUN pip install --no-cache-dir -r requirements.txt

# 运行爬虫命令
CMD scrapy crawl caixukun
