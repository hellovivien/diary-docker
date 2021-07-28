from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.propagate import set_global_textmap
from opentelemetry.propagators.b3 import B3Format

# Example usage inside functions
# trace a block of code
# with tracer.start_as_current_span("time-consuming-operation"): {block of code}
# customize error recording
# span = trace.get_current_span()
# span.record_exception(error)
# span.set_status(StatusCode.ERROR)


def init_ot_with_jaeger():
    set_global_textmap(B3Format())
    trace.set_tracer_provider(
        TracerProvider(
            resource=Resource.create({SERVICE_NAME: "ot-fastapi-service"})
        )
    )
    # jaeger exporter
    jaeger_exporter = JaegerExporter(
        agent_host_name="localhost",
        agent_port=6831,
    )
    # add exporter to trace
    trace.get_tracer_provider().add_span_processor(
        BatchSpanProcessor(jaeger_exporter)
    )
