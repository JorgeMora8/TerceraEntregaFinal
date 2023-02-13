from ..models import User, type_of_product, Product, Review

class DAO_sqlite: 
    def __init__(self, model): 
        self.model = model

    def get_all(self): 
        return self.model.objects.all()

    def get_by_type(self, type_to_search): 
        return self.model.objects.filter(type__type=type_to_search)

    def get_by_name(self, name):
        return self.model.objects.filter(name__name = name)




dao_user = DAO_sqlite(User)
dao_product_type = DAO_sqlite(type_of_product)
dao_products = DAO_sqlite(Product)
dao_reviews = DAO_sqlite(Review)