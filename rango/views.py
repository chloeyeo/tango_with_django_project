from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to sent to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, "rango/index.html", context=context_dict)

    # The render function takes as input user's request, the template filename,
    # and the context dictionary; then combine these data together with the template
    # to produce a complete HTML page that is returned with a HttpResponse.
    # This response is then returned and dispatched to the user's web browser.

def about(request):
    context_dict = {"boldmessage": "This tutorial has been put together by Chloe Yeo."}
    return render(request, "rango/about.html", context=context_dict)
