FROM python:3.13-slim

WORKDIR /app

COPY /DataPersister/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /kafka_ /app/kafka_

COPY /DataPersister /app/DataPersister

COPY /config.py /app/config.py

COPY /logger_ /app/logger_


CMD ["python", "-m" , "DataPersister.main"]

