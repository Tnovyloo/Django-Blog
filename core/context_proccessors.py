from .models import Category

def navbar_context(request):
    return {'category_menu': Category.objects.all(), }

