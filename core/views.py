from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from math import ceil
from .models import *
from .decorators import admin_only, allowed_users, unauthenticated_user
from .forms import AddRatingForm

from math import sqrt
import numpy as np
import pandas as pd

@login_required(login_url='login')
def adminPage(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    context = {
        'students': students,
        'courses': courses
    }
    return render(request, 'core/dashboard.html', context)

@unauthenticated_user
def registerPage(request):

    if request.method == 'POST':    
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['first_name'] + f" " + request.POST['last_name']
            csee = request.POST['csee']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            # necta_student_csee = NectaBasicInfoAPI.objects.filter(csee=csee)
            # print(necta_student_csee)

            # if necta_student_csee == csee:
            #     messages.error(request, 'CSEE number does not match')
            if NectaAPI.objects.filter(csee=csee).exists():
                if password1 == password2:
                    if User.objects.filter(first_name=first_name, last_name= last_name).exists():
                        messages.error(request, 'User already exist')
                        return redirect('register')
                    elif User.objects.filter(email=email).exists():
                        messages.error(request, 'Password does not match')
                    else:
                        user = User.objects.create_user(
                            username = username,
                            first_name= first_name, 
                            last_name=last_name,
                            email=email,
                            password=password1
                        )
                        user.save()

                        group = Group.objects.get(name='student')
                        user.groups.add(group)

                        Student.objects.create(
                            user = user,
                            first_name = first_name,
                            last_name = last_name,
                            email = email,

                            csee = csee,
                        )
                        print('user creates successfully')


                    messages.success(request, 'Account was created for ' + first_name)
                    return redirect('login')

                else: 
                    messages.error(request, 'Password does not match')
                    return redirect('register')
            else:
                messages.error(request, 'CSEE number does not match')
                return redirect('register')
    context = {}
    return render(request, 'core/auth/register.html', context)

@unauthenticated_user
def loginPage(request):
    # If user is logged in he/she should never access the login page through URL
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        email = request.POST.get('email') # update - make all username entered be lowercase
        password = request.POST.get('password')
        username = User.objects.get(email=email.lower()).username
        # print(username)
        # print(username + " " + password)
        # check if the user exists, if dont output a flash message
        try:
            user = User.objects.get(email=email)
            print(user)
        except:
            messages.error(request, 'User does not exist') # use flash error message

        # Get user object and authenticate based on username and password
        user = authenticate(request, username=username, password=password)

        if user is not None: # check if there is user or no user
            login(request, user) # Login the user and add the session into the db and browser
            return redirect('studentPage')

        else:
            messages.error(request, 'Username or password does not exist') # use flash error message
            print(user)
    context = {}
    return render(request, 'core/auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('studentPage')

@login_required(login_url='login')
@admin_only
def dashboard(request):
    return render(request, 'core/dashboard.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def studentPage(request):
    courses = Course.objects.all()

    context = {
        'courses': courses
    }
    return render(request, 'core/starter.html', context)



def personalInfo(request):
    return render(request, 'core/personal_info.html')

def preferencePage(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'core/preference.html', context)


def application_status(request):
    return render(request, 'core/application_status.html')


# Collaborative Filtering Algorithm
def filterCourseByInterest():
     #filtering by genres
    allCourses=[]
    interestCourse= Course.objects.values('interest', 'id')
    interests= {item["interest"] for item in interestCourse}
    for interest in interests:
        course=Course.objects.filter(interest=interest)
        print(course)
        n = len(course)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allCourses.append([course, range(1, nSlides), nSlides])
    params={'allCourses':allCourses }
    return params


def generateRecommendation(request):
    course=Course.objects.all()
    rating=Rating.objects.all()
    x=[] 
    y=[]
    A=[]
    B=[]
    C=[]
    D=[]
    #Movie Data Frames
    for item in course:
        x=[item.id,item.name,item.interest] 
        y+=[x]
    course_df = pd.DataFrame(y,columns=['courseId','name','interest'])
    print("Course DataFrame")
    print(course_df)
    print(course_df.dtypes)
    #Rating Data Frames
    print(rating)
    for item in rating:
        A=[item.user.id,item.course,item.rating]
        B+=[A]
    rating_df=pd.DataFrame(B,columns=['userId','courseId','rating'])
    print("Rating data Frame")
    rating_df['userId']=rating_df['userId'].astype(str).astype(np.int64)
    rating_df['courseId']=rating_df['courseId'].astype(str).astype(np.int64)
    rating_df['rating']=rating_df['rating'].astype(str).astype(np.float)
    print(rating_df)
    print(rating_df.dtypes)
    if request.user.is_authenticated:
        userid=request.user.id
        #select related is join statement in django.It looks for foreign key and join the table
        userInput=Rating.objects.select_related('course').filter(user=userid)
        if userInput.count()== 0:
            recommenderQuery=None
            userInput=None
        else:
            for item in userInput:
                C=[item.course.name,item.rating]
                D+=[C]
            inputCourse=pd.DataFrame(D,columns=['name','rating'])
            print("Selected Courses by user")
            inputCourse['rating']=inputCourse['rating'].astype(str).astype(np.float)
            print(inputCourse.dtypes)

            #Filtering out the movies by title
            inputId = course_df[course_df['name'].isin(inputCourse['name'].tolist())]
            #Then merging it so we can get the movieId. It's implicitly merging it by title.
            inputCourse = pd.merge(inputId, inputCourse)
            # #Dropping information we won't use from the input dataframe
            # inputMovies = inputMovies.drop('year', 1)
            #Final input dataframe
            #If a movie you added in above isn't here, then it might not be in the original 
            #dataframe or it might spelled differently, please check capitalisation.
            print(inputCourse)

            #Filtering out users that have watched movies that the input has watched and storing it
            userSubset = rating_df[rating_df['courseId'].isin(inputCourse['courseId'].tolist())]
            print(userSubset.head())

            #Groupby creates several sub dataframes where they all have the same value in the column specified as the parameter
            userSubsetGroup = userSubset.groupby(['userId'])
            
            #print(userSubsetGroup.get_group(7))

            #Sorting it so users with movie most in common with the input will have priority
            userSubsetGroup = sorted(userSubsetGroup,  key=lambda x: len(x[1]), reverse=True)

            print(userSubsetGroup[0:])


            userSubsetGroup = userSubsetGroup[0:]


            #Store the Pearson Correlation in a dictionary, where the key is the user Id and the value is the coefficient
            pearsonCorrelationDict = {}

        #For every user group in our subset
            for name, group in userSubsetGroup:
            #Let's start by sorting the input and current user group so the values aren't mixed up later on
                group = group.sort_values(by='courseId')
                inputCourse = inputCourse.sort_values(by='courseId')
                #Get the N for the formula
                nRatings = len(group)
                #Get the review scores for the movies that they both have in common
                temp_df = inputCourse[inputCourse['courseId'].isin(group['courseId'].tolist())]
                #And then store them in a temporary buffer variable in a list format to facilitate future calculations
                tempRatingList = temp_df['rating'].tolist()
                #Let's also put the current user group reviews in a list format
                tempGroupList = group['rating'].tolist()
                #Now let's calculate the pearson correlation between two users, so called, x and y
                Sxx = sum([i**2 for i in tempRatingList]) - pow(sum(tempRatingList),2)/float(nRatings)
                Syy = sum([i**2 for i in tempGroupList]) - pow(sum(tempGroupList),2)/float(nRatings)
                Sxy = sum( i*j for i, j in zip(tempRatingList, tempGroupList)) - sum(tempRatingList)*sum(tempGroupList)/float(nRatings)
                
                #If the denominator is different than zero, then divide, else, 0 correlation.
                if Sxx != 0 and Syy != 0:
                    pearsonCorrelationDict[name] = Sxy/sqrt(Sxx*Syy)
                else:
                    pearsonCorrelationDict[name] = 0

            print(pearsonCorrelationDict.items())

            pearsonDF = pd.DataFrame.from_dict(pearsonCorrelationDict, orient='index')
            pearsonDF.columns = ['similarityIndex']
            pearsonDF['userId'] = pearsonDF.index
            pearsonDF.index = range(len(pearsonDF))
            print(pearsonDF.head())

            topUsers=pearsonDF.sort_values(by='similarityIndex', ascending=False)[0:]
            print(topUsers.head())

            topUsersRating=topUsers.merge(rating_df, left_on='userId', right_on='userId', how='inner')
            topUsersRating.head()

                #Multiplies the similarity by the user's ratings
            topUsersRating['weightedRating'] = topUsersRating['similarityIndex']*topUsersRating['rating']
            topUsersRating.head()


            #Applies a sum to the topUsers after grouping it up by userId
            tempTopUsersRating = topUsersRating.groupby('courseId').sum()[['similarityIndex','weightedRating']]
            tempTopUsersRating.columns = ['sum_similarityIndex','sum_weightedRating']
            tempTopUsersRating.head()

            #Creates an empty dataframe
            recommendation_df = pd.DataFrame()
            #Now we take the weighted average
            recommendation_df['weighted average recommendation score'] = tempTopUsersRating['sum_weightedRating']/tempTopUsersRating['sum_similarityIndex']
            recommendation_df['courseId'] = tempTopUsersRating.index
            recommendation_df.head()

            recommendation_df = recommendation_df.sort_values(by='weighted average recommendation score', ascending=False)
            recommender=course_df.loc[course_df['courseId'].isin(recommendation_df.head(5)['courseId'].tolist())]
            print(recommender)
            return recommender.to_dict('records')

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def courseRating(request):
    if request.user.is_authenticated: 
        params=filterCourseByInterest()
        params['user']=request.user
        if request.method=='POST':
            userid=request.POST.get('userid')
            courseid=request.POST.get('courseid')
            course=Course.objects.all()
            u=User.objects.get(pk=userid)
            m=Course.objects.get(pk=courseid)
            rfm=AddRatingForm(request.POST)
            params['rform']=rfm
            if rfm.is_valid():
                rat=rfm.cleaned_data['rating']
                count=Rating.objects.filter(user=u,course=m).count()
                if(count>0):
                    messages.warning(request,'You have already submitted your review!!')
                    return render(request,'core/course_rating.html',params)
                action=Rating(user=u,course=m,rating=rat)
                action.save()
                messages.success(request,'You have submitted'+' '+rat+' '+"star")
            return render(request,'core/course_rating.html',params)
        else:
            #print(request.user.id)
            rfm=AddRatingForm()
            params['rform']=rfm
            course=Course.objects.all()
            return render(request,'core/course_rating.html',params)
    else:
        return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def courseRecommendation(request):
    params=filterCourseByInterest()
    params['recommended']=generateRecommendation(request)
    return render(request,'core/course_recommend.html',params)

