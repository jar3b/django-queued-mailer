# django-queued-mailer

Django mail backend uses celery as email message queue

### requirements

Django >= 1.11, Celery >= 4.1.1

### setup

- add `git+https://github.com/jar3b/django-queued-mailer.git` to requirements.txt
- install package `pip install --upgrade git+https://github.com/jar3b/django-queued-mailer.git`
- run celery worker

```
celery -A project worker
```

### run one task at time (optional)

- setup Celery routes

```
app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('qmailer_mail_queue', routing_key='qmailer.send.#'),
)
```

- start separate worker

```
celery -A project worker -Q qmailer_mail_queue --concurrency=1
```

### configure

Django settings:

- `QMAILER_EMAIL_BACKEND` - set email backend, default `django.core.mail.backends.smtp.EmailBackend`
- `QMAILER_TASK_QUEUE_NAME` - queue name for routing, default `default`, if you use separate "serial" worker as described above, you need to specify this option