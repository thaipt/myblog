web: flask db upgrade; flask translate compile; gunicorn myblog:app
worker: rq worker myblog-tasks
