FROM python:3.11-slim


WORKDIR /app
COPY /end_points/requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY /Dal  /app/Dal

COPY /config.py /app/config.py

COPY /end_points /app/end_points

COPY /logger_ /app/logger_

EXPOSE 8000

CMD ["uvicorn", "end_points.end_points_app:app", "--host", "0.0.0.0", "--port", "8000"]