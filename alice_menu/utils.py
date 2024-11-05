from django.db import models
from django.http import JsonResponse


class Manger(models.Manager):
    def is_not_deleted(self):
        return self.filter(is_deleted=False)

    def active(self):
        return self.filter(is_deleted=False, status=True)


class BaseModel(models.Model):
    """
    This is the base model for all the models.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    sorting_order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    objects = Manger()

    class Meta:
        abstract = True
        ordering = ["-created_at"]

class DeleteMixin:
    def remove_from_DB(self, request):
        try:
            object_id = request.GET.get("pk", None)
            object = self.model.objects.get(id=object_id)
            object.is_deleted = True
            object.save()

            return True
        except Exception as e:
            print(e)
            return str(e)

    def get(self, request):
        status = self.remove_from_DB(request)
        return JsonResponse({"deleted": status})

import qrcode
from django.core.files.base import ContentFile
def generate_qr_code(url, hash_value, hashvalue_obj):
    # Combine the URL and hash into a single string
    data = f"{url}/initialize?hash={hash_value}"
    
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a BytesIO object
    from io import BytesIO
    img_buffer = BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    # Create a unique filename based on the table number
    filename = f'table{hashvalue_obj.table}qr.png'

    # Save the image in the image field of the HashValue instance
    hashvalue_obj.qr_code.save(filename, ContentFile(img_buffer.getvalue()), save=True)