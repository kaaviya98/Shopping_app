from django.test import TestCase
from tests.test_model_mixin import ModelMixinTestCase
from django.urls import reverse


class TestModelMethod(ModelMixinTestCase, TestCase):
    def test_absolute_url_in_Category_model_returns_product_list_view(self):
        product_list_category = reverse(
            "shop:product_list_by_category", args=[self.first_category.slug]
        )
        self.assertEqual(
            product_list_category, self.first_category.get_absolute_url()
        )

    def test_absolute_url_in_Product_model_returns_product_detail_view(self):
        product_detail_view = reverse(
            "shop:product_detail",
            args=[self.first_product.id, self.first_product.slug],
        )
        self.assertEqual(
            product_detail_view, self.first_product.get_absolute_url()
        )
