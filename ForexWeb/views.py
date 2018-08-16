from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def main(request):
    return render(request,'main.html',{})