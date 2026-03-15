# Loosely based on Rust result type

from typing import Generic, TypeVar, Literal
from pydantic import BaseModel
import random

T = TypeVar("T")

class Ok(BaseModel, Generic[T]):
    status: Literal["ok"] = 'ok'
    is_ok: bool = True
    value: T

class Err(BaseModel):
    status: Literal["err"] = 'err'
    is_ok: bool = False
    error: str

type Result[T] = Ok[T] | Err

def example_function(success: bool) -> Result[int]:
    if success:
        return Ok(value=42)
    return Err(error="Something went wrong")

if __name__ == "__main__":
    result = example_function(success=random.choice([True, False]))
    print(f"{result=}, {result.status=}, {result.is_ok is True=}")