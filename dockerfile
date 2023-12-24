# Используем официальный образ Python 3 как базовый
FROM python:3.9

# Установка рабочего каталога в контейнере
WORKDIR /app

# Копирование файла зависимостей в текущую директорию
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода приложения в контейнер
COPY . .

# Определение переменной среды для работы Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Открываем порт 5000
EXPOSE 5000

# Запускаем приложение Flask
CMD ["flask", "run"]
