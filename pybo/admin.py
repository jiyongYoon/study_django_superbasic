from django.contrib import admin
from .models import Question, Answer

# Register your models here.

# Question 모델을 관리자가 관리할 수 있도록 등록
# admin.site.register(Question)
admin.site.register(Answer)


# 관리자 화면에 검색기능 추가
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject'] # 모델의 검색할 컬럼


admin.site.register(Question, QuestionAdmin)

# [장고 관리자기능 공식문서](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)