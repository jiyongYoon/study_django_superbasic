from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

count = 0
routing_count = 0
view_count = 0
model_count = 0
topics = [
    {'id':1, 'title':'routing', 'body': 'Routing is ...'},
    {'id':2, 'title':'view', 'body': 'View is ...'},
    {'id':3, 'title':'Model', 'body': 'Model is ...'}
]

def HTMLTemplate(articleTag, id=None):
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''

def index(request):
    global topics
    global count
    count += 1
    article = f'''
    <h2> Welcome </h2>
        Hello, <br>
    I'm django <br>
    count: {count}
    '''
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')

@csrf_exempt
def read(request, id):
        global topics
        article = ''
        for topic in topics:
            if topic['id'] == int(id):
                article = f'''
                <h2>{topic["title"]}</h2>
                {topic["body"]} <br>
                <form action="/delete/" method="post">
                    <p><input type="hidden" name="id" value={id}></p>
                    <p><input type="submit" value="삭제"></p>
                </form>
                <li>
                    <a href="/update/{id}">update</a>
                </li>
                '''
        return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        global topics
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": len(topics) + 1, "title":title, "body":body}
        topics.append(newTopic)
        return redirect('/read/' + str(len(topics)))

@csrf_exempt
def update(request, id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                findTopic = {
                    "title":topic['title'],
                    "body":topic['body']
                }
        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={findTopic["title"]}></p>
                <p><textarea name="body" placeholder="body">{findTopic["body"]}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')


###############################################################

from .models import Question


def index(request):
    question_list = Question.objects.order_by('-create_date') # - 가 붙어있으면 역순 정렬
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

"""
render 함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수.
위 index 함수는 question_list 데이터를 'pybo/question_list.html' 파일에 적용하여 HTML을 생성한 후 리턴한다.

점프 투 장고에 있는 모델을 활용하지 않고, 기존에 생활코딩에서 했던 내용을 발전시키는 것으로 방향을 선회하여, 새로운 Topic 모델을 가지고 진행하기로 한다.
"""
