FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y && apt-get install -y build-essential libssl-dev libffi-dev python3-dev mariadb-client
RUN apt-get install -yq nano vim
RUN python3 -m pip install pip && pip install --upgrade pip
ENV TZ=Asia/Ho_Chi_Minh

WORKDIR /backend/
COPY ./backend/lightvisiontest/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ENTRYPOINT [ "python" ]