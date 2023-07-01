from pydantic import BaseModel, validator
from typing import List, Union
from datetime import datetime

from pydantic.types import FiniteFloat


class GetLeakRequest(BaseModel):
    id_number: str


class GetLeakResponse(BaseModel):
    leaks: List[dict]


class ErrorMessage(BaseModel):
    detail: str
