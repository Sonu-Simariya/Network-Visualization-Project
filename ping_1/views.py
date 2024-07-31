
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login,logout
# from django.http import JsonResponse

from .models import CustomUser,details,live_data,csv_1
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from collections import Counter
from datetime import datetime,date
from django.contrib import messages

from pythonping import ping
import socket
import csv
import datetime as dt

from nltk.chat.util import Chat, reflections





def Logout(request):
    logout(request)
    return redirect ('Log')

@csrf_exempt
@login_required
def alert(request):
    if request.method == 'POST':
        user_id = request.user.id
        timestamp=datetime.now()
        ip_address = request.POST.get('ip_address',not None)
        status=request.POST.get('quantity',not None)
        if request.method == 'POST':
            ip_address = request.POST.get('ip_address')
            try:
                response = ping(ip_address)
                if response.success():
                    status = 'Reachable'
                else:
                    status = 'Destination Unreachable'
                
            except Exception as e:
                status = 'False - Error: ' + str(e) 
                
            ping_result = live_data(ip_address=ip_address, status=status,cust_id_id=user_id)
            ping_result.save()
            user_id = request.user.id
            data = live_data.objects.filter(cust_id_id=user_id)

            return render(request, 'ui-alerts.html', {'data':data,'ip_address':ip_address,'timestamp':timestamp, 'status': status})

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    user_id = request.user.id

    events = live_data.objects.filter(cust_id_id=user_id)
    if start_date:
        events = events.filter(timestamp__gte=start_date)

    if end_date:
        events = events.filter(timestamp__lte=end_date)
    return render(request, 'ui-alerts.html',{'user_id':user_id,'events':events})
@csrf_exempt
@login_required
def time(request):
    nowt=datetime.now()
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    user_id = request.user.id

    events = details.objects.all()
    if start_date:
        events = events.filter(id_cust_id=user_id,date_1__gte=start_date)

    if end_date:
        events = events.filter(id_cust_id=user_id,date_1__lte=end_date)
    z=len(events.filter(Status='Reachable'))
    y=len(events.filter(Status='Destination Unreachable'))
    x=z+y
    return render(request, 'ui-card.html',{'events':events,'x':x,'y':y,'z':z,'nowt':nowt})
@csrf_exempt
def Log(request):
    if request.method == 'POST':
    
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the user exists in the custom database
        user = CustomUser.objects.filter(username=username, password=password,isadmin=False).first()

        if user:
            # Log in the user
            login(request, user)
            # Redirect to a success page
            return redirect('desktop')
        else:
            # Handle invalid login credentials
            error_message = {'message': 'Invalid login credentials'}
            return render(request, 'authentication-login - Copy.html', {'error_message': error_message,'is_True': True})
    else:
        return render(request, 'authentication-login - Copy.html')
@csrf_exempt
def Regiss(request):
    if request.method == "POST":
        first_name = request.POST.get("f_name",not None)
        last_name = request.POST.get("l_name",not None)
        email = request.POST.get("Email",not None)
        password=request.POST.get("Password1", not None)
        confirm_password=request.POST.get("password2", not None)
        if CustomUser.objects.filter(username=first_name+last_name+email).exists():
            return render(request, 'authentication-login - Copy.html')
        else:
        
            user = CustomUser(username=first_name+last_name,last_name=last_name ,first_name=first_name,confirm_password=confirm_password,email=email, password=password,isadmin=False)
            user.save()
            context=HttpResponse('User created')
            return context  
    return render(request, 'authentication-register - Copy.html')
def check_network_connection():
    ping_result = ping('172.18.90.200', count=6)
    if ping_result.success():
        return "Connected"
    else:
        return "Connected"

@csrf_exempt
@login_required
def desktop(request):
    
    now=datetime.now()
    user_id=request.user.id
    data = details.objects.filter(id_cust_id=user_id)
    P=details.objects.order_by('-id')[:]
    dis=details.objects.order_by('-id')[:30]
    now=date.today()
    p1 = details.objects.order_by('-id')[0]
    z=details.objects.order_by('-id')[:]
    type_counts = dict(Counter(fruit.Ip for fruit in data))
    ip_add = details.objects.order_by('-id')[:1]  
    labes = []
    last_5_addresses = details.objects.order_by('-id')[:1]
    labels = [str(  Ip) for Ip in last_5_addresses]
    dat = [1] * len(last_5_addresses)
    user_ip=request.META.get('REMOTE_ADDR')
    try:
        ping_result = ping('172.18.90.200', count=1)
        if ping_result.success():
            state=True
        else:
            state=False
    except:
        status_1="Error"
    if request.method=='POST':
        inputs = request.POST.get('inputss',not None)
        if inputs is not  None:
            response=datetime.now()
        else:
            response="please type 'what is Time: ' "
    else:
        response="exit"
    server_ip = socket.gethostbyname(socket.gethostname())
    
    if server_ip == server_ip:
        status_1=check_network_connection()
        if state:
            status_1="Connected"
            status = {'message': 'Not Connected '}
            if status_1=='Connected':
                
                current_index = request.session.get('current_index', 0)
                z=csv_1.objects.all()
                if current_index >= len(z):
                    current_index = 0  
                current_value = csv_1.objects.values_list('Ip', flat=True)[current_index]
                Loc = csv_1.objects.values_list('Location', flat=True)[current_index]
                
                if status_1=='Connected':

                    if request.method=='POST':
                        ip_address = csv_1.objects.values_list('Ip', flat=True)[current_index]
                        Loc = csv_1.objects.values_list('Location', flat=True)[current_index]
                        Date = request.POST.get('date',not None)
                        response = ping(ip_address)
                        
                        if response.success():
                            staus = 'Reachable'
                            request.session['current_index'] = current_index + 1
                    
                        else:
                            staus = 'Destination Unreachable'
                            request.session['current_index'] = current_index + 1

                        ping_result= details(id_cust_id=user_id,Status=staus,Ip=ip_address,Rack_Location=Loc,date_1=Date)
                        ping_result.save()
                
                else:
                    status = {'message': 'Not Connected '}
                    status_1='Not Connected'
                    current_value="Ip: Connect to your Network" 
                    request.session['current_index'] = 0
                    Loc="Location: Connect to your Network"    
            else:
                
                status = {'message': 'Not Connected '}
                status_1='Not Connected'
                current_value="Ip: Connect to your Network" 
                request.session['current_index'] = 0
                Loc="Location: Connect to your Network"    

        else:
                
            status = {'message': 'Not Connected '}
            status_1='Not Connected'
            current_value="Ip: Connect to your Network" 
            request.session['current_index'] = 0
            Loc="Location: Connect to your Network"
        
            
                

    else:
        request.session['position'] = 0
        status = {'message': 'Not Connected '}
        status_1='Not Connected'
        current_value="Ip: Connect to your Network"  
        Loc="Location: Connect to your Network"

    message="IP and Location Save Done"
    labels=[]
    a1=details.objects.filter(Ip='172.18.90.196').last()
    a2=details.objects.filter(Ip='172.18.90.197').last()
    a3=details.objects.filter(Ip='172.18.90.198').last()
    a4=details.objects.filter(Ip='172.18.90.199').last()
    a5=details.objects.filter(Ip='172.18.90.200').last()
    a6=details.objects.filter(Ip='172.18.90.201').last()
    a7=details.objects.filter(Ip='172.18.90.202').last()
    a8=details.objects.filter(Ip='172.18.90.203').last()
    a9=details.objects.filter(Ip='172.18.90.204').last()
    a10=details.objects.filter(Ip='172.18.90.205').last()
    a11=details.objects.filter(Ip='172.18.90.206').last()
    a12=details.objects.filter(Ip='172.18.90.207').last()
    a13=details.objects.filter(Ip='172.18.90.208').last()
    a14=details.objects.filter(Ip='172.18.90.209').last()
    a15=details.objects.filter(Ip='172.18.90.210').last()
    a16=details.objects.filter(Ip='172.18.90.211').last()
    a17=details.objects.filter(Ip='172.18.90.212').last()
    a18=details.objects.filter(Ip='172.18.90.213').last()
    a19=details.objects.filter(Ip='172.18.90.214').last()
    a20=details.objects.filter(Ip='172.18.90.215').last()
    a21=details.objects.filter(Ip='172.18.90.216').last()
    a22=details.objects.filter(Ip='172.18.90.217').last()
    a23=details.objects.filter(Ip='172.18.90.218').last()
    a24=details.objects.filter(Ip='172.18.90.219').last()
    a25=details.objects.filter(Ip='172.18.90.220').last()
    a26=details.objects.filter(Ip='172.18.90.221').last()
    a27=details.objects.filter(Ip='172.18.90.222').last()
    a28=details.objects.filter(Ip='172.18.90.223').last()
    a29=details.objects.filter(Ip='172.18.90.224').last()
    a30=details.objects.filter(Ip='172.18.90.225').last()
    a31=details.objects.filter(Ip='172.18.90.226').last()
    a32=details.objects.filter(Ip='172.18.90.227').last()
    a33=details.objects.filter(Ip='172.18.90.228').last()
    a34=details.objects.filter(Ip='172.18.90.229').last()
    a35=details.objects.filter(Ip='172.18.90.230').last()
    a36=details.objects.filter(Ip='172.18.90.231').last()
    a37=details.objects.filter(Ip='172.18.90.232').last()
    a38=details.objects.filter(Ip='172.18.90.233').last()
    a39=details.objects.filter(Ip='172.18.90.234').last()
    a40=details.objects.filter(Ip='172.18.90.235').last()
    a41=details.objects.filter(Ip='172.18.90.236').last()
    a42=details.objects.filter(Ip='172.18.90.237').last()
    a43=details.objects.filter(Ip='172.18.90.238').last()
    a44=details.objects.filter(Ip='172.18.90.239').last()
    a45=details.objects.filter(Ip='172.18.90.240').last()
    a46=details.objects.filter(Ip='172.18.90.241').last()
    a47=details.objects.filter(Ip='172.18.90.242').last()
    a48=details.objects.filter(Ip='172.18.90.243').last()
    a49=details.objects.filter(Ip='172.18.90.244').last()
    a50=details.objects.filter(Ip='172.18.90.245').last()
    a51=details.objects.filter(Ip='172.18.90.246').last()
    a52=details.objects.filter(Ip='172.18.90.247').last()
    a53=details.objects.filter(Ip='172.18.90.248').last()
    a54=details.objects.filter(Ip='172.18.90.249').last()
    a55=details.objects.filter(Ip='172.18.90.250').last()
    a56=details.objects.filter(Ip='172.18.90.251').last()
    a57=details.objects.filter(Ip='172.18.90.252').last()
    a58=details.objects.filter(Ip='172.18.90.253').last()
    a59=details.objects.filter(Ip='172.18.90.254').last()
    a60=details.objects.filter(Ip='172.18.90.255').last()

    for ip in ip_add:
        labels.append(ip.Ip)
        labes.append(ip.Status)
    context = {
    'data':data,'user_id':user_id,  
    'type_counts':type_counts,'dat':dat,
    'Loc':Loc,'current_value':current_value, 
    'labels':labels,'labes':labes,'P':P,'p1':p1,
    'z':z,'user_ip':user_ip,'server_ip':server_ip,
    'status':status,'status_1':status_1,
    'a1':a1,'a2':a2,'a3':a3,'a4':a4,'a5':a5,'a6':a6,'a7':a7,'a8':a8,'a9':a9,'a10':a10,
    'a11':a11,'a12':a12,'a13':a13,'a14':a14,'a15':a15,
    'a16':a16,'a17':a17,'a18':a18,'a19':a19,'a20':a20,'a21':a21,'a22':a22,'a23':a23,
    'a24':a24,'a25':a25,'a26':a26,'a27':a27,'a28':a28,'a29':a29,
    'a30':a30,'a31':a31,'a32':a32,'a33':a33,'a34':a34,'a35':a35,'a36':a36,
    'a37':a37,'a38':a38,'a39':a39,'a40':a40,'a41':a41,'a42':a42,'a43':a43,
    'a44':a44,'a45':a45,'a46':a46,'a47':a47,'a48':a48,'a49':a49,'a50':a50,
    'a51':a51,'a52':a52,'a53':a53,'a54':a54,'a55':a55,'a56':a56,
    'a57':a57,'a58':a58,'a59':a59,'a60':a60,'now':now,'dis':dis,'response':response,
    

    
    
}

    return render(request, 'index2 - Copy.html',context)





def Logt(request):
    logout(request)
    return redirect ('Log')
@csrf_exempt
@login_required
def pie2(request):
    now=datetime.now()
    p1 = details.objects.order_by('-id')[0]
    p2 = details.objects.order_by('-id')[1]
    p3 = details.objects.order_by('-id')[2]
    
    last_5_addresses = details.objects.order_by('-id')[:3]
    labels = [str(  Ip) for Ip in last_5_addresses]
    dat = [1] * len(last_5_addresses)
    labes = []
    labels=[]
    for ip in last_5_addresses:
        labels.append(ip.Ip)
        labes.append(ip.Status) 

    return render(request, 'ui-buttons.html',{'labes': labes,'dat':dat,'labels':labels,'p1':p1,'p2':p2,'p3':p3,'now':now})
@csrf_exempt
@login_required
def alert2(request):
    if request.method == 'POST':
        user_id = request.user.id
        timestamp=datetime.now()
        ip_address = request.POST.get('ip_address',not None)
        status=request.POST.get('quantity',not None)
        if request.method == 'POST':
            ip_address = request.POST.get('ip_address')
            try:
                response = ping(ip_address)
                if response.success():
                    status = 'Reachable'
                else:
                    status = 'Destination Unreachable'
                
            except Exception as e:
                status = 'False - Error: ' + str(e) 
            
            ping_result = live_data(ip_address=ip_address, status=status,cust_id_id=user_id)
            ping_result.save()
            user_id = request.user.id
            data = live_data.objects.filter(cust_id_id=user_id)
            now=datetime.now()

            return render(request, 'ui-alerts.html', {'data':data,'ip_address':ip_address,'timestamp':timestamp, 'status': status,'now':now})

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    user_id = request.user.id
    now=datetime.now()

    events = live_data.objects.filter(cust_id_id=user_id)

    if start_date:
        events = events.filter(timestamp__gte=start_date)

    if end_date:
        events = events.filter(timestamp__lte=end_date)
    
    return render(request, 'ui-alerts.html',{'user_id':user_id,'events':events,'now':now})
@login_required
@csrf_exempt
def ip_save(request):
    if request.method=='POST':
        user_id=request.user.id
        ip=request.POST.get('IP',not None)
        ips=request.POST.get('ipm',not None)
        chatbot=request.GET.get('userMessage')
        Location=request.POST.get('LOCATION',not None)
        Description=request.POST.get('Description',not None)
        if 'add' in request.POST:
            if csv_1.objects.filter(Ip=ip).exists():
                messages.success(request,"Ip is already Exists")
                return redirect('ip_save')
            else:
                pi_result=csv_1(Ip=ip, Location=Location,user_id_id=user_id,Description=Description)
                pi_result.save()
                messages.error(request,  "Your Record is saved successfully")
                return redirect('ip_save')
        elif 'update' in request.POST:
            ipss=request.POST.get('ipmm',not None)
            yy=request.POST.get('Locc',not None)
            zz=request.POST.get('Dess',not None)
            # Check if the IP exists
            ip_exists = csv_1.objects.filter(Ip=ipss).exists()
            if ip_exists:
                # Fetch the object to update
                obj = csv_1.objects.get(Ip=ipss)
                obj.Ip=ipss
                obj.Location = yy
                obj.Description = zz
                obj.save()
                messages.success(request,"Ip is updated successfully")
                return redirect('ip_save')
            else:
                messages.success(request,"Ip not exists ")
                return redirect('ip_save')
        elif 'delete' in request.POST:
            if csv_1.objects.filter(Ip=ips).exists():
                item =csv_1.objects.filter(user_id_id=user_id,Ip=ips)
                item.delete()
                messages.success(request,"Ip is deleted")
                return redirect('ip_save')
            else:
                messages.success(request,"Ip is not exist")
                return redirect('ip_save')
        else:
        
            messages.error(request,  "Invaild")
            return redirect('ip_save')
    user_id=request.user.id
    P=csv_1.objects.filter(user_id_id=user_id)
    x=len(P)
    now=datetime.now()

    return render(request, 'record.html',{'P':P,'x':x,'now':now})
    




def read_csv_data(filename):
    time=dt.datetime.now()
    pairs = [
    ['hi', ['Hello!', 'Hi there!', 'How can I help you?']],
    ['your name?', ['My name is LEO.']],
    ['how old are you', ['I am just a chatbot.']],
    ['i need help.', ['I can help you with various tasks.']],
    ['which company created LEO?', ['CMTI created LEO AI.']],
    ['time',[f'the date & time is ,{time}']],
    ['CMTI created LEO AI.',['yes LALIT SIMARIYA CREATED LEO CHATBOT']],
    ['WHAT IS CHATBOT',['a computer program designed to simulate conversation with human users, especially over the internet.']]
    ]
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 0:  # Ensure each row has at least an input pattern and response
                input_pattern = row[0].strip()  # Assuming input pattern is in the first column
                response = row[1].strip()  # Assuming response is in the second column
                pairs.append([input_pattern, [response]])
    return pairs
import subprocess
def chat(request):

    user_message = request.GET.get('userMessage')
    bot_response = None
    if user_message:
        z=csv_1.objects.filter(Ip=user_message).exists()
        a=f"{z}"
        if z:
            try:
                # Run the ping command
                result = subprocess.run(['ping', '-c', '1', a], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode == 0:
                    result=f"{user_message} working properly"
                    
                else:
                    result=f"{user_message} not working please check ."
                    
            except Exception as e:
                result="Check the function"
            # Call the function with the IP address
            
            bot_response=[result]
        elif z:
            a=csv_1.objects.filter(Ip=user_message).last()
            b=details.objects.filter(Ip=user_message).last()
            
            bot_response=['Location is:-',a.Location,'Type:-',a.Description,'Last detail:-',b.date_1,'Status:-',b.Status]
        else:
            pairs = read_csv_data('chatbot_data.csv')  # Read pairs from CSV file
            chatbot = Chat(pairs, reflections)
            bot_response = chatbot.respond(user_message)
    return HttpResponse(bot_response)
    


