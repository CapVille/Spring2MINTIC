from db.products_db import ProductsInDB
from db.products_db import get_product, update_product, get_all_products, save_product

from models.products_models import ProductIn, ProductOut

from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.post("/product/")
async def create_product(product_in: ProductIn):
    #Todas las comprobaciones Necesarias
    product_in_db = get_product(product_in.bar_code)

    if product_in_db != None:
        raise HTTPException(status_code=400, detail="La Categoria ya existe")
    
    #Guardando Categoria
    product_saved = save_product(ProductsInDB(**product_in.dict()))

    return ProductOut(**product_saved.dict())


@api.get("/product/{bar_code}")
async def get_product_bar_code(bar_code: str):
    #Buscar la categoria en la base datos
    product_in_db = get_product(bar_code)

    #Comprobar la respuesta
    if product_in_db == None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    #Retorna la categoria
    return ProductOut(**product_in_db.dict())


@api.put("/product/")
async def update_product(product_in: ProductIn):
    #Buscar la categoria en la base datos
    product_in_db = get_product(product_in.bar_code)

    #Comprobar la respuesta
    if product_in_db == None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    #Actualizar product
    product_updated = save_product(ProductsInDB(**product_in.dict()))

    #Retornando Respuesta
    return ProductOut(**product_updated.dict())


@api.get("/products/")
async def get_all():
    products_db = get_all_products()

    products_out = []
    for product_db in products_db:
        products_out.append(ProductOut(**product_db.dict()))

    return products_out