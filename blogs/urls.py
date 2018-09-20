from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('404/', views.not_found_page, name='not_found_page'),
    path('article/', views.article_list_page, name='article_list_page'),
    # path('<int:pk>/', views.DetailsView.as_view()   , name='details'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]