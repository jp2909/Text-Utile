#I have created this project - JAYESH PATIDAR

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    dict = {'name':'JAYESH','DOB':'29-09-2000'}
    return render(request,'index.html',dict)
    #return HttpResponse('''<h1>HELLO</h1>''')


def analyze(request):

    djtext = request.POST.get('text','default')


    removepunc = request.POST.get('removepunc','off')
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


    fullcapitilise = request.POST.get('fullcapitilise','off')

    charcount = request.POST.get('charcount','off')

    spaceremover = request.POST.get('spaceremover','off')

    newlineremover = request.POST.get('newlineremover', 'off')

    analyzed =""
    # Remove punctuation
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuation:
               analyzed = analyzed + char
        param = {'purpose': 'remove punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

    # Capitilyse all letter
    if fullcapitilise == 'on':
       analyzed = djtext.upper()
       param = {'purpose1': 'full capitilise', 'analyzed_text': analyzed}
      # return render(request, 'analyze.html', param)
       djtext = analyzed

   # Count character in string
    if charcount == 'on':
        analyzed = len(djtext)
        param = {'purpose2': 'number of charecter in your text', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', param)
        djtext = analyzed

   # space remover
    if spaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not ( djtext[index]==' ' and djtext[index + 1] == ' ' ):
                analyzed += char
        param = {'purpose3': 'remove space', 'analyzed_text': analyzed}
        djtext = analyzed

    # New line remover
    if newlineremover == 'on':
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        param = {'purpose4': 'new line remove', 'analyzed_text': analyzed}


    if(fullcapitilise != 'on' and newlineremover != 'on' and fullcapitilise != 'on' and spaceremover != 'on' and charcount != 'on'):
        return HttpResponse("You do not choose any operation on your data. Please select any operation")


    # Return all perameter
    return render(request , 'analyze.html',param )



