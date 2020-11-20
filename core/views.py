from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .models import *
from .forms import*
# Create your views here.
def index(request):
    return render(request,'index.html')

def get_user(user):
    qs=Profile.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def CreateUser(request):
	context={}
	if  request.POST:
		form1=UserForm(request.POST)
		form2=ProfileForm(request.POST)
		if form1.is_valid() and form2.is_valid():
			user=form1.save(commit=False)
			user.save()
			f2=form2.save(commit=False)
			f2.user=user
			f2.save()
			login(request,user)
			return redirect('merchanthome')
		else:
			context['form1']=form1
			context['form2']=form2
	else:
		form1=UserForm()
		form2=ProfileForm()
		context['form1']=form1
		context['form2']=form2
	return render(request,'register.html',context)

def MerchantHome(request):
    merchant=Profile.objects.get(user=request.user)
    items=Item.objects.filter(merchant=merchant)
    context={"items":items}
    return render(request,'merchanthome.html',context)

def AddItem(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context={}
    title="Add"
    if request.POST:
        merchant=get_user(user=request.user)
        form=ItemForm(request.POST, request.FILES or None)
        if form.is_valid():
            item=form.save(commit=False)
            item.merchant=merchant
            item.save()
            return redirect('merchanthome')
        else:
            context={'form':form}
    else:
        form=ItemForm()
    context={'form':form,'title':title}
    return render(request,'additem.html',context)

def EditItem(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')
    context={}
    title="Edit"
    item=Item.objects.get(pk=pk)
    form=ItemForm(request.POST or None, request.FILES or None,instance=item)
    if request.POST:
        merchant=get_user(user=request.user)
        if form.is_valid():
            item=form.save(commit=False)
            item.merchant=merchant
            item.save()
            return redirect('merchanthome')
    context={'form':form,'title':title}
    return render(request,'additem.html',context)

def DeleteItem(request,pk):
    item=Item.objects.get(pk=pk)
    item.delete()
    return redirect('merchanthome')
