from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from .models import Invoice, InvoiceDetail

# Endpoint: "/invoices/" - Fetch all the invoices and post new invoice details instances
@api_view(['GET', 'POST'])
def getAllInvoices(request):
    if request.method == 'GET':
        try:
            # Querying all the invoices
            invoices = InvoiceDetail.objects.all()
            # Serializing the data from the database
            serializer = InvoiceDetailSerializer(invoices, many=True)
            return Response(serializer.data)
        except:
            return Response(serializer.errors, status=400)
        
        
    # Create a new invoice instance and insert in the database
    elif request.method == 'POST':
        try:
            # Creating new invoice details instance from request data and serializing it
            serializer = InvoiceDetailSerializer(data=request.data)
            if serializer.is_valid():
                # Saving the data in the database
                serializer.save()
            return Response(serializer.data, status=201)
        except:
            return Response(serializer.errors, status=400)


# Endpoint: "/invoices/<int:pk>/" - For fetching, updating and deleting particular invoice details
@api_view(['GET', 'PUT', 'DELETE'])
def getInvoiceByID(request, pk):
    id = pk
    # Display the invoice of the specified ID
    if request.method == 'GET':
        try:
            # Querying invoice details by invoiceID 
            invoiceById = InvoiceDetail.objects.filter(invoiceID=id)
            # Serializing the data from the database
            serializer = InvoiceDetailSerializer(invoiceById, many=True)
            return Response(serializer.data)
        except:
            return Response(serializer.errors, status=400)
        
    # Check if the record exists in the database and update it
    elif request.method == 'PUT':
        try:
            # Querying the invoice details by id
            instance = InvoiceDetail.objects.get(id=pk)
        # Catching the exception if requested record to update is not available in the database
        except InvoiceDetail.DoesNotExist:
            return Response(data={"message":"Record not found"},status=404)
        
        # If the record is present in the database, updating, serializing and saving it to the database
        serializer = InvoiceDetailSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    # Check if the record exists in the database and delete it
    elif request.method == 'DELETE':
        try:
            # Querying the invoice details by id
            instance = InvoiceDetail.objects.get(id=pk)
         # Catching the exception if requested record to delete is not available in the database
        except InvoiceDetail.DoesNotExist:
            return Response(data={"message":"Record not found"},status=404)
        
        # Deleting the record if it is present in the database
        instance.delete()
        return Response(data={"message":"Deleted successfully"},status=200)

# Endpoint: "/invoices/allcustomers/" - Fetch all the customers
@api_view(['GET'])
def getAllCustomers(request):
    try:
        # Querying all the customers 
        invoices = Invoice.objects.all()
        # Serializing the data from the database
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
    except:
        return Response(serializer.errors, status=400)