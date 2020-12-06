from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()

router.register('coronagevallen', views.CoronaView)

urlpatterns = [
    path('', include(router.urls))
	path('openapi/', get_schema_view(
        title="aantal besmette mensen per land",
        description="schema waarin je kan zien hoeveel mensen er besmet zijn per land"
    ), name='openapi-schema'),
]