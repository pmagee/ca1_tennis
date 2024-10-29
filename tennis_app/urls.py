from django.urls import path
from .views import HomePageView, ClubListView, CompListView, MemListView, CompCreateView,CompDetailView, query1, query2


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('clublist/', ClubListView.as_view(), name='club_list'),
    path('memlist/', MemListView.as_view(), name='m_list'),
    path('complist/', CompListView.as_view(), name='c_list'),
    path('newc/', CompCreateView.as_view(), name='comp_new'),
    path('comp/<int:pk>/', CompDetailView.as_view(), name='comp_detail'),
    path('query1/', query1, name='query1'),
    path('query2/', query2, name='query2'),
]