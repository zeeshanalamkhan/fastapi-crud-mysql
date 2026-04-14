from contextvars import ContextVar

correlation_id_ctx = ContextVar("correlation_id", default=None)