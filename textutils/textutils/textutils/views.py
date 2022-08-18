from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = (request.POST.get('text', 'default'))
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('fullcaps', 'off'))
    newlineremover = (request.POST.get('newlineremover', 'off'))
    extraspaceremover = (request.POST.get('extraspaceremover', 'off'))
    charcount = (request.POST.get('charcount', 'off'))

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover=='on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\n':
                analyzed = analyzed + char
        params = {'purpose': 'Remove newlines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed



    if (charcount=="on"):
        analyzed=''
        count = 0
        for i in djtext:
            count = count + 1
            analyzed =count
        params = {'purpose': 'Character count','count' : 'Total character :','analyzed_text': analyzed}
        

    if (removepunc !="on" and newlineremover != "on" and fullcaps !="on" and extraspaceremover !="on" and charcount !="on"):
        return HttpResponse ("Error,(please select any one check box and try again!!!!")


    return render(request, 'analyze.html', params)

