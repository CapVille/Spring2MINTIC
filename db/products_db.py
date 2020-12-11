from pydantic import BaseModel
from typing import  Dict

class ProductsInDB(BaseModel):
    bar_code        :   str
    name            :   str
    price           :   int
    stock           :   int



#Base de Datos Ficticia 
database_products = Dict[str, ProductsInDB]
database_products = {

    "123_456": ProductsInDB(**{"bar_code":"123_456",
                                "name":"Torta",
                                "price":12000,
                                "stock":10}),

}

def save_product(product_in_db: ProductsInDB):
    database_products[product_in_db.bar_code] = product_in_db
    return product_in_db


def get_product(bar_code_product: str):
    if bar_code_product in database_products.keys():
        return database_products[bar_code_product]
    else:
        return None

qntity : int
def update_product(bar_code_product: ProductsInDB):
    database_products[bar_code_product.stock] -= qntity
    return None



def get_all_products():
    return database_products.values()