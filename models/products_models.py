from pydantic import BaseModel

class ProductIn(BaseModel):
    bar_code        :   str
    name            :   str
    price           :   int
    stock           :   int


class ProductOut(BaseModel):
    name            :   str
    price           :   int
    stock           :   int