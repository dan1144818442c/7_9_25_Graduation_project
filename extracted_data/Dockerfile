FROM python:3.13-slim

WORKDIR /app

COPY /extracted_data/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /kafka_ /app/kafka_

COPY /extracted_data /app/extracted_data

COPY /config.py /app/config.py

COPY /logger_ /app/logger_


CMD ["python", "-m" , "extracted_data.main"]

