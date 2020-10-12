from django.shortcuts import HttpResponse

def test(request):
    response = HttpResponse("Here's the text of the Web page.")
    return response
