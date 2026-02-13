from django.shortcuts import render
from django.http import HttpResponse

# def sh(request):
#     return HttpResponse("hii")

# def clr(reuqest):
#     return render(reuqest,'index.html')


from django.shortcuts import render
import random

# Home page
def home(request):
    return render(request, 'home.html')

# Memories page
def memories(request):
    return render(request, 'memories.html')

# Love Notes page
def love_notes(request):
    notes = [
        "You make me smile every day 😊",
        "You are my favorite hello and hardest goodbye 💕",
        "Together, we can do anything 🌟",
        "Love you to the moon and back 🌙💖",
        "My heart beats for you 💗",
        "You + Me = Forever 🥰"
    ]
    random_note = random.choice(notes)
    return render(request, 'love_notes.html', {'note': random_note})

# Valentine page
def valentine(request):
    return render(request, 'valentine.html')


