FROM tiangolo/uwsgi-nginx-flask:python3.10
MAINTAINER rlegorreta@legosoft.com.mx

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

COPY ./requirements.txt /var/www/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /var/www/requirements.txt

COPY ./app /app
