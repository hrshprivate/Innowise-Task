FROM python:3.8
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /api

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]