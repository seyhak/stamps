FROM python:3.12-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
# RUN apk add --update --no-cache postgresql-client libpq-dev
RUN pip install --no-cache-dir -r ./requirements.txt
COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
