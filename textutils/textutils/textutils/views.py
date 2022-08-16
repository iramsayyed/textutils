from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = (request.GET.get('text', 'default'))
    removepunc = (request.GET.get('removepunc', 'off'))
    fullcaps = (request.GET.get('fullcaps', 'off'))
    newlineremover = (request.GET.get('newlineremover', 'off'))
    extraspaceremover = (request.GET.get('extraspaceremover', 'off'))
    charcount = (request.GET.get('charcount', 'off'))

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)

    elif fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)

    elif(newlineremover=='on'):
        analyzed = ''
        for char in djtext:
            if char != '/n':
                analyzed = analyzed + char
        params = {'purpose': 'Remove newlines', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (charcount=="on"):
        analyzed=''
        count = 0
        for i in djtext:
            count = count + 1
            analyzed =count
        params = {'purpose': 'Character count','count' : 'Total character :','analyzed_text': analyzed}
        return render(request, 'analyze.html', params)






    else:
        return HttpResponse("Error,[please select any one check box]",)

# def capfirst(request):
#     return HttpResponse("capfirst")
#
# def newlineremove(request):
#     return HttpResponse("new line")
#
# def spaceremove(request):
#     return HttpResponse("space remove")
#
# def charcount(request):
#     return HttpResponse("character count")
