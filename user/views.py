from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.views import APIView


class Signup(APIView):

    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'user/signup.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('user:login')
        return render(request, 'user/signup.html', context)
