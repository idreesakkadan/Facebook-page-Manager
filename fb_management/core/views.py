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
  token = {"EAAoZAaCbXTB0BALgUswfgdYXJGEo6eN0W3dI4MQlGYvZACZBio2O9QZBLzKSZBCJKZBQQKREcSPtxnDVFh0JJigESnhkDM1DsJnL5NuL79lfZCtrvUS6nnJwCaWiazp1LwrKm4MjdxdZC7A7yOZCARliIZAe02eh9AcNuaQbm4D0FxjbWRd6aVyTqX2ZAtbHBVwzbZCBBtBYVzO2oj9zWL4SCAQx"}
  
  graph = facebook.GraphAPI(access_token=token)

  fields = ['name','location','phone']

  fields = ','.join(fields)


  profile = graph.get_object('me',fields=fields)
  name = profile['name']
  location = profile['location']
  phone = profile['phone']
  source = 'facebook'

  obj1 = Pages.objects.create(source=source,page_name=name,address=location,phone=phone,listed=0)


  token2 = {'EAAoZAaCbXTB0BAKBY43X1TjJyw2EW7G4teWVRqAXFZCMZCe1NaBZAd1X7YrC15HSq2mtvRINJ0lOLNE4mjZAcxy8vxJT01PbfCpUSLn5mt9GwrOhmtZAymYq8zGj2ZA2qauRi7sT926a5EPxhi3h2noK1TfKDH0wSEsdwqh3jW5Cti6aKswpW3jNlNS7ZCae7KXF1ZAy3iPltIxBaxqY6BrgD'}
  graph = facebook.GraphAPI(access_token=token2)

  fields = ['name','location','phone']

  fields = ','.join(fields)

  profile = graph.get_object('me',fields=fields)
  name = profile['name']
  location = profile['location']
  phone = profile['phone']
  source = 'facebook'

  obj2 = Pages.objects.create(source=source,page_name=name,address=location,phone=phone,listed=0)




  token3 = {'EAAoZAaCbXTB0BAOSARiWnycuXpz4xEwaOMtmenvpP7cdYZB5SEnARL451dGZCmKlTvvbSim2mH45iNtyRl7U23mVgqRHZAgNrTpz7NyLOJOdZA8lLEXIDT8ZBi0Xn3vOQ3MeKIGHi64EocUDNd378R2UKgo0TcANVqkjtvnxSAtgrpTxEoFRt4qR6GQW7MjbBo3cOs7HwP3cXknjKBMXEO'}
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



  

