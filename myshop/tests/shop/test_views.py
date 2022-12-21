from django.test import TestCase
from django.urls import reverse
from tests.test_model_mixin import ModelMixinTestCase
from shop.models import Product


class TestListView(ModelMixinTestCase, TestCase):
    def test_list_views_shows_all_products_when_category_not_selected(self):
        response = self.client.get(reverse("shop:product_list"))
        All_products = Product.objects.all()
        self.assertQuerysetEqual(
            response.context.get("products"), All_products
        )

    def test_list_views_shows_products_of_particular_category_when_category_selected(
        self,
    ):
        response = self.client.get(
            reverse(
                "shop:product_list_by_category",
                args=[
                    self.first_category.slug,
                ],
            )
        )
        First_category_products = Product.objects.filter(
            category=self.first_category
        )
        self.assertQuerysetEqual(
            response.context.get("products"), First_category_products
        )

    def test_list_views_displays_no_products_message_for_category_selected_without_products(
        self,
    ):
        response = self.client.get(
            reverse(
                "shop:product_list_by_category",
                args=[
                    self.third_category.slug,
                ],
            )
        )
        No_products_message = (
            "No Products in this category, We will get u soon!"
        )
        self.assertInHTML(No_products_message, response.content.decode())

    def test_list_views_returns_404_for_invalid_category(self):
        response = self.client.get(
            reverse(
                "shop:product_list_by_category", args=["invalid_category_slug"]
            )
        )
        self.assertEqual(response.status_code, 404)

    def test_list_views_shows_correct_name_price_of_the_product(self):
        response = self.client.get(
            reverse(
                "shop:product_list_by_category",
                args=[
                    self.second_category.slug,
                ],
            )
        )

        product_name = self.second_product.name
        product_price = str(self.second_product.price)

        self.assertIn(product_name, response.content.decode())
        self.assertIn(product_price, response.content.decode())

    def test_list_views_shows_default_image_for_product_if_no_picture_is_added(
        self,
    ):
        response = self.client.get(
            reverse(
                "shop:product_list_by_category",
                args=[
                    self.second_category.slug,
                ],
            )
        )
        self.assertIn("no_image.png", response.content.decode())


class TestDetailView(ModelMixinTestCase, TestCase):
    def test_detail_returns_details_of_correct_product(self):
        response = self.client.get(
            reverse(
                "shop:product_detail",
                args=[self.first_product.id, self.first_product.slug],
            )
        )
        self.assertEquals(response.context.get("product"), self.first_product)

    def test_detail_returns_returns_404_for_invalid_details_of_product(self):
        response = self.client.get(
            reverse(
                "shop:product_detail",
                args=[self.first_product.id, "Invalid_category_slug"],
            )
        )
        self.assertEquals(response.status_code, 404)
