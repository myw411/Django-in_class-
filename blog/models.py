from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30) # 제목 글자수 제한
    content = models.TextField() # 내용
    
    created_at = models.DateTimeField(auto_now_add=True) # 날짜
    updated_at = models.DateTimeField(auto_now=True) # 날짜
    
    # author: 추후 작성 예정
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    