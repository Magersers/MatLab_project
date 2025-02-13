from django.shortcuts import render
import numpy as np

def index(site):
    arr1 = np.array([1,2,3,4])
    mal = {'name':arr1}
    return render(site,'index.html',context=mal)
# Create your views here.
