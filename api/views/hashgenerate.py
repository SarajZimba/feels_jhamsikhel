from rest_framework.views import APIView
from api.serializers.hashgenerate import HashValueSerializer
from rest_framework.response import Response
from order.models import HashValue

class HashAPIView(APIView):
    def post(self, request, *args, **kwargs):
        posted_data = request.data
        outlet = posted_data['outlet']
        table = posted_data['table']
        try:
            serializer = HashValueSerializer(data=posted_data)

            if serializer.is_valid():
                hashvalue_obj = HashValue.objects.filter(outlet=outlet, table=table)
                if hashvalue_obj:
                    hashvalue_obj.delete()

                hashvalue_obj = serializer.save()

                hashvalue = hashvalue_obj.hash_value

                # return Response({"hashvalue": f"backend.silverlimenu.silverlinepos.com/{hashvalue}"}, 200)
                return Response({"hashvalue": hashvalue}, 200)

            else:
                return Response(e, 400)
        except Exception as e:
            return Response(e, 400)        

from menu.models import Organization
class GiveTableOutletHashAPIView(APIView):
    def get(self, request, *args, **kwargs):
        hashvalue = kwargs.get('hashvalue')
        org = Organization.objects.first()
        try:
            hashvalue_obj = HashValue.objects.get(hash_value=hashvalue)
            dict = {
                "org_name": org.name,
                "org_address": org.address, 
                "org_logo": org.org_logo.url if org.org_logo else None, 
                "background_image": org.background_image.url if org.background_image else None,
                "outlet": hashvalue_obj.outlet, 
                "table_no": hashvalue_obj.table
            }
            return Response(dict, 200)
        except Exception as e:
            return Response(e, 400)
        
class ClearHashValue(APIView):
    def get(self, request, *args, **kwargs):
        hashvalue = kwargs.get('hashvalue')
        try:
            hashvalue_obj = HashValue.objects.get(hash_value=hashvalue)
            hashvalue_obj.delete()
            return Response("Hash object deleted successfully", 200)
        except Exception as e:
            return Response(e, 400)
            
import hashlib

def create_hash(outlet, table):
        hash_object = hashlib.sha256()
        hash_object.update(f"{outlet}{table}".encode('utf-8'))
        hash_value = hash_object.hexdigest()
        return hash_value
from alice_menu.utils import generate_qr_code
# class CreateQrAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         data = request.data

#         outlet = data['outlet']
#         start = data['start']
#         end= data['end']
#         url = data['url']

#         for i in range(int(start), int(end)+1):
#             hash_value = create_hash(outlet, i)
#             hashvalue_obj = HashValue.objects.create(outlet=outlet, url=url, table=i, hash_value=hash_value)
#             # def generate_qr_code(url, hash_value, hashvalue_obj):
#             generate_qr_code(url,hash_value, hashvalue_obj)

    
#         return Response("Qr code generated sucessfully", 200)

from rest_framework.response import Response
from rest_framework import status

class CreateQrAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        outlet = data['outlet']
        start = data['start']
        end = data['end']
        url = data['url']


        for i in range(int(start), int(end) + 1):
            if HashValue.objects.filter(table=i, outlet=outlet).exists():
                return Response(f"Hash and Qr for this table {i} for this {outlet} already exists", 400)

            hash_value = create_hash(outlet, i)
            hashvalue_obj = HashValue.objects.create(outlet=outlet, url=url, table=i, hash_value=hash_value)

            # Generate the QR code for the hash value
            generate_qr_code(url, hash_value, hashvalue_obj)

        return Response({"message": "QR codes generated successfully."}, status=status.HTTP_201_CREATED)

