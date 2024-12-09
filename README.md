# System Metrics Exporter

Этот проект представляет собой экспортер метрик системы для Prometheus. Экспортер собирает данные о состоянии системы (процессор, оперативная память, диски) и предоставляет их для мониторинга через Grafana.

---

## 🚀 Функциональность

Экспортер предоставляет следующие метрики:

- **Использование процессора**: загрузка ядер.
- **Использование памяти**: общая и используемая оперативная память.
- **Использование дисков**: общий объём и занятая память.

---

## 📦 Установка и запуск

### 1. Клонирование репозитория

Склонируйте проект:

```bash
git clone https://github.com/uumk0n/prometheus-exporter.git
cd prometheus-exporter.git
```

### 2. Создайте файл `.env`

Создайте файл `.env` и добавьте переменные окружения:

```plaintext
EXPORTER_HOST=0.0.0.0
EXPORTER_PORT=8000
```

### 3. Запустите с помощью Docker Compose

Соберите и запустите все сервисы:

```bash
docker-compose up --build
```

---

## 🌐 Доступ к сервисам

1. **Экспортер**: [http://localhost:8000](http://localhost:8000)  
   Метрики доступны на корневом пути `/`.
2. **Prometheus**: [http://localhost:9090](http://localhost:9090)  
   Можно тестировать запросы PromQL.
3. **Grafana**: [http://localhost:3000](http://localhost:3000)
   - **Логин**: `admin`
   - **Пароль**: `admin` (по умолчанию).

---

## 🔧 Настройка Grafana

### Импорт дашборда

1. Перейдите в Grafana: [http://localhost:3000](http://localhost:3000).
2. Нажмите на "Plus" (плюс) → **Import**.
3. Загрузите файл `grafana_dashboard.json` из корня репозитория.
4. Выберите источник данных (Prometheus) и нажмите **Import**.

---

## 📜 PromQL запросы

- **Использование процессора**:

  ```promql
  avg(rate(node_cpu_seconds_total{mode!="idle"}[5m]))
  ```

- **Общая и используемая память**:

  ```promql
  node_memory_MemTotal_bytes
  node_memory_MemAvailable_bytes
  ```

- **Использование дисков**:
  ```promql
  node_filesystem_size_bytes
  node_filesystem_avail_bytes
  ```

---

## 🐋 Контейнеры

- **Exporter**: собирает метрики системы.
- **Prometheus**: собирает и хранит метрики.
- **Grafana**: визуализирует метрики.
