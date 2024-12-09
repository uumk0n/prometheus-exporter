# Базовый образ
FROM python:3.10-slim

# Устанавливаем зависимости
RUN pip install --no-cache-dir prometheus_client psutil

# Копируем код приложения
WORKDIR /app
COPY exporter.py .

# Задаём переменные окружения по умолчанию
ENV EXPORTER_HOST=0.0.0.0
ENV EXPORTER_PORT=8000

# Запускаем приложение
CMD ["python", "exporter.py"]
