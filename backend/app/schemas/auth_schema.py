from pydantic import BaseModel


class TokenSchema(BaseModel):
    """Модель для сериализации токена"""

    access_token: str
    token_type: str
