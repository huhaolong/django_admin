from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *
# Create your views here.
@login_required
def app01(request):
    obj = Aliyun_list.objects.all().values()
    # if request.method == "get":
    #     title_name = request.GET.get("change_content")
    #     print(title_name)
    return render(request,'app01.html',{"obj":obj})






@login_required
def myblog(request):
    obj = Article.objects.all().values()
    # if request.method == "get":
    #     title_name = request.GET.get("change_content")
    #     print(title_name)
    return render(request,'myblog.html',{"obj":obj})