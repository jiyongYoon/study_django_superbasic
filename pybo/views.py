from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .models import Topic, Question, Answer

count = 0
routing_count = 0
view_count = 0
model_count = 0
# topics = [
#     {'id':1, 'title':'routing', 'body': 'Routing is ...'},
#     {'id':2, 'title':'view', 'body': 'View is ...'},
#     {'id':3, 'title':'Model', 'body': 'Model is ...'}
# ]

# def HTMLTemplate(articleTag, id=None):
#     ol = ''
#     topics = Topic.objects.order_by('-id')
#     print(topics)
#     for topic in topics:
#         ol += f'<li><a href="/read/{topic.id}">{topic.title}</a></li>'
#     return f'''
#     <html>
#     <body>
#         <h1><a href="/">Django</a></h1>
#         <ul>
#             {ol}
#         </ul>
#         {articleTag}
#         <ul>
#             <li><a href="/create/">create</a></li>
#         </ul>
#     </body>
#     </html>
#     '''
#
# @csrf_exempt
# def delete(request):
#     if request.method == 'POST':
#         id = request.POST['id']
#         findTopic = Topic.objects.get(id=id)
#         findTopic.delete()
#         return redirect('/')
#
# @csrf_exempt
# def read(request, topic_id):
#     try:
#         find_topic = Topic.objects.get(id=topic_id)
#     except Topic.DoesNotExist:
#         return HttpResponse('해당 게시글이 없습니다.')
#
#     article = f'''
#         <h2>{find_topic.title}</h2>
#         {find_topic.body} <br>
#         <form action="/delete/" method="post">
#             <p><input type="hidden" name="id" value={find_topic.id}></p>
#             <p><input type="submit" value="삭제"></p>
#         </form>
#         <li>
#             <a href="/update/{find_topic.id}">update</a>
#         </li>
#     '''
#     return HttpResponse(HTMLTemplate(article, id))
#
# @csrf_exempt
# def create(request):
#     if request.method == 'GET':
#         article = '''
#             <form action="/create/" method="post">
#                 <p><input type="text" name="title" placeholder="title"></p>
#                 <p><textarea name="body" placeholder="body"></textarea></p>
#                 <p><input type="submit"></p>
#             </form>
#         '''
#         return HttpResponse(HTMLTemplate(article))
#     elif request.method == 'POST':
#         topic = Topic(title=request.POST['title'], body=request.POST['body'])
#         topic.save()
#         return redirect('/read/' + str(int(topic.id)))
#
# @csrf_exempt
# def update(request, topic_id):
#     try:
#         findTopic: Topic = Topic.objects.get(id=topic_id)
#     except Topic.DoesNotExist:
#         return HttpResponse('해당 게시글이 없습니다.')
#
#     if request.method == 'GET':
#         article = f'''
#             <form action="/update/{topic_id}/" method="post">
#                 <p><input type="text" name="title" placeholder="title" value={findTopic.title}></p>
#                 <p><textarea name="body" placeholder="body">{findTopic.body}</textarea></p>
#                 <p><input type="submit"></p>
#             </form>
#         '''
#         return HttpResponse(HTMLTemplate(article, topic_id))
#     elif request.method == 'POST':
#         findTopic.title = request.POST["title"]
#         findTopic.body = request.POST["body"]
#         findTopic.save()
#         return redirect(f'/read/{topic_id}')


def HTMLTemplate(articleTag, id=None):
    ol = ''
    questions = Question.objects.order_by('-id')
    print(questions)
    for question in questions:
        ol += f'<li><a href="/read/{question.id}">{question.subject}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            <li><a href="/create/">질문 올리기</a></li>
        </ul>
        <ul>
            {ol}
        </ul>
        {articleTag}
    </body>
    </html>
    '''

def index(request):
    global count
    count += 1
    article = f'''
        <h2> Welcome </h2>
            Hello, <br>
        I'm django <br>
        today's visited: {count}
    '''
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        id = request.POST['id']
        findQuestion = Question.objects.get(id=id)
        findQuestion.delete()
        return redirect('/')

@csrf_exempt
def deleteAnswer(request):
    if request.method == 'POST':
        id = request.POST['id']
        findAnswer = Answer.objects.get(id=id)
        findAnswer.delete()
        return redirect(f'/read/{findAnswer.question_id}/')

@csrf_exempt
def read(request, question_id):
    try:
        findQuestion = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return HttpResponse('해당 질문이 없습니다.')

    allAnswer = findQuestion.answer_set.all()
    ol2 = ''
    for answer in allAnswer:
        ol2 += f'<li><a href="/read/answer/{answer.id}/">{answer.content}</a></li>'

    article = f'''
        <h3>-----------질문----------</h3>
        <li>
            <a href="/update/{findQuestion.id}/">질문 수정하기</a>
        </li>
        <h2>제목: {findQuestion.subject}</h2>
        내용: {findQuestion.content} <br>
        <form action="/delete/" method="post">
            <p><input type="hidden" name="id" value={findQuestion.id}></p>
            <p><input type="submit" value="삭제"></p>
        </form>
                
        <h3>----------답변----------</h3>
        <ul>
            {ol2}
        </ul>
        <br>
        <li>
            <a href="/create/answer/{findQuestion.id}/">답변 달기</a>
        </li>
            
        
    '''
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def readAnswer(request, answer_id):
    try:
        findAnswer = Answer.objects.get(id=answer_id)
    except Answer.DoesNotExist:
        return HttpResponse('해당 답변이 없습니다.')

    article = f'''
        {findAnswer.content} <br>
        <form action="/delete/answer/" method="post">
            <p><input type="hidden" name="id" value={findAnswer.id}></p>
            <p><input type="submit" value="답변 삭제"></p>
        </form>
        <li>
            <a href="/update/answer/{findAnswer.id}/">답변 수정</a>
        </li>
    '''
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="subject" placeholder="subject"></p>
                <p><textarea name="content" placeholder="content"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        question = Question(subject=request.POST["subject"], content=request.POST["content"], create_date=timezone.now())
        question.save()
        return redirect('/read/' + str(int(question.id)) + '/')


@csrf_exempt
def createAnswer(request, question_id):
    if request.method == 'GET':
        article = f'''
            <form action="/create/answer/{question_id}/" method="post">
                <p><input type="text" name="content" placeholder="content"></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        try:
            findQuestion = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return HttpResponse('해당 질문이 없습니다.')

        answer = Answer(question=findQuestion, content=request.POST["content"], create_date=timezone.now())
        answer.save()
        return redirect('/read/' + str(int(findQuestion.id)) + '/')



@csrf_exempt
def update(request, question_id):
    try:
        findQuestion: Question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return HttpResponse('해당 게시글이 없습니다.')

    if request.method == 'GET':
        article = f'''
            <form action="/update/{question_id}/" method="post">
                <p><input type="text" name="subject" placeholder="subject" value={findQuestion.subject}></p>
                <p><textarea name="body" placeholder="body">{findQuestion.content}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, question_id))
    elif request.method == 'POST':
        findQuestion.subject = request.POST["subject"]
        findQuestion.content = request.POST["content"]
        findQuestion.save()
        return redirect(f'/read/{question_id}/')



@csrf_exempt
def updateAnswer(request, answer_id):
    try:
        findAnswer: Answer = Answer.objects.get(id=answer_id)
    except Answer.DoesNotExist:
        return HttpResponse('해당 답변이 없습니다.')
    if request.method == 'GET':
        article = f'''
            <form action="/update/answer/{answer_id}/" method="post">
                <p><input type="text" name="content" value="{findAnswer.content}" placeholder="content"></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        findAnswer.content = request.POST["content"]
        findAnswer.save()
        return redirect(f'/read/{findAnswer.question_id}/')

###############################################################

from .models import Question


def pybo_index(request):
    question_list = Question.objects.order_by('-create_date') # - 가 붙어있으면 역순 정렬
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

"""
render 함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수.
위 index 함수는 question_list 데이터를 'pybo/question_list.html' 파일에 적용하여 HTML을 생성한 후 리턴한다.

점프 투 장고에 있는 모델을 활용하지 않고, 기존에 생활코딩에서 했던 내용을 발전시키는 것으로 방향을 선회하여, 새로운 Topic 모델을 가지고 진행하기로 한다.
"""
