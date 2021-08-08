from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import mimetypes


# Create your views here.
def ev(response):
    return render(response, 'evo/index.html', {})


def some_view(request):
    #create bytestream buffer
    buffer = io.BytesIO()
    #create canvas
    p = canvas.Canvas(buffer, pagesize=letter)
    #create text object
    p.drawString(100,500, "Doc exercise")
    #finish up
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='receipts.pdf')


def upload(response):
    return render(response, 'evo/uploadin.html', {})


# uploading file
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'evo/upload.html', {'form': form})


#handle uploaded file
def handle_uploaded_file(f):
    with open('cv.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



