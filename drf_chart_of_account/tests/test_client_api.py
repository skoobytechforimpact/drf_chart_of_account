"""Test cases for LayerModel views apis."""
from django.test import TestCase
from rest_framework.test import RequestsClient
from ..models import LayerOneModel


class LayerViewsAPITestCases(TestCase):
    """Testing various apis of the Layer views."""

    client = RequestsClient()

    def setUp(self):
        """Set up all layers post request apis."""
        # self.client.post('/accounts/charts/layer/one/', {'name': 'test_api_layer_one', 'created_by': 1}, format='json')

    def test_post_request_apis(self):
        """Test all layers post request apis."""
        request = self.client.post('http://127.0.0.1:8000/accounts/charts/layer/one/', {'name': 'test_api_layer_one', 'created_by': 1})
        self.assertEqual(request.status_code, 201)

    def test_layer_one_model_viewsets_api(self):
        """Test layer one viewsets apis."""
        request = self.client.get('/accounts/charts/layer/one/')
        self.assertEqual(request.status_code, 200)
