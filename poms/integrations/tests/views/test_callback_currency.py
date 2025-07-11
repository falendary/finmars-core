from poms.common.common_base_test import BaseTestCase
from poms.currencies.models import Currency
from poms.integrations.database_client import get_backend_callback_urls
from poms.integrations.tests.common_callback_test import CallbackSetTestMixin


class CallbackCurrencyViewSetTest(CallbackSetTestMixin, BaseTestCase):
    databases = "__all__"

    def setUp(self):
        super().setUp()
        self.init_test_case()
        self.url = get_backend_callback_urls()["currency"]

    def test__currency_created(self):
        task = self.create_task(
            name="Import Currency From Finmars Database",
            func="import_currency_finmars_database",
        )
        user_code = self.random_string(3)
        post_data = {
            "request_id": task.id,
            "task_id": None,
            "data": {
                "id": self.random_int(),
                "user_code": user_code,
                "short_name": f"short_{user_code}",
                "name": f"name_{user_code}",
            },
        }
        response = self.client.post(path=self.url, format="json", data=post_data)
        self.assertEqual(response.status_code, 200, response.content)

        response_json = response.json()
        self.assertEqual(response_json["status"], "ok", response_json)
        self.assertNotIn("message", response_json)

        currency = Currency.objects.filter(user_code=user_code).first()

        self.assertIsNotNone(currency)
        self.assertEqual(currency.user_code, user_code)
        self.assertEqual(currency.short_name, f"short_{user_code}")
        self.assertEqual(currency.name, f"name_{user_code}")
