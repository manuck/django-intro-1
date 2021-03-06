from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # print(request.META)
    # return HttpResponse(request, 'index.html')
    return render(request, 'index.html')
    
def dinner(request):
    box = ['치킨', '치킨', '롯데리아']
    dinner = random.choice(box)
    '''
    render 필수인자
    1) request, 2) template 파일(html)
    render 선택인자
    3) dictionary : 템플릿에서 쓸 변수 값을 정의
    '''
    
    # return HttpResponse(dinner)
    # return render(request, 'dinner.html') # dinner.html 렌더링해주기
    return render(request, 'dinner.html', {'dinner' : dinner, 'box' : box}) #인자 넘겨주기
    # template는 기본적로 문법이 jinja2랑 비슷한데 장고에서는 DTL을 쓴다.
    # dDjango Template Language

def you(request, name):
    # name = '지원'
    return render(request, 'you.html', {'name' : name})

def cube(request, num):
    # num = int(num) # url.py 에서 <int:num>로 넘겨주면 생략가능
    return render(request, 'cube.html', {'cube' : num**3})
    
# import random
# from django.shortcuts import render, HttpResponse

# # Create your views here.
# def index(request):
#     print(request)
#     print(type(request))
#     print(request.META)
#     return render(request, 'index.html')
    
# def dinner(request):
#     box = ['치킨', '치킨', '편도', '롯데리아']
#     dinner = random.choice(box)
#     # render 필수인자
#     # 1) request,  2) template 파일(html)
#     # render 선택인자
#     # 3) dictionary : 템플릿에서 쓸 변수 값을 정의
#     return render(request, 'dinner.html', {'dinner': dinner, 'box': box})
#     # template은 기본적으로 문법이 jinja2랑 비슷한데, 장고에서는 DTL을 쓴다.
#     # Django Template Language

# def you(request, name):
#     return render(request, 'you.html', {'name': name})