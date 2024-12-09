import os
import psutil
from prometheus_client import start_http_server, Gauge
from time import sleep

# Переменные окружения для хоста и порта
EXPORTER_HOST = os.getenv('EXPORTER_HOST', '0.0.0.0')
EXPORTER_PORT = int(os.getenv('EXPORTER_PORT', 8000))

# Метрики
cpu_usage_gauge = Gauge('cpu_usage', 'CPU Usage by core', ['core'])
memory_total_gauge = Gauge('memory_total', 'Total Memory in the system')
memory_used_gauge = Gauge('memory_used', 'Used Memory in the system')
disk_total_gauge = Gauge('disk_total', 'Total Disk Space')
disk_used_gauge = Gauge('disk_used', 'Used Disk Space')

def collect_metrics():
    # CPU usage per core
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpu_usage_gauge.labels(core=f'core_{i}').set(percentage)

    # Memory usage
    memory = psutil.virtual_memory()
    memory_total_gauge.set(memory.total)
    memory_used_gauge.set(memory.used)

    # Disk usage
    disk = psutil.disk_usage('/')
    disk_total_gauge.set(disk.total)
    disk_used_gauge.set(disk.used)

if __name__ == "__main__":
    # Запуск HTTP-сервера
    start_http_server(EXPORTER_PORT, addr=EXPORTER_HOST)
    print(f"Exporter is running on {EXPORTER_HOST}:{EXPORTER_PORT}")

    while True:
        collect_metrics()
        sleep(5)  # Обновление метрик каждые 5 секунд
