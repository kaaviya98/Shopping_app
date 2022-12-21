from django.test import TestCase
from shop.models import Product, Category


class ModelMixinTestCase(TestCase):
    def setUp(self):
        self.first_category = Category.objects.create(
            name="Food",
            slug="food",
        )
        self.second_category = Category.objects.create(
            name="Gadgets",
            slug="gadgets",
        )
        self.third_category = Category.objects.create(
            name="Clothes",
            slug="clothes",
        )

        self.first_product = Product.objects.create(
            category=self.first_category,
            name="Briyani",
            slug="briyani",
            description="Tasty",
            price=120.20,
        )
        self.second_product = Product.objects.create(
            category=self.second_category,
            name="Iphone",
            slug="iphone",
            description="Costly",
            price=50000,
        )
