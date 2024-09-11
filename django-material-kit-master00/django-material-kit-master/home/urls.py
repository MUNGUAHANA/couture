
from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.hOmePage, name='homePage'),
    path('', views.index, name='index'),
    
    path('index1', views.index1, name='index1'),
    path('models', views.models, name='models'),
    path("", include('theme_material_kit.urls')),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('siDm', views.UserLoginViewDressMaker.as_view(), name='loginDM'),
    path('homeDM', views.homeDM, name='homeDM'),
    path('post/add', views.blog_post_add, name='add'),
    path('post/addmod', views.blog_post_addMod, name='addmod'),
]
