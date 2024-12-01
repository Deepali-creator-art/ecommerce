from .models import Category
from django.conf import settings
def menu_links(request):
    links=Category.objects.all()
    print(links)
    return dict(links=links)
def get_paypal_client_id(request):
    return {'PAYPAL_CLIENT_ID':settings.PAYPAL_CLIENT_ID}