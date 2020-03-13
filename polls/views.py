from django.shortcuts import render, get_object_or_404,reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import question, choice

# Create your views here.


def index(req):
    ql = question.objects.all()
    # return HttpResponse("Hello world. You're at the polls index")
    context = {
        "ql": ql
    }
    return render(req, 'polls/index.html', context=context)


def results(req, qid):
    cl = choice.objects.filter(question_id=qid)
    context = {
        "cl": cl,
        "q": question.objects.get(id=qid)
    }
    return render(req, 'polls/results.html', context=context)


def vote(req, qid):
    print(req.POST)
    q = get_object_or_404(question, id=qid)
    print(q.choice_set.all())
    try:
        c = q.choice_set.get(choice_text=(req.POST['choice']))
    except (KeyError):
        return render(req, 'polls/detail.html', {
            'q': q,
            # "You did not select a valid choice",
            'error_message': str(req.POST['choice'])+' not found'
        })
    else:
        print(c)
        print(dir(c))
        c.votes += 1
        c.save()
    return HttpResponseRedirect(reverse('results', args=(qid,)))


def detail(req, qid):
    context = {
        "q": question.objects.get(id=qid)
    }
    return render(req, 'polls/detail.html', context=context)
