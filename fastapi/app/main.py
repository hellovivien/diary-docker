from fastapi import FastAPI

from app.api.api import api_router
from app.config import settings

from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
import app.monitoring.opentelemetry as monitoring

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url="/openapi.json"
)

app = FastAPI()

app.include_router(api_router)

if settings.MONITORING_ACTIVE:
    # Opentelemetry + Jaeger
    monitoring.init_ot_with_jaeger()
    FastAPIInstrumentor.instrument_app(app)

    # Prometheus
    Instrumentator().instrument(app).expose(app)
