from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request, 'generator/home.html')


def about(request):
    # return HttpResponse('TEST')
    return render(request,'generator/about.html')

def password(request):
    characters = list('qwertyuioplkjhgfdaszxcvbnm')
    generate_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@$*#%&()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    # import pdb;pdb.set_trace()
    for i in range(length):
        generate_password += random.choice(characters)
    
    # print("the password is {}".format(generate_password))

    data = {'password':generate_password}

    return render(request,'generator/password.html',data)
