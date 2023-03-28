from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from infrastructure.exceptions.validation_exception import ValidationException


@dataclass(frozen=True)
class DateTime():
    dateTime: Optional[str]

    def __post_init__(self):
        if self.dateTime is not None:
            try:
                datetime.strptime(self.dateTime, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                print(ValidationException(self.dateTime, 'dateTime invalido'))
                raise ValidationException(self.dateTime, 'dateTime invalido')