__all__ = (
    'get_current_datetime',
)


def get_current_datetime() -> str:
    from datetime import datetime
    import time

    timestamp = time.time()
    d = datetime.fromtimestamp(timestamp)
    return d.strftime('%Y/%m/%d %H:%M:%S')
