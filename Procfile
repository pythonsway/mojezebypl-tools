release: python manage.py migrate
web: gunicorn mojezeby.wsgi --timeout 120 --log-file -
worker: python manage.py rqworker default
