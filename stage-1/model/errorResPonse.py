from pydantic import BaseModel


class ErrorResponse(BaseModel):
    number: str
    error: bool = True