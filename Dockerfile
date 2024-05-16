FROM python:3.12

RUN apt-get update

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x run.sh

EXPOSE 8000

ENTRYPOINT ["bash","run.sh"]

