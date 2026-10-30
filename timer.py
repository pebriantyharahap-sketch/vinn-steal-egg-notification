
from datetime import datetime, timezone

def get_timer(despawn_time):
    if not despawn_time:
        return "UNKNOWN"

    end = datetime.fromisoformat(
        despawn_time.replace("Z", "+00:00")
    )

    now = datetime.now(timezone.utc)
    remaining = int((end - now).total_seconds())

    if remaining <= 0:
        return "EXPIRED"

    minutes, seconds = divmod(remaining, 60)
    hours, minutes = divmod(minutes, 60)

    return f"{hours:02}:{minutes:02}:{seconds:02}"
