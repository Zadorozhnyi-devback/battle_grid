__all__ = (
    'get_current_datetime',
    'update_timestamp'
)


def get_current_datetime() -> str:
    from datetime import datetime
    import time

    timestamp = time.time()
    d = datetime.fromtimestamp(timestamp)
    return d.strftime('%Y/%m/%d %H:%M:%S')


def update_timestamp(self, category: str) -> None:
    self._categories[category]['updated_at'] = get_current_datetime()
