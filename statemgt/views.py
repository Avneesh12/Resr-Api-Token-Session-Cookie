from django.shortcuts import render

# Create your views here.

def setMycookie(request):
    if request.method == 'POST':
        name = request.POST.get('cname')
        resp = render(request,'statemgt/setcookie.html')
        resp.set_cookie(key='name',value=name)
        return resp
    return render(request,'statemgt/setcookie.html')

def getMycookie(request):
    if request.method == 'POST':
        name = request.COOKIES.get('name','NA')
        if name == 'NA':
            d = {'name':'NoCookie'}
            return render(request,'statemgt/getcookie.html',context=d)
        else:
            d = {'name':name}
            return render(request,'statemgt/getcookie.html',context=d)
    return render(request,'statemgt/getcookie.html')

def get_visit(request):
    count = request.session.get('count','NA')
    if count == 'NA':
        count = 1
    else:
        count = count + 1
    request.session['count'] = count
    d = {'count':count}
    return render(request,'statemgt/visitcount.html',context=d)


def setsession(request):
    request.session['name'] = 'Avneesh'
    return render(request,'statemgt/setsession.html')

def getsession(request):
    name = request.session['name']
    return render(request,'statemgt/getsession.html',{'name':name})