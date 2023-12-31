from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    # The main page of project
    return render(
        request=request,
        template_name='core/index.html',
        context={"page_content": "core/home.html"},
    )
