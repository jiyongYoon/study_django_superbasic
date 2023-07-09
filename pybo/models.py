from django.db import models

# Create your models here.

# 장고에서 사용하는 속성 타입
# https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types


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


class Question(models.Model):
    subject = models.CharField(max_length=200) # 최대 200자까지 가능 / CharField는 글자수 길이가 제한된 텍스트일경우 사용
    content = models.TextField() # 글자수 길이 제한이 없음
    create_date = models.DateTimeField()


    """
    모델의 데이터는 .objects를 통해서 조회 가능하다.
    >>> Question.objects.all() -> Question의 모든 데이터를 조회하는 함수
    <QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>
    : 결과값의 () 안에 숫자는 해당 데이터의 id 값이다.
    아래와 같은 함수의 리턴값을 특정해주면, .objects로 조회 시 () 안에 리턴되는 값을 변경할 수 있다.
    """
    def __str__(self):
        return self.subject
    """
    >>> Question.objects.all()                   
    <QuerySet [<Question: pybo가 무엇인가요?>, <Question: 장고 모델 질문입니다.>]>
    
    >>> Question.objects.filter(id=1)
    <QuerySet [<Question: pybo가 무엇인가요?>]>
    [필터 사용법 공식문서](https://docs.djangoproject.com/en/4.0/topics/db/queries/)
    
    >>> Question.objects.get(id=1)
    <Question: pybo가 무엇인가요?>
    """


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question 모델과 연관관계 매핑. CASCADE 속성은, 질문이 지워지면 답변도 지워진다는 뜻
    content = models.TextField()
    create_date = models.DateTimeField()


    """
    1) Answer 데이터를 기입할 때는 Question을 넣어줄 수 있다.
    >>> q=Question.objects.get(id=2)               
    >>> q
    <Question: 장고 모델 질문입니다.>
    >>> from django.utils import timezone
    >>> a = Answer(question = q, content = '네 자동생성됩니다.', create_date=timezone.now())
    >>> a.save()

    2) Answer 객체에 연관된 Question도 불러올 수 있다.
    >>> a.question
    <Question: 장고 모델 질문입니다.>

    3) Question 객체에 연관된 Answer도 불러올 수 있다.
    >>> q.answer
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    AttributeError: 'Question' object has no attribute 'answer'
    안되네??
    >>> q.answer_set.all() 
    <QuerySet [<Answer: Answer object (1)>]>
    이렇게 가져와야 한다.
    Java로 따지면 단방향 연관관계구만!
    """
