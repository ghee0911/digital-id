from django.shortcuts import render
from identitys.models import Selection

def index(request):
    selection_list = Selection.objects.all().order_by('id')
    return render(request, 'identitys/index.html', {'selection_list': selection_list})


# def inputdata(request):
# def result(request):
# def searching(request):
