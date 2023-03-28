import uuid
from dataclasses import dataclass
from typing import ClassVar

from infrastructure.exceptions.validation_exception import ValidationException


@dataclass(frozen=True)
class UUIDValue():
    __uuidVersion: ClassVar[int] = 4
    myUuid: str

    def __post_init__(self):
        try:
            uuid.UUID(self.myUuid, version=UUIDValue.__uuidVersion)
            return True
        except ValueError as err:
            print(ValidationException(self.myUuid, "uuid debe ser un uuid valido"))
            raise ValidationException(self.myUuid, "uuid debe ser un uuid valido")

    def __str__(self):
        return self.myUuid

    def __repr__(self):
        return self.myUuid
