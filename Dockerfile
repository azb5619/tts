FROM python:3

ADD web.py web.py
ADD send_reply.py send_reply.py

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir flask twilio cheroot

EXPOSE 5000

ENTRYPOINT ["python3", "web.py"]
