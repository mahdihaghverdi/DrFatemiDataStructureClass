import enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from zoneinfo import ZoneInfo

import humanize


class Priority(str, enum.Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class Task:
    title: str
    priority: "Priority"
    time_limit: int
    steps: Optional[list[str]] = None
    note: Optional[str] = None
    _creation: datetime = field(
        default=datetime.now(ZoneInfo("Asia/Tehran")),
        init=False,
    )

    @property
    def creation(self):
        return self._creation.strftime("%d %B, %Y %H:%M:%S")

    @property
    def humanize_creation(self):
        return humanize.naturaltime(
            datetime.now(ZoneInfo("Asia/Tehran")) - self._creation,
        )
