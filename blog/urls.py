from django.urls import path
from . import views

urlpatterns = [
    # 요거는 CVB 사용할 때
    # 주소에 접속했을 때 게시글 목록 페이지를 보여주도록 연결하는 코드
    # views.py 안의 PostList 클래스가 실행
    path('',views.PostList.as_view()),
    path('<int:pk>/',views.PostDetail.as_view())
    
    # 요거는 FBV 사용할 때
    # path('<int:pk>/', views.single_post_page),
    # path('',views.index), # views.py에 index함수 만들거임

]