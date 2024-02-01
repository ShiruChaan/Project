from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
]

urlpatterns += [
    path('api/projects/', api.ProjectList.as_view(), name='api_project_list'),
    path('api/projects/<int:pk>/', api.ProjectDetails.as_view(), name='api_project_details'),

    path('api/feedback/', api.FeedbackList.as_view(), name='api_feedback_list'),
    path('api/feedback/<int:pk>/', api.FeedbackDetails.as_view(), name='api_feedback_details'),

    path('api/posts/', api.PostList.as_view(), name='api_post_list'),
    path('api/posts/<int:pk>/', api.PostDetails.as_view(), name='api_post_details'),

    path('api/contact_requests/', api.ContactRequestList.as_view(), name='api_contact_request_list'),
    path('api/contact_requests/<int:pk>/', api.ContactRequestDetails.as_view(), name='api_contact_request_details'),

]