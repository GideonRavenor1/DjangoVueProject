from django.urls import path
from .views import (
    RegisterView, PermissionsAPIView,
    LoginView, AuthenticationView,
    LogoutView, RolesViewSet,
    UserCRUDAPIView, ProfileInfoAPIView,
    ProfilePasswordAPIView
)

app_name = "users"

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('user/', AuthenticationView.as_view(), name="user"),
    path('permissions/', PermissionsAPIView.as_view(), name="permissions"),
    path('roles/', RolesViewSet.as_view({
        "get": "list",
        "post": "create"
    }), name="get_post_roles"),
    path('roles/<int:pk>/', RolesViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }), name="get_put_delete_role"),
    path('info/', ProfileInfoAPIView.as_view(), name="profile-info"),
    path('password/', ProfilePasswordAPIView.as_view(), name="profile-password"),
    path('', UserCRUDAPIView.as_view(), name="users"),
    path('user/<int:pk>/', UserCRUDAPIView.as_view(), name="user")



]