from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import ProductInventory


@registry.register_document
class ProductInventoryDocument(Document):

    product = fields.ObjectField(properties={"name": fields.TextField()})

    class Index:
        name = "productinventory"

    class Django:
        model = ProductInventory

        fields = [
            "id",
            "sku",
        ]
