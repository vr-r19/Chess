from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class UserListView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]

