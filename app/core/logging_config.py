import logging
from app.core.context.context import correlation_id_ctx

class CorrelationIdFilter(logging.Filter):

    def filter(self, record):
        record.correlation_id = correlation_id_ctx.get() or "N/A"
        return True
    
def setup_logging():
    logger = logging.getLogger()
    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "[Correlation_Id: %(correlation_id)s] %(levelname)s - %(message)s"
    )

    handler.setFormatter(formatter)
    handler.addFilter(CorrelationIdFilter())

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

   