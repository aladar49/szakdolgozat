FROM python:3.6.2

ENV MAX_THREAD 2
ENV SCHEDULER_URL 0.0.0.0

ADD /app /app
VOLUME /tmp/videos

EXPOSE 8080

# Get pip to download and install requirements:
RUN pip install -r /app/requirements.txt

CMD ["python", "/app/converter_server.py"]
