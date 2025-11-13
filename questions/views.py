from django.shortcuts import render
from django.views import View

MOCK_QUESTIONS = [
    {
        "id": 1,
        "count": 15,
        "answers": 8,
        "views": 24,
        "text": "How to center a div with CSS?",
        "description": "I've been trying to center a div both horizontally and vertically but nothing seems to work. I've tried display: flex, position: absolute, and transform methods..."
    },
    {
        "id": 2,
        "votes": 42,
        "answers": 15,
        "views": 356,
        "text": "What is the difference between let and var in JavaScript?",
        "description": "I'm learning JavaScript and confused about when to use let vs var. Can someone explain the key differences with examples?"
    },
    {
        "id": 3,
        "votes": 3,
        "answers": 0,
        "views": 45,
        "text": "Django model relationships - ForeignKey vs OneToOneField",
        "description": "When should I use ForeignKey and when should I use OneToOneField in Django models? What are the performance implications?"
    },
]


# Create your views here.
class IndexView(View):
    def get(self, request, **args):
        return render(request, "index.html", context={"question_list": MOCK_QUESTIONS})