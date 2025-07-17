from django.urls import path
from . import views

app_name = 'auth_app'
urlpatterns = [
    path('',views.home),
    
    path('logout',views.logout_view),

    path('stream_chatbot/',views.deepseek_stream_chat),

    path('edit_learning_mode/',views.edit_learning_mode)
]