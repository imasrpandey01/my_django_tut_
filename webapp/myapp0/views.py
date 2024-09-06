import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

from myapp0.models import Employee


def hello_world(request):
   return HttpResponse ('<h1>hello_world</h1> ')
    
def date_time(request):
   dt=datetime.datetime.now()
   s='<h1>The current date and time is' + str(dt) +'</h1>'
   return HttpResponse(s)  

def greets(request):
   return HttpResponse('<h1>Hello_Welcome To Django</h1>')


def morning_wish(request):
   return HttpResponse('<h1>GoodMorning_Welcome To Django</h1>')

def evening_wish(request):
   return HttpResponse('<h1>GoodEvening_Welcome To Django</h1>')


def template_view(request):
   dt=datetime.datetime.now()
   my_dict={'date':dt}
   return HttpResponse(render(request,'myapp0/results.html',context=my_dict))
#here in the above line context is the third parameter of render function which is used to inject dynamic 
#values into html file and return the response containg that dynamic data injected through context

#Now the code we're going to write is for displaying the content in database instead of the admin interface
#and that too in json format
def view_data_db(request):
    employees = Employee.objects.all()
    employee_data = list(employees.values())  # Convert queryset to list of dictionaries
    return JsonResponse(employee_data, safe=False)


#In String format 
#It looks like you’re trying to return data from the database as an HTTP response. 
# However, HttpResponse expects a string, not a list of objects. 
# In Django, when you want to return data from the database as part of an HTTP response, 
# you typically convert the data to a format that can be easily rendered in the response.
#FOR RETURNING DATA AS PLAIN TEXT IN RESPONSE 
from django.http import HttpResponse
from .models import Employee

from django.http import HttpResponse
from .models import Employee

def view_data_db_text(request):
    employees = Employee.objects.all()
    employee_list = [f"Name: {e.e_name}, Emp_No: {e.e_no}" for e in employees]  # Adjust fields accordingly
    response_content = "\n".join(employee_list)
    return HttpResponse(response_content, content_type='text/plain')
