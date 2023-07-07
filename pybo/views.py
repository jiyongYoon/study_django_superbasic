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