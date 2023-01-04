from django.shortcuts import render

# Create your views here.

import functools

from django.http import HttpResponse
from django.template.loader import get_template
from .models import Filament

from weasyprint import HTML


# function to generate pdf using weasyprint
def generate_pdf(request):
    # get the template
    template_name = "label_page.html"
    template = get_template(template_name)
    # render the template
    filaments = Filament.objects.all()
    context = {"filaments": filaments, "offset": 0}
    html = template.render(context)
    # create a pdf
    response = HttpResponse(content_type="application/pdf")
    filename = "label.pdf"
    response["Content-Disposition"] = f"attachment; filename={filename}"
    # find the css
    css = ["staticfiles/css/app.css"]
    # write the pdf using weasyprint
    HTML(string=html).write_pdf(response, stylesheets=css)
    return response


# function based view to list all the filaments
def filament_list(request):
    # get all the filaments
    filaments = Filament.objects.all()
    # render the template
    template_name = "label_page.html"
    context = {"filaments": filaments}
    return render(request, template_name, context)
