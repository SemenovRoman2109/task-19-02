from django.shortcuts import render,get_object_or_404
from .models import Question,Answer
# Create your views here.

def create_question(request):
    context = dict()
    if request.method == "POST":
        author = request.POST.get("author")
        topic_question = request.POST.get("topic")
        text = request.POST.get("text")
        Question.objects.create(author = author,topic_question = topic_question,text = text)
        context["message"] = "Запитанання створено"
    return render(request,"create_question.html",context=context)

def show_question(request, question_pk):
    context = {
        "question":get_object_or_404(Question,pk=question_pk),
        "list_answers": Answer.objects.filter(question_id=question_pk) 
    }
    if request.method == "POST":
        author = request.POST.get("author")
        text = request.POST.get("text")
        Answer.objects.create(author= author,text=text,question_id=question_pk)
    
    return render(request,'question.html',context=context)
    
def menu(request):
    context = {
        "list_question":Question.objects.all()
    }
    return render(request,"menu.html",context)