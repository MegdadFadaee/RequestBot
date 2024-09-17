import time
from datetime import datetime, timezone

from jdatetime import datetime as jdatetime


class BeautifulTime:

    @staticmethod
    def create_readable_time(unix_time: int) -> str:
        date_time = datetime.fromtimestamp(unix_time, timezone.utc)
        jalali_date_time = jdatetime.fromtimestamp(unix_time)
        return f'{date_time:%Y-%m-%d %H:%M:%S}\n{jalali_date_time:%Y-%m-%d %H:%M:%S}'

    @staticmethod
    def is_now_command(command: str) -> bool:
        return command.lower() == 'now'

    @staticmethod
    def is_unix_time(text: str) -> bool:
        return text.isnumeric() and len(text) == 10

    @staticmethod
    def get_readable_now() -> str:
        unix_time = int(time.time())
        return f'{unix_time}\n' + BeautifulTime.create_readable_time(unix_time)
