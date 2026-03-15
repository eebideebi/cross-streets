# Loosely based on Rust result type

from typing import Generic, TypeVar
from pydantic import BaseModel
import random

T = TypeVar("T")

class Ok(BaseModel, Generic[T]):
    value: T

class Err(BaseModel):
    error: str

type Result[T] = Ok[T] | Err

def example_function(success: bool) -> Result[int]:
    return Ok(value=success) if success else Err(error="Something went wrong")

if __name__ == "__main__":
    result = example_function(random.choice([True, False]))
    print(f"{result=}, {isinstance(result, Ok)=}")