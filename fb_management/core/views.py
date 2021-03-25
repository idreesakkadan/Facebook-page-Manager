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
  token = {"EAAoZAaCbXTB0BAPhcQaolni8qngfXKBLOxjzWmJ1xEN8ud4wixPbMCoWA4oVlkpr4O38bpLVVYrZApkGyW68NhFvOrygTbREOuApqKVIIfuAvMEO4cia8y8hZCaHVqUhCQ2I2IEcVUmZAYjs59nhgYZA9jya4ei0WGxswovZCQMaTPV4tV3ZB0CJ8fK28QJplNxszTaPGo3ZAEtHGtDahjQs"}
  
  graph = facebook.GraphAPI(access_token=token)

  fields = ['name','location','phone']

  fields = ','.join(fields)


  profile = graph.get_object('me',fields=fields)
  name = profile['name']
  location = profile['location']
  phone = profile['phone']
  source = 'facebook'

  obj1 = Pages.objects.create(source=source,page_name=name,address=location,phone=phone,listed=0)


  token2 = {'EAAoZAaCbXTB0BAE4ONM4dWL6vUFX9fmR3LIDHUgysasenFmuWKB2ks95wWZB4v7fBjfXaIyAves4mR6ZB8UI6Cqodqgfmtvmv8ATBxbGiTeUM9gsIEpbdgInO3dkxAd9qJTZCoQPpXwp5Y6NHxv1xteWCWz1WJmXxmOTglb4OIxIIIflrkDOMY5XvgZCAr8FnXL8ZAYkwQDDLsZAz02OVFE'}
  graph = facebook.GraphAPI(access_token=token2)

  fields = ['name','location','phone']

  fields = ','.join(fields)

  profile = graph.get_object('me',fields=fields)
  name = profile['name']
  location = profile['location']
  phone = profile['phone']
  source = 'facebook'

  obj2 = Pages.objects.create(source=source,page_name=name,address=location,phone=phone,listed=0)





  token3 = {'EAAoZAaCbXTB0BABnZBP3dBtmfgsgpkdmZAq6YhKVGmAvWG1Ik4GYv6PP45HW09iZCq4GnpwsphIqfT4G1JXFh6g9epUcM9Qxnw19wcz1npA22t8dnSvOGraDDr39SJuuru7KCOq80ZAbDNHLZBeR0vWC1U4qkULHaYTAQqFrofozoqVN48KON7btFtf3ZBAUrhhkgnGIHsPfGErap8YqwZAW'}
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



  

