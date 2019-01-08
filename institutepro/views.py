from django.shortcuts import render , redirect , get_object_or_404
from .models import RegistrationData , ApplicantData,FeedbackData, Page ,CompanyAddress
from .forms  import RegistrationForm ,LoginForm ,ApplicantForm,FeedbackForm , ForgotPasswordForm
from .password_hasher import *
from .third_party_security import smartlogin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.decorators import method_decorator
# from  Institute.settings import LOGIN_URL

import datetime

pagename = ''


def forgotPassword(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            if password1 == password2 :
                print('password matched')
                user = RegistrationData.objects.filter(username=username)
                user.update(password1 = hasher(password1))
                user.update(password2 = hasher(password2))
                print('password updated')
            return redirect('/')
    else:
        form = ForgotPasswordForm()
        return render(request, 'registration/forgot_password.html', {'form': form})

def registrationview(request):
    if request.method == 'POST' :
        rform  = RegistrationForm(request.POST)
        if rform.is_valid():
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            mobile = request.POST.get('mobile', '')
            # dob = RegistrationForm.cleaned_data.get('dob','')
            data = RegistrationData(
                username=username,
                password1=hasher(password1),
                password2=hasher(password2),
                email=email,
                mobile = mobile ,
                # dob = dob
            )
            User.objects.create_user(username=username,
                                     email=email,
                                     password=password1,

                                     )
            data.save()
            return  redirect('/')
        rformer(request)
    else :
        rform = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': rform})

def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print('in views')
        if form.is_valid():
            print('after calling is valid')
            username = request.POST.get('username' ,'')
            password = request.POST.get('password', '')

            un = RegistrationData.objects.filter(username=username)
            print(un)
            hash = RegistrationData.objects.values('password1')
            print(hash)
            print('username',un)
            user = auth.authenticate(username=username, password=password)
            print('auth in django',user)
            if  un:
                if checker(hash ,password) is  None:
                    print('password')
                    request.session['username'] = username
                    auth.login(request,user)
                    return redirect('/home/')
                else:
                    print('wrong password')
                    return redirect('/')
            else:
                print('wrong username')
                return redirect('/')
        print('after form is valid')
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})



@smartlogin
@login_required()
def home(request):
    pagename = 'home'
    catch = linkdispatcher(pagename)
    return render(request, catch[0] ,context=catch[1])



@smartlogin
@login_required()
def services(request):
    pagename = 'services'
    catch = linkdispatcher(pagename)
    return render(request, catch[0] ,context=catch[1])

@smartlogin
@login_required()
def contacts(request):
    pagename = 'contacts'
    submitted = False
    catch = linkdispatcher(pagename)
    if request.method == 'POST':
        aform = ApplicantForm(request.POST)
        if aform.is_valid():
            name = aform.cleaned_data.get('name','')
            email = aform.cleaned_data.get('email','')
            mobile = aform.cleaned_data.get('mobile','')
            courses = aform.cleaned_data.get('courses' , '')
            timings= aform.cleaned_data.get('timings','')
            startdate = aform.cleaned_data.get('startdate' ,'')

            data =  ApplicantData(

                name= name ,
                email= email,
                mobile= mobile ,
                courses= courses ,
                timings= timings ,
                startdate=startdate
            )
            data.save()
            return redirect('/contacts?submitted=True')

    else :
        aform = ApplicantForm()
        if 'submitted' in request.GET:
            submitted = True
        cont = catch[1]
        cont['aform'] = aform
        cont['address'] = CompanyAddress.objects.all()
        cont['submitted'] = submitted
    return render(request, catch[0], context=cont )



@smartlogin
@login_required()
def feedbacks(request):
    pagename = 'feedback'
    submitted = False
    catch = linkdispatcher(pagename)
    cont = catch[1]
    cont['fbs'] = FeedbackData.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('ratings')
            feedback = request.POST.get('feedback')
            if len(feedback) <=50 :
                data = FeedbackData(

                    name=name.title(),

                    rating=rating,

                    feedback=feedback ,

                    datetime = datetime.datetime.now()
                )

                data.save()
                return redirect('/feedback/?submitted=True')

    else:
        form = FeedbackForm()
        if 'submitted' in request.GET:
            submitted = True
        cont['form'] = form
        cont['submitted'] = submitted
        return render(request, catch[0], context=cont)
    return render(request, catch[0], context=cont)

@smartlogin
@login_required()
def gallery(request):
    pagename = 'gallery'
    catch = linkdispatcher(pagename)
    return render(request, catch[0], context=catch[1])


def logout(request):

    try :
        auth.logout(request)
        print('trying to delete session data' ,request.session.get('username'))
        del request.session['username']
        print('data deleted')
        print('auth logging out')


    except :
        print('unable to delete')

    if not request.session.get('username'):

        return  redirect('/')


def rformer(request):
    rform = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': rform})

def loger(request):
    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def linkdispatcher( pagename):

    paglink ='/'+ pagename
    pg = get_object_or_404(Page , permalink=paglink)
    context = {

        'title' : pg.title ,
        'last_updated' : pg.update_date ,
        'page_list':Page.objects.all()

    }

    return [ str(pagename)+'.html',  context]



