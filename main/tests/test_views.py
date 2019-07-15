from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from main import models

# Create your tests here.
class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'BookTime')


    def test_about_us_page_works(self):
        response = self.client.get(reverse("about-us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
        self.assertContains(response, "BookTime")


    def test_products_page_returns_active(self):
        models.Product.objects.create(
            name="The cathedral and the bazaar",
            slug="cathedral-bazaar",
            price=Decimal("10.00")
        )

        models.Product.objects.create(
            name = "A tale of two cities",
            slug = "tale-two-cities",
            price = Decimal("2.00"),
            active = False
        )

        response = self.client.get(
            reverse("products", kwargs={"tag":"all"})
        )

        # testing if the response returned successfully and base template extension works
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BookTime")

        # testing if the products um expecting to come back actually came back in response
        product_list = models.Product.objects.active().order_by("name")
        self.assertEqual(
            list(response.context["object_list"]),
            list(product_list)
        )
