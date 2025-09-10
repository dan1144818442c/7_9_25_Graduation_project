FROM python:3.13-slim

WORKDIR /app

COPY /Transcription_and_updating/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /kafka_ /app/kafka_

COPY /Transcription_and_updating /app/Transcription_and_updating

COPY /config.py /app/config.py

COPY /DataPersister /app/DataPersister

COPY /Dal  /app/Dal

COPY /tools  /app/tools

COPY /logger_ /app/logger_


CMD ["python", "-m" , "Transcription_and_updating.main"]

