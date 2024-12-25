from pydantic import BaseModel


class getOffice(BaseModel):
    """Модель для сериализации руководителя"""

    id: int
    name: str
    location: str

    model_config = {"from_attributes": True}
