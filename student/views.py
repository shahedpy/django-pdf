# DJANGO IMPORTS
from django.views.generic import View
from django.template.loader import get_template
from django.http import HttpResponse

# THIRD PARTY IMPORTS
from weasyprint import HTML

# MODELS IMPORTS
from .models import Student


class StudentView(View):

    def get(self, request, *args, **kwargs):
        template = get_template('student/student.html')
        context = {
            'students': Student.objects.all()
        }
        html = template.render(context)
        pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf() # noqa
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'filename=nothi_letter.pdf'
        return response
