from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from polls.models import Question, Choice, Comment
from .forms import CommentForm

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    comments = question.comment_set.all()
    new_comment = None
    print("request.method:", request.method)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.question = question
            new_comment.author = request.user
            new_comment.save()
    else: 
        comment_form = CommentForm()
    context = {
        'question': question,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    choices = Question.objects.get(id=question_id).choice_set.all()
    context = {
        'choices': choices,
    }
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

