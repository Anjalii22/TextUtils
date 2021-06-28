# i have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request ,'index.html')

def analyze(request):

    # to get text
    djtext= request.POST.get("text",'off')

    #check checkbox values
    removepunc = request.POST.get('removepunc','off')
    charcount = request.POST.get('charcount','off')
    caps = request.POST.get('caps','off')
    removeextraspace = request.POST.get('removeextraspace','off')
    newlineremover = request.POST.get('newlineremover','off')

    # check which checkbox is on

    if removepunc == 'on':
           punctuations ='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
           analyzed= ''
           for i in djtext:
              if i not in punctuations:
                  analyzed += i
           new={'purpose':'Removed Punctuations' , 'analyzed_text':analyzed}
           djtext = analyzed


    if charcount== 'on':
        analyzed = len(djtext)
        new = {'purpose': 'Length of Characters', 'analyzed_text': analyzed}
        djtext = analyzed


    if caps=='on':
        analyzed = djtext.upper()
        new = {'purpose': 'Capital Letters', 'analyzed_text': analyzed}
        djtext = analyzed


    if removeextraspace == 'on':
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analyzed+=char
        new = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        djtext = analyzed


    if newlineremover == 'on':
        analyzed=""
        for i in djtext:
            if i != "\n" and i != "\r":
                analyzed += i
        new = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        djtext = analyzed


    if (removepunc != "on" and newlineremover != "on" and removeextraspace != "on" and caps != "on" and charcount != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', new)
