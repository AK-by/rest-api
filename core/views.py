from django.shortcuts import render


def index(request):
    # The main page of project
    return render(
        request=request,
        template_name='core/index.html',
        context={"page_content": "core/content-home.html"},
    )
