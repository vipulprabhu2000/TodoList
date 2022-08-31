from asyncio.windows_events import NULL
from django.shortcuts import render

list_message=[]
# Create your views here.
def index(request):
    list_message.clear()
    return render(request,'index.html')
    

def todolist(request):
    global list_message
    text=request.POST['text']
    list_message.append(text)
    return render(request,'index.html',{'todotext':list_message})
        
   

    
