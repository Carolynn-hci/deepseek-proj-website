from django.shortcuts import render, redirect

from django.contrib.auth import logout

from .openai_ref import Event_source_stream

#for ds2
from django.http import JsonResponse, StreamingHttpResponse


# Create your views here.
def home(request):
    return render(request,'homepage.html')

def logout_view(request):
    logout(request)
    return redirect('/')


    
def deepseek_stream_chat(request):

    prompt = request.GET.get('prompt')
    if prompt:
        response = StreamingHttpResponse(Event_source_stream(prompt = prompt),content_type="text/event-stream")
        response['Cache-Control'] = 'no-cache'
        response.flush = True
        return response
    else:
        return render(request,'stream_deepseek_chat.html')    
