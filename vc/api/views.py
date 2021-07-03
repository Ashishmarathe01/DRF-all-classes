from django.shortcuts import render

# Create your views here.

from .models import  Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
# for two combine classs
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
# for three combine class
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class StudentList(ListAPIView): # this will done all thing for us reagrding listing
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCre(CreateAPIView): # this will done all thing for us reagrding listing
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRe(RetrieveAPIView): # this will done all thing for us reagrding listing
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUp(UpdateAPIView): # this will done all thing for us reagrding listing
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDe(DestroyAPIView): # this will done all thing for us reagrding listing
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#### not combine stared##########################################################################


class StudenLC(ListCreateAPIView): # this will done all thing for us reagrding listing
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudenRU(RetrieveUpdateAPIView): # this will done all thing for us reagrding listing
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudenRD(RetrieveDestroyAPIView): # this will done all thing for us reagrding listing
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# for three combine class ########################

class StudenRUD(RetrieveUpdateDestroyAPIView): # this will done all thing for us reagrding listing
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# # if you only want to do CRUD operation use only two classes i.e RetrieveUpdateDestroyAPIView and ListCreateAPIView#######

class StudentLC(ListCreateAPIView): # for non id oprations
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRUD(RetrieveUpdateDestroyAPIView): # for id oprations
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


