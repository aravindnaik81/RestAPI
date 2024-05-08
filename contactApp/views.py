from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ContactBook
from .serializers import ContactSerializers

@api_view(["GET", "POST"])
def contacts_all(request):
    if request.method == "GET":
        all_contacts = ContactBook.objects.all()
        serializer = ContactSerializers(all_contacts, many=True)
        return Response({"Message": "List of Contacts", "Contact List": serializer.data}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ContactSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "New Contact Added", "Contact": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def update_contact(request, pk):
    try:
        contact = ContactBook.objects.get(Phone_Number=pk)
    except ContactBook.DoesNotExist:
        return Response({"Message": "Contact not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ContactSerializers(contact)
        return Response({"Message": "Contact details", "Contact": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = ContactSerializers(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Contact information Updated Successfully", "Contact": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        contact.delete()
        return Response({"Message": "Contact deleted successfully"}, status=status.HTTP_200_OK)
