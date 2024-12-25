from pydantic import BaseModel


class getCandidate(BaseModel):
    """Модель для сериализации кандидата"""

    id: int
    email: str
    full_name: str
    quotas: int
    phone: str

    model_config = {"from_attributes": True}
