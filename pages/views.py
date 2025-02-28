from django.views.generic import TemplateView
from django.shortcuts import render


def page_error(request, exception):
    return render(request, "pages/404.html", status=404)
