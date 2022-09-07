from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        sentence = request.POST['sentence']
        
        amount_of_words = sentence.split()
        amount_of_words = len(amount_of_words)
       
        return render(request, 'index.html', {'amount_of_words': amount_of_words})
    
    return render(request, 'index.html')