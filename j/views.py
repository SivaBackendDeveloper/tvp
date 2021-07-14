from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect


from j.forms import MemberForm, ActivityForm
from j.models import Member, Activity


def base_view(request):
   return render(request, 'j/base.html')

def home_view(request):
   return render(request, 'j/home.html')

def show_view(request):
   members=Member.objects.all()
   return render(request, 'j/index.html',{'members':members})

def activity_view(request):
   activity=Activity.objects.all()
   return render(request, 'j/activity.html',{'activity':activity})

@login_required()
def insert_view(request):
   form=MemberForm()
   if request.method == 'POST':
    form = MemberForm(request.POST)
    if form.is_valid():
       form.save()
    return redirect('/')
   return render(request, 'j/insert.html', {'form': form})

@login_required()
def activityinsert_view(request):
    if request.method == "POST":
        form = ActivityForm(data=request.POST, files=request.FILES)
        if form.is_valid():
          form.save()
          obj = form.instance
          return render(request, "j/addactivity.html", {"form": form ,"obj": obj})
    else:
       form = ActivityForm()

    return render(request, "j/addactivity.html", {"form": form })

@login_required()
def delete_view(request, id):
  member = Member.objects.get(id=id)
  member.delete()
  return redirect('/')


@login_required()
def activitydelete_view(request, id):
  activity = Activity.objects.get(id=id)
  activity.delete()
  return redirect('/')


@login_required()
def update_view(request,id):
   member = Member.objects.get(id=id)
   if request.method == 'POST':
     form = MemberForm(request.POST, instance=member)
     if form.is_valid():
        form.save()
     return redirect('/')
   return render(request, 'j/update.html', {'member': member})

@login_required()
def activityupdate_view(request, id):
   activity = Activity.objects.get(id=id)
   if request.method == 'POST':
     form = ActivityForm(request.POST, instance=activity)
     if form.is_valid():
        form.save()
     return redirect('/')
   return render(request, 'j/upactivity.html', {'activity': activity})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})


def logout_view(request):
    auth.logout(request)
    return redirect('/')



