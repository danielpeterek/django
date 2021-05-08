from django.urls import path
from . import views

# URL mapování - seznam URL adres pro aplikaci bazar
urlpatterns = [
    path('', views.index, name='index'),
    path('tenisky', views.SneakersListView.as_view(), name='list'),
    path('tenisky/<int:pk>', views.SneakersDetailView.as_view(), name='detail'),
    path('tenisky/create/', views.TeniskyCreate.as_view(), name='tenisky-create'),
    path('tenisky/<int:pk>/update/', views.TeniskyUpdate.as_view(), name='tenisky-update'),
    path('tenisky/<int:pk>/delete/', views.TeniskyDelete.as_view(), name='tenisky-delete'),
]