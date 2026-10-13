from datetime import datetime, date

from pydantic import BaseModel, ConfigDict


class SleepResponse(BaseModel):

    SleepID: int

    UserID: int

    SleepDate: date

    SleepStart: datetime

    SleepEnd: datetime

    DurationMinutes: int

    SleepQuality: int

    model_config = ConfigDict(
        from_attributes=True
    )