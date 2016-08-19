web: gunicorn config.wsgi:application
worker: celery worker --app=dictionary2.taskapp --loglevel=info
