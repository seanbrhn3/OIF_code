FROM ubuntu:latest

RUN apt-get update && apt-get install python3-pip -y \
python3-dev -y

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "python3","app.py" ]
