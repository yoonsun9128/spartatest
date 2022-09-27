from django.shortcuts import render
from introduce.models import Accesslogs

# Create your views here.
def intro(request):
    access_log = Accesslogs()
    # 지정 어디 페이지를 들어갈때 로그할껀지 지정
    access_log.location = "introduce"
    access_log.save()
    return render(request, 'intro.html')