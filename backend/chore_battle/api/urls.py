from codecs import lookup
from django.urls import path
from .views import ChoreView, LoginView, HistoryView, HistoryDetailView, UserView, CookieTokenRefreshView, LogoutView, ScoreView
from rest_framework import routers

ROUTER = routers.DefaultRouter()
ROUTER.register(r"chores",ChoreView)

urlpatterns = [
    path('auth/refresh/', CookieTokenRefreshView.as_view(), name="refresh"),
    path('auth/login/', LoginView.as_view(), name="login"),
    path("auth/logout/",LogoutView.as_view(), name="logout"),

    path('history/', HistoryView.as_view(), name="history"),
    path('history/<int:pk>/', HistoryDetailView.as_view(), name="history-detail"),

    path('users/<int:pk>/', UserView.as_view(), name="user-detail"),
    path('score/<int:pk>/', ScoreView.as_view(), name="score"),
]

urlpatterns += ROUTER.urls