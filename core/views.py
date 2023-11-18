from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/sign-in/")
def index(request):
    # The main page of project
    return render(
        request=request,
        template_name='core/index.html',
    )
