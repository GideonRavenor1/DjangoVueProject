from rest_framework import views, generics, status, exceptions, viewsets, permissions, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serializers import UsersSerializer, PermissionSerializer, RoleSerializer
from .models import User, Permission, Role
from .authentications import generate_access_token, JWTAuthentication
from .permissions import CustomPermission


class RegisterView(views.APIView):

    @staticmethod
    def post(request):
        data = request.data
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Password do not match')

        serializer = UsersSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})


class LoginView(generics.GenericAPIView):

    @staticmethod
    def post(request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user is None:
            raise exceptions.AuthenticationFailed({"data": 'User not found'})

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed({"data": 'Incorrect password'})

        response = Response()

        token = generate_access_token(user)
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class LogoutView(views.APIView):

    @staticmethod
    def post(request,
             ):
        response = Response()
        response.delete_cookie(key='jwt')
        response.data = {
            'data': {"message": "success"}
        }
        return response


class AuthenticationView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        serializer = UsersSerializer(request.user).data
        try:
            serializer["permissions"] = [permission["name"] for permission in serializer["role"]["permissions"]]
        except TypeError:
            serializer["permissions"] = ['view_products']
        data = {
            'data': serializer
        }

        return Response(data)


class PermissionsAPIView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        data = {
            'data': serializer.data
        }

        return Response(data)


class RolesViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated & CustomPermission]
    permission_object = 'roles'

    @staticmethod
    def list(request):
        serializer = RoleSerializer(Role.objects.all(), many=True)
        data = {
            'data': serializer.data
        }
        return Response(data)

    @staticmethod
    def retrieve(request, pk=None):
        serializer = RoleSerializer(get_object_or_404(Role, pk=pk))
        data = {
            'data': serializer.data
        }
        return Response(data)

    @staticmethod
    def create(request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @staticmethod
    def update(request, pk=None):
        serializer = RoleSerializer(instance=get_object_or_404(Role, pk=pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_202_ACCEPTED)

    @staticmethod
    def destroy(request, pk=None):
        role = get_object_or_404(Role, pk=pk)

        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCRUDAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated & CustomPermission]
    permission_object = 'users'
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def get(self, request, pk=None):
        if pk:
            data = {
                "data": self.retrieve(request, pk).data
            }
            return Response(data)
        return self.list(request)

    def post(self, request):
        request.data.update({
            'password': 1234,
            'role': request.data['role_id']
        })
        data = {
            "data": self.create(request).data
        }
        return Response(data)

    def put(self, request, pk=None):
        if request.data["role_id"]:
            request.data.update({
                'role': request.data['role_id']
            })
        data = {
            "data": self.partial_update(request, pk).data
        }
        return Response(data)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class ProfileInfoAPIView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def put(request, pk=None):
        if request.data["role_id"]:
            request.data.update({
                'role': request.data['role_id']
            })
        user = request.user
        serializer = UsersSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            "data": serializer.data
        }
        return Response(data)


class ProfilePasswordAPIView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def put(request, pk=None):
        user = request.user
        if request.data["password"] != request.data["password_confirm"]:
            raise exceptions.ValidationError("Passwords do not match")
        serializer = UsersSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            "data": serializer.data
        }
        return Response(data)

