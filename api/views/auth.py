from rest_framework import views, status
from django.contrib.auth import authenticate, login


class LoginView(views.APIView):
    def post(self, request, format=None):
        data = request.data

        username = data.get("username", None)
        password = data.get("password", None)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return views.Response(status=status.HTTP_200_OK)
            else:
                return views.Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return views.Response(status=status.HTTP_404_NOT_FOUND)
