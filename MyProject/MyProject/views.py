from django.http import HttpResponse
from django.shortcuts import render
import joblib
def home(request):
    return render(request,'home.html')


def result(request):
    regressor=joblib.load('finalized_model.sav')
    lis=[]
    lis.append(request.GET['years'])
    print('lis',lis[0])
    qwe=float(lis[0])
    ans=regressor.predict([[qwe]])
    return render(request,'result.html',{'ans':ans})


