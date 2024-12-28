from pydantic import BaseModel


class getOffice(BaseModel):
    """Модель для сериализации руководителя"""

    id: int
    name: str
    location: str

    class ConfigDict:
        from_attributes = True
