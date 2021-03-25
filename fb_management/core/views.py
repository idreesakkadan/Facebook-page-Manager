from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Pages
import json
import facebook

# Create your views here.
def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  return render(request, 'base.html')

@login_required
def dashbord(request,):
  return render(request, 'dashboard.html')

@login_required
def reviews(request,):
  return render(request, 'reviews.html')

@login_required
def settings(request,):
  return render(request, 'settings.html')

@login_required
def visitors(request,):
  return render(request, 'visitors.html')

@login_required
def website(request,):
  return render(request, 'website.html')

@login_required
def appoinments(request,):
  return render(request, 'appoinments.html')




@login_required
def get_data(request):
  token = {"EAAoZAaCbXTB0BADr65cuxuLZCq3tXR6skFwphq5ZAZA0dZBd6ZC1XtsSfuAj1Iy2xrDoCubZCo4LmdkDbtHZBAMjC4fjbr9C891ZAXLIHaSa1Y3jjqLJ1GDvRSK2GqGcTolwEfE37cgN916j5BwS0WNi1sjLKLjpEdjAe28xshVZBdt879ScBFUdzX2ZCbJm8qtaJgNyLALsN9NTqezpeXzZBwSq"}
  
  graph = facebook.GraphAPI(access_token=token)

  fields = ['name','location','phone']

  fields = ','.join(fields)


  profile = graph.get_object('me',fields=fields)
  name = profile['name']
  location = profile['location']
  phone = profile['phone']
  source = 'facebook'

  obj1 = Pages.objects.create(source=source,page_name=name,address=location,phone=phone,listed=0)


  token2 = {'EAAoZAaCbXTB0BAJ3ZCZCKVArXDUv6PESbZCP2qpGITZCdf7Gd01rIUddD5M7nB2mp35X3ZC0KmMOZCVv7jgY9LsAZCy70XtQekHAsx2trtdssc6AAvZAPCxMHZAqjk3NLYKfbWHvrekeRxU8iusjXsxfEuo9FN5jiAXdskMnj0tHe5XwRCUWTdZAZA3U848GW2IZAsMdZC00JLM9W9v8lqLetKZABjF'}
  graph = facebook.GraphAPI(access_token=token2)

  fields = ['name','location','phone']

  fields = ','.join(fields)

  profile = graph.get_object('me',fields=fields)
  name = profile['name']
  location = profile['location']
  phone = profile['phone']
  source = 'facebook'

  obj2 = Pages.objects.create(source=source,page_name=name,address=location,phone=phone,listed=0)




  token3 = {'EAAoZAaCbXTB0BAIwjnZAyPH2XhyBME6IlrpIMyqpjKXvKMYU10pnboqpvlqqzWNiZCIFhAKoZBHZAemz6XfNvVi8ZBuGiDBkVFHhx8LjUH04KxfDpx6P55ZCjZAZAkyTMkAqkTKDlgpHvZAhR17kZAmZBS7O43kSPqqHA6uWybDfUy9eTPu70qDR40d4Tq4iySYrEpnddMZAZBeDmFA42bYj9QLKzp'}
  graph = facebook.GraphAPI(access_token=token3)

  fields = ['name','location','phone']
  fields = ','.join(fields)

  profile = graph.get_object('me',fields=fields)
  name = profile['name']
  location = profile['location']
  phone = profile['phone']
  source = 'facebook'

  obj3 = Pages.objects.create(source=source,page_name=name,address=location,phone=phone,listed=0)

  return redirect(listings)

  # print(profile['id'])
  # print(name)
  # print(location)
  # print(phone)

  # print(profile)
  # print(json.dumps(profile,indent=4))

  # return render(request,'list.html',{'name':name,'location':location,'phone':phone})

@login_required
def listings(request):
  obj2 = Pages.objects.all()
  return render(request,'list.html',{'data':obj2})


@login_required
def update(request,id):
  update_page=Pages.objects.get(pk=id)
  print(update_page)

  if request.method == 'GET':
    return render(request,'update.html',{'data':update_page})
  else:
    update_page.page_name = request.POST.get('name')
    update_page.address = request.POST.get('address')
    update_page.phone = request.POST.get('phone')
    update_page.listed = 1
    update_page.save()
    return redirect(listings)



  

