#!/bin/sh
docker build -nocache -t yomtvraps .

docker run -p 8000:8000 -it yomtvraps python3 /usr/local/lib/python3.6/site-packages/web1/manage.py runserver 0.0.0.0:8000

