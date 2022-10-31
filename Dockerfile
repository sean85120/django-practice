FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
