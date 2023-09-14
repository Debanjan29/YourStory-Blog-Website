from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from . models import Contact
from . models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# from django.core.validators import RegexValidator
# import re

def edit(title):
  n=len(title)
  title2=title.replace(" ","+")
  print(n)
  return title2

def home(request):
    return render(request,'blog/home.html')

def about(request):
      return render(request,'blog/about.html')
    #return HttpResponse("Hello, MY name is CRISTIANOOOOOOO RONALDOOOOOOO")

def contact(request):
     if request.method=="POST":
          name=request.POST["name"]
          email=request.POST["email"]
          phone=request.POST["phone"]
          msg=request.POST["content"]

          if (len(name)<2 or len(email)<8 or len(phone)<10 or len(msg)<5):
               messages.error(request,"Fill the form correctly:")
          else:
            print(name)
            print(email)
            print(phone)
            print(msg)
            global params
            params=[]
          #   msg=edit(msg)
            messages.success(request,"Congrats! We got your Message")
            contact_variable=Contact(Name=name,Phone=phone,Email=email,Content=msg) # contact_variable is a variable which is used to store the result of Object Calling 'Contact'
            contact_variable.save()

          # userprint=Contact.objects.filter(Name=name).first()
          # params={'userprint':userprint}
          
     return render(request,'blog/contact.html')

def blogHome(request):
     allPosts=Post.objects.all().order_by('time') #allPosts gets all the objects from Database
     #print(allPosts)
     context={'allPosts':allPosts} # context is a way of making a dictionary ('allPosts') of allPost . Now, we can use 'allPosts' in .html file to fetch dynamically.
     return render(request,'blog/home.html',context)
     

def blog(request):
     return render(request,'blog/blog.html')

def blogPost(request,slug_incoming):
     post=Post.objects.filter(slug=slug_incoming).first()
     context={'post':post}
     print(post)
     return render(request,'blog/blog.html',context)

def search(request):
     global flag
     flag=False
     query=request.GET['query']
     if len(query)>20 or query==" " or query=="" or query=="  ":
        result=Post.objects.none()
        flag=True
     else:
          query=request.GET['query']

          resultTitle=Post.objects.filter(Title__icontains=query)
          # Django icontains 
          #Post is the name of the Database #( fieldname__icontains='value')

          allPostsAuthor= Post.objects.filter(Author__icontains=query)
          allPostsContent =Post.objects.filter(Content__icontains=query)

          result=resultTitle.union(allPostsContent, allPostsAuthor) #Merging 3 query set

          if result.count()==0:
               messages.error(request,"No Results Found.Please refine your search")

     params={'results':result , 'query':query ,'flags':flag}
     # The icontains lookup is used to get records that contains a specified value. The icontains lookup is case insensitive. For a case sensitive search, use the contains lookup.


     return render(request,'blog/search.html',params)
     #return HttpResponse("Search Page")


def register(request):
    if request.method== "POST":
        user=request.POST["Username"]
        user=user.lower()
        Fname=request.POST["FName"]
        Lname=request.POST["LName"]
        email=request.POST["Email"]
        passw1=request.POST["Pass1"]
        passw2=request.POST["Pass2"]
        print(user,Fname,Lname,email,passw1,passw2)

        if len(user)<3 or len(Fname)<3 or len(Lname)<2 or len(email)<5:
            messages.error(request,"UserName or First Name or Last Name or email is not acceptable. Enter Proper Details ")
            return redirect('Home')

        if(passw1==passw2):
            
            if (User.objects.filter(username=user)):
                messages.error(request,"Username already exists.Choose Something different")
                return redirect('Home',)
            if (User.objects.filter(email=email)):
                messages.error(request,"Email already exists.Choose Something different")
                return redirect('Home')
            else:
                user=User.objects.create_user(username=user,email=email,password=passw1)
                user.first_name=Fname
                user.last_name=Lname
                user.save()

                userprint=User.objects.filter(username=user).first()
                params={'userprint':userprint}
                messages.success(request,"Account created successfully")
                messages.info(request,"Username is in smallcase.Eg: 'Deba1234' will be read as 'deba1234' ")
                return redirect('login',params)
                #return render(request,'blog/login.html',params)
                #return redirect('contact')
    else:
     return redirect('Home')
    

# Your view has the same name as the auth login function, so it is hiding it. Change the view name, or import the function under a different name eg from django.contrib.auth import login as auth_login.

def loginn(request):
    global wrongflag
    wrongflag=False
    if request.method=="POST":
        username=request.POST["username"]
        Pass=request.POST["pass"]

        user=authenticate(username=username,password=Pass)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect('/')
        else:
            wrongflag=True
            messages.error(request,"Wrong Credentials")
            
        params23={'wrongflag':wrongflag}
        return render(request,"blog/login.html",params23)
    else:
        return render(request,'blog/login.html')


def logoutt(request):
    logout(request)
    messages.success(request,"Logged out Succesfully")
    return redirect('/')

def post(request):
    if request.method=="POST":
        user=request.user
        email=user.email
        user1=user.first_name
        u=user.last_name
        user=user1+" " + u
        title=request.POST["title11"]
        content=request.POST["content11"]
        slug=edit(title)
        save=Post(Author=user,Email=email,Title=title,slug=slug,Content=content)
        save.save()
        # print(title)
        # print(content)
        # print(user)
        # print(email)
        # print(slug)
        messages.success(request,"Your Blog has been Posted!")
    return render(request,"blog/postb.html")