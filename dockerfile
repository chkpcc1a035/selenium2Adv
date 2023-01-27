FROM python:3.10-alpine3.16

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app

COPY ./app /app

WORKDIR /app

CMD ["python","startService.py"]