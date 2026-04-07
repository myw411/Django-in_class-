from django.contrib import admin

# Register your models here.
from .models import Post  # 현재 파일에서 models안에 Post를 쓰겠다

admin.site.register(Post)