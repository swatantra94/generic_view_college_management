from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from main import models

# Create your views here.
class Index(View):
    def get(self,request):
        return HttpResponse("Get Request")
    def post(self,request):
        return HttpResponse("Post Request")

class CollegeDetail(DetailView):
    model = models.College
    template_name = 'college_detail.html'

class CollegeList(ListView):
    model = models.College
    template_name = 'college_list.html'
    context_object_name = 'colleges'

class StudentCreate(CreateView):
    model = models.Student
    template_name = 'create_student.html'
    fields = '__all__'
    success_url = '/college'

class CollegeCreate(CreateView):
    model = models.College
    template_name = 'create_college.html'
    fields = '__all__'
    success_url = '/college'

class CollegeUpdate(UpdateView):
    model = models.College
    template_name = 'create_college.html'
    fields = '__all__'
    success_url = '/college'

class StudentUpdate(UpdateView):
    model = models.Student
    template_name = 'create_student.html'
    fields = '__all__'
    success_url = '/college'

class CollegeDelete(DeleteView):
    model = models.College
    template_name = 'confirm.html'
    success_url = '/college'