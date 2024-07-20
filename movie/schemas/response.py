from typing import TypeVar, Generic
from pydantic.generics import GenericModel

T = TypeVar('T')

class CustomResponse(GenericModel, Generic[T]):
    content: T
    status: int
    message: str
