from django.urls import path
from .import views
app_name='college_app'
urlpatterns = [
    path('',views.index,name='index'),
    # path('<slug:cslug>/',views.allprodCat,name='prod_by_cat'),
    # path('<slug:cslug>/<slug:product_slug>',views.ProDetail,name='all_pro_detail'),
]