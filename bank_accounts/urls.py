from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_list, name='accounts'),

    path('add/', views.add_account),
    path('edit/<int:id>/', views.edit_account),
    path('deactivate/<int:id>/', views.deactivate_account),
    path('transactions/<int:id>/', views.transaction_history),
]