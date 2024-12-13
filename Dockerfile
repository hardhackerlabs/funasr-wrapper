# 使用官方 Python 运行时作为父镜像
FROM python:3.10-slim

RUN apt-get update && apt-get install -y git ffmpeg
RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

RUN pip install -U funasr modelscope huggingface_hub
# RUN git clone https://github.com/alibaba/FunASR.git && cd FunASR && pip install -e . && cd ..

# 将当前目录内容复制到容器的 /app 中
COPY . /app
RUN pip install -r ./requirements.txt

EXPOSE 7777

# 运行 FastAPI 应用
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "7777"]