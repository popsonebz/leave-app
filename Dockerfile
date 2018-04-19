FROM python:2.7.14

EXPOSE 1234

RUN apt-get update
RUN apt-get install -y swig libssl-dev dpkg-dev netcat git
RUN pip install --upgrade pip

RUN mkdir /code

WORKDIR /code

RUN git clone https://github.com/popsonebz/leave-app.git

WORKDIR ./leave-app

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate

ENV DJANGO_ENV=prod

ENV DOCKER_CONTAINER=1

RUN chmod u+x entrypoint.sh

#CMD ["sh", "entrypoint.sh"]

CMD ["python", "./manage.py", "runserver", "0.0.0.0:1234"]
