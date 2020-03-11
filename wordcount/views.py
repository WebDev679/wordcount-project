from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['words']
    words = text.split()
    length = len(words)
    count_word = {}
    for word in words:
        if word in count_word:
            count_word[word] += 1
        else:
            count_word[word] = 1
    sorted_word_list = sorted(count_word.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'words':text, 'count':length, 'word_list':sorted_word_list})

def about(request):
    return render(request, 'about.html')
