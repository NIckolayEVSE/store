from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView, ListView

from products.models import Product, ProductCategory, Basket


# Create your views here.

class IndexView(TemplateView):
    template_name = 'products/index.html'

    # extra_context = {'title': 3}

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Store'
        return context


# def index(request):
#     context = {
#         'title': 'Store',
#     }
#     return render(request, 'products/index.html', context=context)

class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id', 0)
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data()
        contex['title'] = 'Store - Каталог'
        contex['categories'] = ProductCategory.objects.all()
        return contex


# def products(request, category_id: int = 0, page_number: int = 1):
#     products_all = Product.objects.all() if not category_id else Product.objects.filter(category_id=category_id)
#
#     per_page = 3
#     paginator = Paginator(products_all, per_page).page(page_number)
#
#     context = {
#         'title': 'Store - Каталог',
#         'categories': ProductCategory.objects.all(),
#         'products': paginator,
#         'category_id': category_id
#     }
#     return render(request, 'products/products.html', context=context)


@login_required  # декоратор доступа
def basket_add(request, product_id):
    product = Product.objects.get(pk=product_id)
    baskets = Basket.objects.get_or_create(user=request.user, product=product)[0]
    baskets.quantity += 1
    baskets.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_pk):
    Basket.objects.get(pk=basket_pk).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
