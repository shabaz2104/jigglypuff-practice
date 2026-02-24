# agents/core/tracing.py
# COMPLETE NO-OP LANGFUSE STUB (FINAL, SAFE)

class DummyObservation:
    def __init__(self, *args, **kwargs):
        pass

    # Context manager support
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    # Langfuse span methods (NO-OP)
    def update(self, *args, **kwargs):
        pass

    def end(self, *args, **kwargs):
        pass

    def log(self, *args, **kwargs):
        pass


class DummyLangfuse:
    def start_as_current_observation(self, *args, **kwargs):
        # Accepts ANY args like name, user_id, metadata, etc.
        return DummyObservation()

    def flush(self, *args, **kwargs):
        pass


langfuse = DummyLangfuse()