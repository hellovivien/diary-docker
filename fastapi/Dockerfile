FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Copy app
COPY /app /app

# Install pip requirements
RUN python -m pip install -r app/requirements.txt

