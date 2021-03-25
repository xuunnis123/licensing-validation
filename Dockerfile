FROM python:3.6
WORKDIR /app
ADD . /app
RUN pip3 install -r requirements.txt
