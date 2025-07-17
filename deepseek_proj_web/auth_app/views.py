from django.shortcuts import render, redirect

from django.contrib.auth import logout

from .openai_ref import Event_source_stream


#for ds2
from django.http import HttpResponse, StreamingHttpResponse
from django.template import loader
import os
module_dir = os.path.dirname(__file__)  # get current directory

def get_prompts():
    file_path = os.path.join(module_dir, 'learning_mode_prompts.txt')
    with open(file_path,'r') as file:
        data = file.readlines()
        data = ''.join(data)
    return data

# Create your views here.
def home(request):
    return render(request,'homepage.html')

def logout_view(request):
    logout(request)
    return redirect('/')


    
def deepseek_stream_chat(request):

    prompt = request.GET.get('prompt')
    if not prompt:
        return render(request,'stream_deepseek_chat.html')  
    response = StreamingHttpResponse(Event_source_stream(prompt = prompt),content_type="text/event-stream")
    response['Cache-Control'] = 'no-cache'
    response.flush = True
    return response

      

def edit_learning_mode(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        content = content.replace('\r\n','\n')
        file_path = os.path.join(module_dir, 'learning_mode_prompts.txt')
        with open(file_path,'w') as file:
          file.write(content)
        return render(request,'form_submitted.html')
    
    content = {'content' :get_prompts() }
    template = loader.get_template('edit_learning_mode.html')

    return HttpResponse(template.render(content, request))