from abc import ABC, abstractclassmethod


class ProductAbstract(ABC):

    @abstractclassmethod
    def create_product(self, name, price):
        pass

    @abstractclassmethod
    def edit_product(self, product_id, name, price):
        pass

    @abstractclassmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractclassmethod
    def get_all_products(self):
        pass

    @abstractclassmethod
    def upload_product_image(self, product_id, image_path):
        pass

    @abstractclassmethod
    def delete_product(self, product_id):
        pass


class ProductManager(ProductAbstract):
    def create_product(self, name: str, price):
        print(f"Product: {name}({price} GHS) created")

    def edit_product(self, product_id):
        print(f"Product with ID: {product_id} edited")

    def get_product_by_id(self, product_id):
        print(f"Product with ID {product_id} retrieved")

    def get_all_products(self):
        print("All the product retrieved")

    def upload_product_image(self, product_id, image_path):
        print(
            f"You upload the image of the product with ID {product_id} is uploaded under the path {image_path}")

    def delete_product(self, product_id):
        print(f"Product with ID {product_id} deleted")


product = ProductManager()
product.create_product('Champoo', 12)
product.edit_product(1)
product.get_product_by_id(1)
product.get_all_products()
product.upload_product_image(1, 'photo')
product.delete_product(1)
