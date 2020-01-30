from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'hithere' : "blah!"})

def count(request):
    fulltext = request.GET['fulltext']

    wordList = fulltext.split()

    worddictionary = {}

    for word in wordList:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordList), 'worddictionary':worddictionary.items()})
