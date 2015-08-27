FROM zalando/python:3.4.0-4

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY app.py /
COPY swagger.yaml /

WORKDIR /data
CMD /app.py
