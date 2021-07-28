# Diary

🚧 **not ready yet** 🚧


```
Diary
├─ docker-compose.yaml
├─ fastapi
│  ├─ alembic
│  │  ├─ env.py
│  │  ├─ README
│  │  ├─ script.py.mako
│  │  └─ versions
│  │     └─ 73e046ff2fd0_baseline.py
│  ├─ alembic.ini
│  ├─ app
│  │  ├─ api
│  │  │  ├─ api.py
│  │  │  ├─ deps.py
│  │  │  └─ endpoints
│  │  │     ├─ login.py
│  │  │     ├─ posts.py
│  │  │     └─ users.py
│  │  ├─ config.py
│  │  ├─ core
│  │  │  └─ security.py
│  │  ├─ crud
│  │  │  ├─ base.py
│  │  │  ├─ crud_post.py
│  │  │  ├─ crud_user.py
│  │  │  └─ __init__.py
│  │  ├─ db
│  │  │  ├─ base.py
│  │  │  ├─ base_class.py
│  │  │  ├─ init_db.py
│  │  │  └─ session.py
│  │  ├─ diary.db
│  │  ├─ main.py
│  │  ├─ models
│  │  │  ├─ post.py
│  │  │  ├─ user.py
│  │  │  └─ __init__.py
│  │  ├─ monitoring
│  │  │  └─ opentelemetry.py
│  │  └─ schemas
│  │     ├─ post.py
│  │     ├─ token.py
│  │     ├─ user.py
│  │     └─ __init__.py
│  ├─ Dockerfile
│  └─ reset_db.sh
├─ grafana
│  ├─ dashboards
│  │  ├─ dashboards.yml
│  │  └─ fastapi.json
│  ├─ datasources
│  │  └─ datasources.yml
│  └─ Dockerfile
├─ images
│  └─ grafana.png
├─ prometheus
│  └─ prometheus.yml
└─ README.md

```

## Build and start

```bash
docker-compose up --build
```

Try it at [http://localhost:8000](http://localhost:8000)

![Grafana](images/grafana.png "Grafana")