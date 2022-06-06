from django.shortcuts import render
# from django.http import HttpResponse
# from appTwo.models import User

from appTwo.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'apptwo/index.html')


def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit =True)
            return index(request)

        else:
            print("Error Form Invalid")

    return render(request, 'apptwo/user.html', {'form':form})

# def users(request):
#     user_list = User.objects.order_by('first_name')
#     user_info= {'user_list': user_list }
#     return render(request,'apptwo/user.html',context = user_info )
