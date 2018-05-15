FROM registry.opensource.zalan.do/stups/python:3.6.5-22

COPY Pipfile /
COPY Pipfile.lock /

RUN pipenv install --system --deploy --ignore-pipfile

COPY app.py /
COPY swagger.yaml /

WORKDIR /data
CMD /app.py
