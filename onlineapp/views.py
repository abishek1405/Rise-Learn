from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib  import messages
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from .models import  score,CustomUser,Grant,Loan,incentive,job,study_meterial,video_meterial,category,subject_name,question_paper,JobApplication
from .models import LoanRequest


def test_success(request):
    return render(request,'test_success.html')



from django.contrib.auth.hashers import make_password
def accpect_mentor(request,id):
    data = CustomUser.objects.get(id = id) #3
    if request.method == 'POST':
        data.verifi = True 
        data.save()
        return redirect('/add_mendor')
    return render(request,'accpect_mentor.html',{'data':data})




def accept_mentor(request,id):
    data = CustomUser.objects.get(id = id) #3
    data.verifi = True 
    data.save()
    messages.success(request,'Mentor Accepted')
    return redirect('/add_mendor')
def reject_mentor(request,id):
    data = CustomUser.objects.get(id = id) #3
    data.verifi = False 
    data.save()
    messages.success(request,'Mentor Rejected')
    return redirect('/add_mendor')


def job_apllication(request):
    data = JobApplication.objects.all()
    return render(request,'job_apllication.html',{'data':data})





def job_view(request):
    data = job.objects.all()
    return render(request,'job.html',{'data':data})



def job_apply(request,id):
    data_job = job.objects.get(id = id)
    data = CustomUser.objects.get(username = request.user)
    if request.method == 'POST':
        # Collect the form data
        name = request.POST.get('name')
        age = request.POST.get('age')
        skills = request.POST.get('skills')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        resume = request.FILES.get('resume')

        # Create a new JobApplication instance and save to the database
        if JobApplication.objects.filter(user = request.user, job = data_job).exists():
            messages.success(request, 'Your application already Submitted!')
            return redirect('/job')
        job_application = JobApplication(
            
            name=name,
            age=age,
            skills=skills,
            email=email,
            phone=phone,
            resume=resume,
            user = data,
            job = data_job
        )
        job_application.save()  # Save the application in the database

        # Show a success message
        messages.success(request, 'Your application has been submitted successfully!')

        # Redirect to the job list or another page after successful submission
        return redirect('/job')
    return render(request,'job_apply.html')




def loan_request_accept(request,id):
    data = LoanRequest.objects.get(id = id)
    data.status = 'APPROVED'
    data.save()
    return redirect('/loan_request')

def loan_request_reject(request,id):
    data = LoanRequest.objects.get(id = id)
    data.status = 'REJECTED'
    data.save()
    return redirect('/loan_request')



def loan_request(request):
    data = LoanRequest.objects.filter(status = 'PENDING')
    return render(request,'loan_request.html',{'data':data})




def admin_view_requests(request):
    # Fetch all loan requests
    loan_requests = LoanRequest.objects.all()

    if request.method == 'POST':
        loan_id = request.POST.get('loan_id')
        action = request.POST.get('action')

        loan_request = get_object_or_404(LoanRequest, id=loan_id)

        if action == 'approve':
            loan_request.status = 'APPROVED'
            messages.success(request, 'Loan request has been approved.')
        elif action == 'reject':
            loan_request.status = 'REJECTED'
            messages.success(request, 'Loan request has been rejected.')
        
        loan_request.save()

        return redirect('/admin_view_requests')

    return render(request, 'admin_view_requests.html', {'loan_requests': loan_requests})


@login_required
def loat_request(request):
    data = LoanRequest.objects.filter(user = request.user)
    if request.method == 'POST':
        description_loan = request.POST.get('description_loan')
        
        if description_loan:
            # Save the loan request
            loat_request = LoanRequest.objects.create(
                user=request.user,
                description_loan=description_loan
            )
            
            return redirect('/loan_success')
        else:
            messages.error(request, 'Please provide a description for your loan request.')

    return render(request, 'loat_request.html',{'data':data})

def loan_success(request):
    return render(request,'loan_success.html')


def Approved_Student(request):
    data = CustomUser.objects.filter(student_guid = request.user.id)
    return render(request,'Approved_Student.html',{'data':data})


def my_account(request):
    username = request.user
    data = CustomUser.objects.get(username=username)
    print(data.user_type)
    if data.user_type == 1:
        return render(request,'my_account.html',{'data': data})
    elif data.user_type == 2:
        return render(request,'fac_account.html',{'data': data})
    else:
        return render(request,'admin_account.html',{'data': data})



def acc(request,id):
    data = CustomUser.objects.get(id = id)
    if data.user_type == 1:
        if request.method == "POST":
            data.email = request.POST.get('email') 
            data.contact = request.POST.get('number')
            data.age = request.POST.get('age')
            data.gender = request.POST.get('gender')
            data.class_name = request.POST.get('c_name')
            data.save()
            return redirect('/acc/'+id+'/')
        return render(request,'acc_edit.html',{'data':data})
    elif data.user_type == 2:
        if request.method == "POST":
            data.email = request.POST.get('email')
            data.contact = request.POST.get('number')
            data.qualification = request.POST.get('qly')
            data.class_name= request.POST.get('cls')
            data.fee = request.POST.get('fee')
            data.save()
            return redirect('/acc/'+id+'/')
        return render(request,'faculty_acc_edit.html',{'data': data})   
        
 


def choose_signup(request):
    return render(request,'common_signup.html')

def view_incentive(request):
    data = incentive.objects.all()
    return render(request,'view_incentive.html',{'data':data})

def view_load(request):
    data = Loan.objects.all()
    return render(request,'view_loan.html',{'data':data})

def view_grants(request):
    data = Grant.objects.all()
    return render(request,'view_grants.html',{'data':data})




def stu_more_information(request):
    return render(request,'stu_more_information.html')



def test(request, id):
    data = CustomUser.objects.get(username=request.user)

    sub_data = subject_name.objects.get(sub=id,user = request.user.student_guid)
    sub_values = question_paper.objects.filter(user=data.student_guid, test_id=sub_data.id)
    
    if request.method == 'POST':
        scoree = 0  
        ques = 0     
        
        for key, value in request.POST.items():
            if key.startswith('answer_'):
                if value == sub_values[ques].correct_answer:
                    scoree+=1                    
                ques+=1
        wrong = ques-scoree 
        try:
            score_data = score.objects.get(user = request.user,test_id = sub_data.sub)
            score_data.test_id = sub_data.sub             
            score_data.student_score = scoree
            score_data.worng_ans = wrong
            score_data.tot = ques
            score_data.save()            
        except:
            score.objects.create(user = request.user,tot = ques,worng_ans = wrong,test_id = sub_data.sub,student_score = scoree)
        return redirect('/test_success')  # Redirect to a success page or another view

    return render(request, 'test.html', {'data': sub_values})





def choose_test(request):
    data = CustomUser.objects.get(username = request.user)
    sub_values = subject_name.objects.filter(user=data.student_guid).values('sub').distinct()
    score_data = score.objects.filter(user = request.user)
    return render(request,'choose_test.html',{'data':sub_values})













def progress(request):
    score_data = score.objects.filter(user = request.user)
    sscore = 0
    tot = 0
    for x in score_data:
        sscore += int(x.student_score)
        tot += int(x.tot)

    

    return render(request,'progress.html',{'score_data':score_data,'sscore':sscore,'tot':tot})













def faculty_progress(request):
    stu_data = CustomUser.objects.filter(student_guid=request.user.id)
    score_data = []
    for student in stu_data:
        scores = score.objects.filter(user=student.id)
        if scores.exists():  
            score_data.extend(scores)  
    return render(request, 'faculty_progress.html', {'score_data': score_data})


def add_questions(request,id):
    test_ids = question_paper.objects.filter(user=request.user, test_id=int(id)).values('test_id')
    data = question_paper.objects.filter(test_id__in=[item['test_id'] for item in test_ids])
    if request.method == 'POST':
        question = request.POST.get('question')
        obtionA = request.POST.get('obtionA')
        obtionB = request.POST.get('obtionB')
        obtionC = request.POST.get('obtionC')
        obtionD = request.POST.get('obtionD') 
        correct_answer = request.POST.get('correct_answer')
        question_paper.objects.create(user = request.user,test_id = int(id),question = question,obtionA = obtionA,obtionB = obtionB,obtionC = obtionC,obtionD = obtionD,correct_answer = correct_answer)
    return render(request,'add_question.html',{'data':data})


def add_test(request):
    data = subject_name.objects.filter(user = request.user)
    if request.method == 'POST':
        categoryy = request.POST.get('sub')
        subject_name.objects.create(user = request.user,sub=categoryy)
        return redirect('/add_test')
    return render(request,'add_test.html',{'data':data})

from django.db.models import F

def cat_books(request):
    data = CustomUser.objects.get(username=request.user)
    distinct_categories = study_meterial.objects.filter(user=data.student_guid).values('category').distinct()
    return render(request, 'cat_books.html', {'distinct_categories': distinct_categories})

def book(request,id):
    data = CustomUser.objects.get(username=request.user)
    meterial = study_meterial.objects.filter(user = data.student_guid, category = id)
    return render(request, 'books.html', {'meterial': meterial})


def  cat_video(request):
    # Fetch the user data based on the logged-in user
    user = CustomUser.objects.get(username=request.user.username)
    
    # Fetch distinct categories for the user
    distinct_categories = video_meterial.objects.filter(user=user.student_guid).values('category').distinct()
    
    # Create a dictionary to hold subjects for each category
    category_subjects = {}
    
    # Iterate through each distinct category and get subjects
    for category in distinct_categories:
        category_id = category['category']
        subjects = video_meterial.objects.filter(user=user.student_guid, category=category_id).values_list('subject', flat=True).distinct()
        category_subjects[category_id] = subjects
    
    context = {
        'distinct_categories': distinct_categories,
        'category_subjects': category_subjects
    }
    
    return render(request, 'cat_video.html', context)


def videos(request,id):
    data = CustomUser.objects.get(username = request.user)
    video = video_meterial.objects.filter(user = data.student_guid,category = id)
    return render(request,'vidoe.html',{'video':video})



def study_material(request):
    return render(request,'study_material.html')


def delete_video_met(request, id):
    data = video_meterial.objects.get(id=id)
    data.video.delete()
    data.delete()  
    return redirect('/add_video_material')



def delete_material(request, id):
    data = study_meterial.objects.get(id=id)
    data.meterial.delete()
    data.delete()  
    return redirect('/add_study_material')


def del_category(request, id):
    data = category.objects.get(id=id)
    data.delete()  
    return redirect('/add_category')

def add_category(request):
    data = category.objects.filter(user = request.user)
    if request.method == 'POST':
        categoryy = request.POST.get('category')
        subject=request.POST.get('subject')
        category.objects.create(user = request.user,categoryy=categoryy,subject=subject)
        return redirect('/add_category')
    return render(request,'add_category.html',{'data':data})


def add_video_material(requset):
    data = category.objects.all()
    material_data = video_meterial.objects.filter(user = requset.user)
    if requset.method == 'POST':
        categoryy = requset.POST.get('category')
        file = requset.FILES.get('file')
        video_meterial.objects.create(user = requset.user,category = categoryy,video=file)
        return redirect('/add_video_material')
    return render(requset,'add_video_material.html',{'data':data,'material_data':material_data})

def add_study_material(requset):
    data = category.objects.all()
    material_data = study_meterial.objects.filter(user = requset.user)
    if requset.method == 'POST':
        categoryy = requset.POST.get('category')
        subject = requset.POST.get('subject')
        file = requset.FILES.get('file')
        study_meterial.objects.create(user = requset.user,category = categoryy,meterial=file,subject=subject)
        return redirect('/add_study_material')
    return render(requset,'add_study_material.html',{'data':data,'material_data':material_data})
 
def payment(request,id):
    data =  CustomUser.objects.get(username = request.user)
    if data.payment == 'success':
        return redirect('/mentor_access')
    else:
        fac_data =  CustomUser.objects.get(id = id)
        if request.method == 'POST':
            user_data = CustomUser.objects.get(username = request.user)
            user_data.student_guid = int(id)
            user_data.student_conformation = 'waiting'
            user_data.payment == 'success'
            user_data.save()
            return redirect('/payment_success/'+str(fac_data.id)+'/')
        return render(request,'payment.html',{'fac_data':fac_data})

def payment_success(request,id):
    fac_data =  CustomUser.objects.get(id = id)
    acount = fac_data.fee
    return render(request,'paymen_success.html',{'acount':acount})


def view_student_details(request,id):
    t_data = CustomUser.objects.get(id = id)
    if t_data.student_conformation == 'waiting':
        data = CustomUser.objects.get(id = id)
    else:
        data = None

    if request.method == 'POST':
        if request.POST.get('rej_acc') == 'Accept':
            print(data.student_conformation)
            # subject = 'course code'
            # message = 'your code is: '+data.contact+''
            # from_email = 'abishek14052018@gmail.com'
            # recipient_list = [data.email]
            # email = EmailMessage(subject, message, from_email, recipient_list)
            # email.send()
            data.student_conformation = 'success'
            data.reason = request.POST.get('reason')
            
            data.save()
            return redirect('/Student_request')
        else:
            data.student_conformation = 'rejected'
            data.reason = request.POST.get('reason')
            data.student_guid = None
            data.save()
            return redirect('/faculty_dashboard')
    return render(request,'view_student_detail.html',{'data':data})



def Student_request(request):
    data = CustomUser.objects.get(username = request.user)
    student_data = CustomUser.objects.filter(student_guid = data.id,student_conformation = 'waiting')
    return render(request,'Student_request.html',{'data':student_data})

def mentor_access(request):
    data = CustomUser.objects.filter(user_type = 2)
    user_det = get_object_or_404(CustomUser, username=request.user)
    try:
        user_guid = CustomUser.objects.get(id = user_det.student_guid)
    except:
        user_guid = 'None'
    return render(request,'mentor_access.html',{'data':data,'user_det':user_det,'user_guid':user_guid})

def faq(request):
    return render(request,'faq.html')

def privacy_and_policy(request):
    return render(request,'privacy_and_policy.html')


def terms_and_conditions(request):
    return render(request,'terms_and_conditions.html')

def add_job(request):
    data = job.objects.all()
    if request.method == 'POST':
        img = request.FILES.get('img')
        title = request.POST.get('titile')
        point = request.POST.get('point')
        job.objects.create(img = img,title=title, point=point)
        return redirect('/add_job')
    return render(request,'add_job.html',{'data':data})

def job_delet(request,id):
    data = job.objects.get(id = id)
    data.img.delete()
    data.delete()
    return redirect('/add_job')






def add_incentive(request):
    data = incentive.objects.all()
    if request.method == 'POST':
        title = request.POST.get('titile')
        point = request.POST.get('point')
        incentive.objects.create(title=title, point=point)
        return redirect('/add_incentive')
    return render(request,'add_incentive.html',{'data':data})
def incentive_delet(request,id):
    data = incentive.objects.get(id = id)
    data.delete()
    return redirect('/add_incentive')


def add_loans(request):
    data = Loan.objects.all()
    if request.method == 'POST':
        title = request.POST.get('titile')
        point = request.POST.get('point')
        Loan.objects.create(title=title, point=point)
        return redirect('/add_loans')
    return render(request,'add_loan.html',{'data':data})
def loans_delet(request,id):
    data = Loan.objects.get(id = id)
    data.delete()
    return redirect('/add_loans')

def grant_delet(request,id):
    data = Grant.objects.get(id = id)
    data.delete()
    return redirect('/add_grants')

def add_grants(request):
    data = Grant.objects.all()
    if request.method == 'POST':
        title = request.POST.get('titile')
        point = request.POST.get('point')
        Grant.objects.create(title=title, point=point)
        return redirect('/add_grants')
    return render(request,'add_grants.html',{'data':data})

def more_informations(request):
    return render(request,'more_information.html')


def mentor_records(request):
    data = CustomUser.objects.filter(verifi = True)
    return render(request,'mentor_records.html',{'data':data})
    



def add_mendor(request):
    data = CustomUser.objects.filter(verifi = False)   
    return render(request,'add_mendor.html',{'data':data})


def student_signup(request):
    data = 'Student Signup'
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['emal']
        contact = request.POST['number']
        clg_name = request.POST['c_name']
        username = request.POST['uname']
        password1 = request.POST['psw']
        password2 = request.POST['re_psw']
        if CustomUser.objects.filter(username = username):
            messages.error(request,'username is already taken')
            return redirect('/')     
        if password1 == password2:
            CustomUser.objects.create_user(username=username, password=password1, user_type=1,name = name,age = int(age),gender = gender,email = email,contact = int(contact),class_name = clg_name)
            return redirect('/login')
        
    return render(request, 'signup.html',{'data':data})

def faculty_signup(request):
    data = 'Faculty Signup'
    if request.method == 'POST':
        username = request.POST['uname']
        password1 = request.POST['psw']
        password2 = request.POST['re_psw']
        email = request.POST['email']
        number =  request.POST['number']
        qly =  request.POST['qly']
        cls = request.POST['cls']
        fee = request.POST['fee']
        if CustomUser.objects.filter(username = username):
            messages.error(request,'username is already taken')
            return redirect('/')  
        if password1 == password2:
            user = CustomUser.objects.create_user(username=username, password=password1, user_type=2,email = email,contact = number,qualification = qly,class_name = cls,fee = fee,verifi = False)
            return redirect('/login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('/admin_signup')
    return render(request, 'fac_signup.html',{'data':data})



def admin_signup(request):
    data = 'Admin Signup'
    if request.method == 'POST':
        username = request.POST['uname']
        password1 = request.POST['psw']
        password2 = request.POST['re_psw']
        pin = request.POST['pin'] #1234
        
        if int(pin) != 1234:
            messages.error(request, 'Invalid PIN')
            return redirect('/admin_signup')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('/admin_signup')
        
        

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('/admin_signup')
        
        CustomUser.objects.create_user(username=username, password=password1, user_type=3)
        return redirect('/login')
    
    return render(request, 'admin_signup.html', {'data': data})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password1 = request.POST.get('psw')
        
        if not username or not password1:
            messages.error(request, 'Please enter both username and password.')
            return redirect('/login')

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            data = CustomUser.objects.get(username=username)
            
            # Redirect based on user_type
            if data.user_type == 1:
                return redirect('/student_dashboard')
            elif data.user_type == 2:
                # Check for faculty verification (assuming verifi is a boolean field)
                if (data.verifi) == 'True':
                    print(data.verifi)
                    return redirect('/faculty_dashboard')
                else:
                    messages.error(request, 'Request declined. Your account is not verified.')
                    return redirect('/login')
            elif data.user_type == 3:
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'User type not recognized.')
                return redirect('/login')

        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('/login')

    return render(request, 'login.html')


def logoutt(request):
    logout(request)
    return redirect('/')


@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required
def faculty_dashboard(request):
    return render(request, 'faculty_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def index(request):        
    return render(request,'index.html')

def common_signup(request):        
    return render(request,'common_signup.html')

