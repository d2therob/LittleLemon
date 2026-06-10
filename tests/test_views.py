from django.test import TestCase
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User



class MenuViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass"
    )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.item1 = MenuItem.objects.create(title="Pizza", price=10.00, inventory=5)
        self.item2 = MenuItem.objects.create(title="Burger", price=8.50, inventory=10)
        self.item3 = MenuItem.objects.create(title="Pasta", price=12.00, inventory=7)



    def test_getall(self):
        # Get response from API endpoint
        response = self.client.get('/restaurant/menu/') 

        # Get all objects from DB
        items = MenuItem.objects.all()

        # Serialize them
        serializer = MenuItemSerializer(items, many=True)

        # Assert response matches serialized data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)



