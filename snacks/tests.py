from django.test import TestCase
from .models import Snack
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.


class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="khrais", email="2014988155@ses.yu.edu.jo", password="khraisawon"
        )

        self.snack = Snack.objects.create(
            title="mansaf",
            purchaser=self.user,
            description="amazing mansaf",
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "mansaf")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "mansaf")
        self.assertEqual(f"{self.snack.purchaser}", "khrais")
        self.assertEqual(self.snack.description, "amazing mansaf")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "mansaf")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack-detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "snack_detail.html")
