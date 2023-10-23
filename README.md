# Инструкция по развертыванию Django проекта

Эта инструкция поможет вам развернуть ваш Django проект на сервере с использованием Nginx и uWSGI.

## Шаг 1: Установка и настройка Nginx

1. Установите Nginx на ваш сервер:

```bash
sudo apt update
sudo apt install nginx
```

2. Создайте конфигурационный файл Nginx для вашего проекта. Создайте файл `/etc/nginx/sites-available/myproject` и откройте его в текстовом редакторе:

```bash
sudo nano /etc/nginx/sites-available/myproject
```

3. Вставьте следующую конфигурацию Nginx в файл `myproject`:
```ini
server {
    listen 80;
    server_name http://127.0.0.1; 
    location / {
        include uwsgi_params;
        uwsgi_pass unix:/path/to/your/project/socket.sock;  # Замените на путь к сокету вашего проекта
    }
}
```
4. Сохраните файл и закройте его.

5. Создайте символическую ссылку на созданный конфигурационный файл в директории `sites-enabled`:

```bash
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled/
```

6. Проверьте, что конфигурация Nginx не содержит ошибок:

```bash
sudo nginx -t
```

7. Если проверка прошла успешно, перезапустите Nginx:

```bash
sudo service nginx restart
```

Теперь Nginx настроен для проксирования запросов к вашему Django проекту.

## Шаг 2: Установка и настройка uWSGI

1. Установите uWSGI в вашем виртуальном окружении Python:

```bash
pip install uwsgi
```

2. Создайте конфигурационный файл uWSGI для вашего проекта. Создайте файл `uwsgi.ini` в корневой директории вашего проекта и откройте его в текстовом редакторе:

```bash
nano uwsgi.ini
```

3. Вставьте следующую конфигурацию uWSGI в файл `uwsgi.ini`:

```ini
[uwsgi]
http-timeout = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout-keepalive = 86400
http-timeout
```
4. Запуск тестового задания:
```
Перед запуском нужно через терминад ввести следующую команду:  service mysql start         
Когда запустите, http://127.0.0.1:8000/upload/ это загрузки данных, http://127.0.0.1:8000/data/ для просмотра данных
```

