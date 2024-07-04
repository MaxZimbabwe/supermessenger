from ...models.products_moderation import ProductsModeration
from ...models.usuarios import Usuario
from ...extension import db

class ProductsModerationServices:

    def __init__(self) -> None:
        pass

    def store(params: dict):
        try:
            products = ProductsModeration(tuple(params))
            db.session.add(products)
            db.session.commit()
            return 'Product stored successfully'
        except Exception as e:
            db.session.rollback()
            raise Exception({'status': 'error', 'message': str(e)})

    def update(params: dict):
        try:
            product = ProductsModeration.query.get(params.get("idproduto"))
            if not product:
                raise Exception({'status': 'error', 'message': 'Product not found'})
            
            product.ativo = params.get("ativo")
            product.titulo = params.get("titulo")
            product.descricao = params.get("descricao")

            db.session.commit()

            return 'Product updated successfully'
        
        except Exception as e:
            raise Exception({'status': 'error', 'message': str(e)})

    def search(filters: list):
        try:
            products = db.session.query(ProductsModeration).join(Usuario)
            for condition in filters:
                products.filter(condition)
            return products.all()
        except Exception as e:
            raise Exception({'status': 'error', 'message': str(e)})
