FROM python:3.13-slim

WORKDIR /app


COPY /data_processing/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /kafka_ /app/kafka_

COPY /DataPersister /app/DataPersister

COPY /data_processing /app/data_processing

COPY /Dal  /app/Dal

COPY /config.py /app/config.py

COPY /logger_ /app/logger_

COPY /tools  /app/tools



CMD ["python", "-m" , "data_processing.main" ]

