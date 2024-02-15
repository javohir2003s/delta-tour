FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip


RUN apt update
RUN apt install gettext -y


RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

LABEL authors="hyperman"

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]
