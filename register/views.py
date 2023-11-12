from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User, Group


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            form.save()
            # get the new user info and set the group for this user to LibraryMember
            user = User.objects.get(username=uname)
            cust_group = Group.objects.get(name='Customer')
            user.groups.add(cust_group)
            user.save()
            return redirect('login')

        return redirect("index")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


from django.shortcuts import render

# Create your views here.
