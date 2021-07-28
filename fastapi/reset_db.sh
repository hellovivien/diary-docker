rm -rf alembic/versions/*
rm app/diary.db
alembic revision --autogenerate -m "baseline"
alembic upgrade head