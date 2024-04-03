# urls.py

from django.urls import path
from .views import SubmitUserInformation, SubmitStoreInformation

urlpatterns = [
    path('submit-user-information/', SubmitUserInformation.as_view(), name='submit_user_information'),
    path('submit-store-information/', SubmitStoreInformation.as_view(), name='submit_store_information'),
]
