from django.db import models

# Create your models here.

# 장고에서 사용하는 속성 타입
# https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types

class Question(models.Model):
    subject = models.CharField(max_length=200) # 최대 200자까지 가능 / CharField는 글자수 길이가 제한된 텍스트일경우 사용
    content = models.TextField() # 글자수 길이 제한이 없음
    create_date = models.DateTimeField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question 모델과 연관관계 매핑. CASCADE 속성은, 질문이 지워지면 답변도 지워진다는 뜻
    content = models.TextField()
    create_date = models.DateTimeField()

# 이 모델을 사용하여 Table을 생성하기 위해서는 config/settings.py 파일의 INSTALLED_APPS 항목에 추가해야함

"""
모델이 신규로 생성되거나 수정되면 `makemigrations` 명령을 먼저 수행한 후에 `migrate` 명령을 수행해야 한다.
python manage.py makemigrations
: 앱.migrations 폴더에 migration을 위한 데이터베이스 작업 파일을 생성한다.
-> python manage.py sqlmigrate pybo 0001
: 해당 작업파일의 sql문을 실행하면 어떤 쿼리문이 실행되는지 확인해볼 수 있다.
-> python manage.py migrate
: 실제 sql문을 실행하여 테이블을 생성한다.
"""