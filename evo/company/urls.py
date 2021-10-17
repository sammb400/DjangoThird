from django.urls import path
from django.urls.resolvers import URLPattern
from .views import ( JobPlanListView, JobPlanCreateView, JobPlanDetailView, JobPlanUpdateView, JobPlanDeleteView,
                        MarketPlanListView, MarketPlanCreateView, MarketPlanDetailView, MarketPlanUpdateView, MarketPlanDeleteView)


urlpatterns = [
    #jobplan
    path('jobp/', JobPlanListView.as_view() , name="job_p"),
    path('jobp/<str:pk>', JobPlanDetailView.as_view() , name="job_p_detail"),
    path('jobp/<str:pk>/update', JobPlanUpdateView.as_view() , name="job_p_update"),
    path('jobp/<str:pk>/delete', JobPlanDeleteView.as_view() , name="job_p_delete"),
    path('jobp/new/', JobPlanCreateView.as_view() , name="job_p_create"),
    #marketplan
    path('marketp/', MarketPlanListView.as_view() , name="market_p"),
    path('marketp/<str:pk>', MarketPlanDetailView.as_view() , name="market_p_detail"),
    path('marketp/<str:pk>/update', MarketPlanUpdateView.as_view() , name="market_p_update"),
    path('marketp/<str:pk>/delete', MarketPlanDeleteView.as_view() , name="market_p_delete"),
    path('marketp/new/', MarketPlanCreateView.as_view() , name="market_p_create"),
]