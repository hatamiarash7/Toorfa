from __future__ import unicode_literals

import datetime

import os
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from hazm import *

from .models import *


def index(request):
    """
    show a simple parsed text
    :param request: None
    :return: parsed string
    """
    normalizer = Normalizer()
    a = normalizer.normalize('اصلاح نويسه ها و استفاده از نیم‌فاصله پردازش را آسان مي كند')
    tokens = word_tokenize(a)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, 'bot/resources')
    tagger = POSTagger(model=path + '/postagger.model')
    tags = tagger.tag(tokens)
    output = ""
    for token in tags:
        output += "[" + token[0] + "-" + token[1] + "]"
    template = loader.get_template('index.html')
    context = {
        'tags': output,
    }
    return HttpResponse(template.render(context, request))


def chat(request):
    """
    show list of all messages
    :param request: None
    :return: messages from db
    """
    msg_list = Message.objects.order_by('-date')
    template = loader.get_template('chat.html')
    context = {
        'msg_list': msg_list,
    }
    return HttpResponse(template.render(context, request))


def chat2():
    """
        show list of all messages
        :param request: None
        :return: messages from db
        """
    msg_list = Message.objects.order_by('-date')
    template = loader.get_template('chat.html')
    context = {
        'msg_list': msg_list,
    }
    return HttpResponse(template.render(context))


def get_msg(request):
    """
    get message from user and save messages to database
    :param request: input message ( body )
    :return: redirect
    """
    msg = request.POST['body']

    author_message = Message.objects.create(
        body=msg,
        date=datetime.datetime.today(),
        author_id=1
    )

    if msg == "سلام" or msg == "درود":
        Message.objects.create(
            body="سلام",
            date=datetime.datetime.today(),
            author_id=2
        )
    elif msg == "چطوری ؟" or msg == "حالت خوبه ؟" or msg == "خوبی ؟" or msg == "حالت چطوره ؟" or \
                    msg == "آیا حالتان خوب است ؟" or msg == "آیا حال شما خوب است ؟" or \
                    msg == "حالتان خوب است ؟" or msg == "حال شما خوب است ؟" or \
                    msg == "حالتان چگونه است ؟" or msg == "حالتان چطور است ؟" or \
                    msg == "حالت خوب است ؟" or msg == "حالتون خوبه ؟" or \
                    msg == "حالتون چطوره ؟" or msg == "حالتون چطور است ؟" or \
                    msg == "حالتون چگونه است ؟" or msg == "آیا حالتون خوبه ؟":
        Message.objects.create(
            body="خوبم. تشکر",
            date=datetime.datetime.today(),
            author_id=2
        )
    elif msg == "چه خبر ؟" or msg == "چه خبرا ؟" or msg == "چه میکنی ؟" or msg == "چه می کنی ؟":
        Message.objects.create(
            body="هیچی. سلامتی",
            date=datetime.datetime.today(),
            author_id=2
        )
    elif msg == "جدا ؟" or msg == "واقعا ؟" or msg == "جدی ؟" or msg == "راست میگی ؟":
        Message.objects.create(
            body="بله",
            date=datetime.datetime.today(),
            author_id=2
        )
    elif msg == "آها" or msg == "بله" or msg == "خوب" or msg == "اهوم" or msg == "اوهوم" or msg == "چه خوب" or msg == "که اینطور" or \
                    msg == "عالی" or msg == "آره" or msg == "عجب" or msg == "چه عجب" or msg == "چه جالب" or msg == "درسته" or msg == "موافقم" or \
                    msg == "همینطوره" or msg == "همینطور است" or msg == "چرا که نه" or msg == "مخالفم" or \
                    msg == "اینطور نیست" or msg == "نه" or msg == "نمیدونم" or msg == "نمی دونم" or msg == "میدونم" or \
                    msg == "می دانم" or msg == "نمیدانم" or msg == "نمی دانم" or msg == "چه میدونم" or msg == "چه می دونم" or \
                    msg == "چه میدانم" or msg == "چه می دانم" or msg == "باشه" or msg == "حله" or msg == "خوبه" or \
                    msg == "عالیه" or msg == "آفرین" or msg == "احسنت" or msg == "باریکلا" or msg == "امیدوارم" or msg == "انشالله" or \
                    msg == "ایشالا" or msg == "ممنون" or msg == "تشکر" or msg == "خواهش" or msg == "خواهش میکنم" or msg == "تشکر میکنم" or \
                    msg == "خواهش می کنم" or msg == "تشکر می کنم" or msg == "متشکرم" or msg == "مچکرم" or msg == "سپاسگزارم" or\
                    msg=="خب" or msg=="خب دیگه":
        pass
    elif msg == "خداحافظ" or msg == "بدرود" or msg == "بای" or msg == "خدانگهدار" or msg == "خدا نگهدار":
        Message.objects.create(
            body="به امید دیدار",
            date=datetime.datetime.today(),
            author_id=2
        )
    elif msg=="کاری نداری ؟" or msg=="کاری ندارید ؟" or msg=="آیا کاری نداری ؟" or msg=="آیا کاری ندارید ؟" \
            or msg=="آیا با من کاری نداری ؟" or msg== "آیا با من کاری ندارید ؟" or msg=="با من کاری نداری ؟" or \
            msg == "با من کاری ندارید ؟" or msg=="امری نیست ؟":
        Message.objects.create(
            body="خیر. سلامت باشید",
            date=datetime.datetime.today(),
            author_id=2
        )
    else:
        output = get_response2(msg)
        if output is None: output = "نی دونم"
        if output != -1:
            bot_message = Message.objects.create(
                body=output,
                date=datetime.datetime.today(),
                author_id=2
            )

    return HttpResponseRedirect('/bot/chat')


def get_response(text):
    """
    get input text and parse it
    :param text: input text by user
    :return: parsed string
    """
    normalizer = Normalizer()
    a = normalizer.normalize(text)
    tokens = word_tokenize(a)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, 'bot/resources')
    tagger = POSTagger(model=path + '/postagger.model')
    tagged = tagger.tag(tokens)
    chunker = Chunker(model=path + '/chunker.model')
    chunks = tree2brackets(chunker.parse(tagged))

    final = ""
    for token in chunks:
        if 65 <= ord(token) <= 90:
            final += token
        if ord(token) == 32:
            final += "*"
    final = final[1:].split('**')
    result = chunks.split('] [')
    s = ""
    for r in result:
        s += '*' + r.split(' ')[0]
    result = s[2:].split('*')

    if ord(text[-1:]) == 1567 or ord(text[-1:]) == 63:
        return find_answer(final, result)
    else:
        add_to_db(final, result)
        return -1


def get_response2(text):
    text = text.replace("چیست", "چه چیزی است")
    text = text.replace("کیست", "چه کسی است")
    text = text.replace("کجاست", "چه مکانی است")
    text = text.replace("چطور", "چه حالتی")
    text = text.replace("چگونه", "چه حالتی")
    normalizer = Normalizer()
    a = normalizer.normalize(text)
    tokens = word_tokenize(a)
    temp = ""
    # for check there is special delimeter
    counter = 0
    for pos, token in enumerate(tokens):
        if len(token) == 1:
            if ord(token) == 1608:
                counter += 1
                temp += "#"
        else:
            temp += " " + token
    temp = temp.replace("# ", "#")
    tokens = word_tokenize(temp)
    replaces = {
        "شما": "من",
        "تو": "من",
        "من": "شما",
        "اسم": "نام",
        "اسمتان": "نامتان",
        "اسمت": "نامت",
        "شد": "است"
    }
    tokens = [replaces.get(n, n) for n in tokens]
    if ord(text[-1:]) == 1567 or ord(text[-1:]) == 63:
        return find_answer2(tokens)
    else:
        a = {}
        for i in range(0, len(tokens)):
            a['T%s' % str(i + 1)] = tokens[i]
        Sentence.objects.create(Count=len(tokens), **a)
    return -1


def delete_messages(request):
    """
    delete all messages
    :param request: None
    :return: None
    """
    Message.objects.all().delete()
    S2P.objects.all().delete()
    S3P.objects.all().delete()
    Sentence.objects.all().delete()
    return HttpResponseRedirect('/bot/chat')


def add_to_db(structure, content):
    if len(structure) == 2:
        S2P.objects.create(NP=content[0], VP=content[1])
    if len(structure) == 3:
        S3P.objects.create(NP=content[0], ADJP=content[1], VP=content[2])


def find_answer(structure, content):
    answer = ""
    if len(structure) == 2:
        l = S2P.objects.filter(VP=content[1])
        for t in l:
            answer += t.NP
    return answer


def find_answer2(tokens):
    if "چه" in tokens:
        tokens.remove("چه")
        le = len(tokens)
        list = Sentence.objects.filter(Count=le)
        list2 = Sentence.objects.filter(Count=le + 1)

        answer = None

        for l in list:
            counter = 0
            for i in range(0, le):
                if tokens[i] == l.T1: counter += 1
                if tokens[i] == l.T2: counter += 1
                if tokens[i] == l.T3: counter += 1
                if tokens[i] == l.T4: counter += 1
                if tokens[i] == l.T5: counter += 1
                if tokens[i] == l.T6: counter += 1
                if tokens[i] == l.T7: counter += 1
                if tokens[i] == l.T8: counter += 1
                if tokens[i] == l.T9: counter += 1
                if tokens[i] == l.T10: counter += 1
                if tokens[i] == l.T11: counter += 1
                if tokens[i] == l.T12: counter += 1
                if tokens[i] == l.T13: counter += 1
                if tokens[i] == l.T14: counter += 1
                if tokens[i] == l.T15: counter += 1
                if tokens[i] == l.T16: counter += 1
                if tokens[i] == l.T17: counter += 1
                if tokens[i] == l.T18: counter += 1
                if tokens[i] == l.T19: counter += 1
                if tokens[i] == l.T20: counter += 1

                if counter == l.Count - 1: answer = l
                # print("L " + str(l.id) + ":" + str(counter) + " - " + str(l.Count))

        for l2 in list2:
            counter2 = 0
            for i in range(0, le):
                if tokens[i] == l2.T1: counter2 += 1
                if tokens[i] == l2.T2: counter2 += 1
                if tokens[i] == l2.T3: counter2 += 1
                if tokens[i] == l2.T4: counter2 += 1
                if tokens[i] == l2.T5: counter2 += 1
                if tokens[i] == l2.T6: counter2 += 1
                if tokens[i] == l2.T7: counter2 += 1
                if tokens[i] == l2.T8: counter2 += 1
                if tokens[i] == l2.T9: counter2 += 1
                if tokens[i] == l2.T10: counter2 += 1
                if tokens[i] == l2.T11: counter2 += 1
                if tokens[i] == l2.T12: counter2 += 1
                if tokens[i] == l2.T13: counter2 += 1
                if tokens[i] == l2.T14: counter2 += 1
                if tokens[i] == l2.T15: counter2 += 1
                if tokens[i] == l2.T16: counter2 += 1
                if tokens[i] == l2.T17: counter2 += 1
                if tokens[i] == l2.T18: counter2 += 1
                if tokens[i] == l2.T19: counter2 += 1
                if tokens[i] == l2.T20: counter2 += 1

                if counter2 == l2.Count - 2: answer = l2
                # print("L " + str(l2.id) + ":" + str(counter2) + " - " + str(l2.Count))
        if answer is None:
            answer = "نمی دونم"
        else:
            answer = answer.get()
        return answer

    else:
        if "آیا" in tokens: tokens.remove("آیا")
        le = len(tokens)
        list = Sentence.objects.filter(Count=le)

        answer = None
        counter = 0
        for l in list:
            counter = 0
            for i in range(0, le):
                if tokens[i] == l.T1: counter += 1
                if tokens[i] == l.T2: counter += 1
                if tokens[i] == l.T3: counter += 1
                if tokens[i] == l.T4: counter += 1
                if tokens[i] == l.T5: counter += 1
                if tokens[i] == l.T6: counter += 1
                if tokens[i] == l.T7: counter += 1
                if tokens[i] == l.T8: counter += 1
                if tokens[i] == l.T9: counter += 1
                if tokens[i] == l.T10: counter += 1
                if tokens[i] == l.T11: counter += 1
                if tokens[i] == l.T12: counter += 1
                if tokens[i] == l.T13: counter += 1
                if tokens[i] == l.T14: counter += 1
                if tokens[i] == l.T15: counter += 1
                if tokens[i] == l.T16: counter += 1
                if tokens[i] == l.T17: counter += 1
                if tokens[i] == l.T18: counter += 1
                if tokens[i] == l.T19: counter += 1
                if tokens[i] == l.T20: counter += 1

                if counter == l.Count:
                    answer = "بله"
                elif counter == l.Count - 1:
                    answer = "خیر"
                else:
                    answer = "نمی دونم"
        return answer
