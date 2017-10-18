FROM python:3.6.2

ENV MAX_THREAD 2

ADD /app /app
VOLUME /workspace/videos

EXPOSE 8080

# Get pip to download and install requirements:
RUN pip install -r /app/requirements.txt

CMD ["python", "/app/converter_server.py"]
