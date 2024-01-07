from rest_framework import status
from rest_framework.test import APITestCase
from .models import Invoice, InvoiceDetail

class InvoiceDetailsTest(APITestCase):

    # Name idData stands for invoiceDetailsData (used shortform for simplicity)
    idData = {
        "id":1,
        "invoiceID":1,
        "description":"Description of the transaction",
        "quantity":5,
        "unit_price":100,
        "price":500
    }
    # Name id stands for invoiceDetails (used shortform for simplicity)
    id = {
        "id":1,
        "date":"2024-01-06",
        "customerName":"Mahesh"
    }

    # This method runs before running each of the tests
    def setUp(self):
        # Creating the database records required for testing
        Invoice.objects.create(id=self.id['id'], date=self.id['date'], customerName=self.id['customerName'])
        invoiceID = Invoice.objects.get(id=1)
        InvoiceDetail.objects.create(id=self.idData['id'], invoiceID=invoiceID, description=self.idData['description'], quantity=self.idData['quantity'], unit_price=self.idData['unit_price'], price=self.idData['price'])

    # Testing the GET method
    # Endpoint: /invoices/
    def test_get_invoice_details(self):
        
        response = self.client.get("/invoices/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['invoiceID'], self.idData['invoiceID'])
        self.assertEqual(response.data[0]['description'], self.idData['description'])
        self.assertEqual(response.data[0]['quantity'], self.idData['quantity'])
        self.assertEqual(response.data[0]['unit_price'], self.idData['unit_price'])
        self.assertEqual(response.data[0]['price'], self.idData['price'])
    
    # Testing the POST method
    # Endpoint: /invoices/
    def test_post_invoice_details(self):
        # The data to be sent as payload for the POST request
        data = {
            "id":1,
            "invoiceID":1,
            "description":"Description of the transaction",
            "quantity":5,
            "unit_price":100,
            "price":500
        }
        response = self.client.post("/invoices/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Testing the DELETE method
    # Endpoint: /invoices/<int:pk>/
    def test_delete_invoice_details(self):
        response = self.client.delete("/invoices/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Testing the PUT method
    # Endpoint: /invoices/<int:pk>/
    def test_put_invoice_details(self):
        # The data to be sent as payload for the PUT request
        data = {
            "invoiceID":1,
            "description":"New Description of the transaction",
            "quantity":5,
            "unit_price":100,
            "price":500
        }
        response = self.client.put("/invoices/1/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['invoiceID'], data['invoiceID'])
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.data['quantity'], data['quantity'])
        self.assertEqual(response.data['unit_price'], data['unit_price'])
        self.assertEqual(response.data['price'], data['price'])