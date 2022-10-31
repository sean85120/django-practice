from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PeopleForm
from .filters import PeopleFilterSet

from rest_framework import views
from django.contrib.auth import logout

from .serializers import LoginSerializer
from django.contrib.auth import login

from .models import People
from .serializers import PeopleSerializer, People2Serializer
from rest_framework import generics

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegisterSerializer


# Create your views here.


def index(request):
    return HttpResponse("Hello world!")


def hello(request):
    context = {"name": "Sean"}
    return render(request, "hello.html", context)


def form(request):

    form = PeopleForm()

    if request.method == "POST":
        form = PeopleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/hello")

    context = {
        "form": form,
    }

    return render(request, "form.html", context)


class PeopleListAPIView(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filter_class = PeopleFilterSet


class PeopleCreateAPIView(generics.CreateAPIView):
    queryset = People.objects.all()
    serializer_class = People2Serializer


class PeopleUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = People.objects.all()
    serializer_class = People2Serializer


@api_view(["GET"])
def people_data(request):
    if request.method == "GET":
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)

        return Response(serializer.data)


@api_view(["GET", "POST"])
def people_list(request):

    if request.method == "GET":
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Account has been created successfully"},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"message": "The input content is invalid"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = LoginSerializer(
            data=request.data, context={"request": self.request}
        )

        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request, user)
            msg = {"success": True, "message": "Validation success"}
            return Response(msg, status=status.HTTP_202_ACCEPTED)

        return Response(
            {
                "success": False,
                "message": "Wrong username or password",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class LogoutAPIView(views.APIView):
    def get(self, request):
        logout(request)

        return Response({"message": "logout successfully"}, status=status.HTTP_200_OK)
