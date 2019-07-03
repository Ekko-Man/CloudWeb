FROM python:3.6-alpine

WORKDIR /home/CloudWeb

COPY requirements.txt requirements.txt
RUN apk add --no-cache --update gcc musl-dev libffi-dev openssl-dev python3-dev
RUN python3 -m venv venv
RUN venv/bin/pip3 install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN venv/bin/pip3 install gunicorn

COPY app app
COPY config.py run.py ./

EXPOSE 5000
ENV FLASK_APP run.py

CMD ["python", "run.py"]
