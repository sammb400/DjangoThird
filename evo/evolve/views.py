from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .forms import UploadFileForm
from django.http import HttpResponseRedirect, HttpResponse
import mimetypes
import os
from .models import FilesAdmin, Doc

# Create your views here.
def ev(response):
    return render(response, 'evo/index.html', {})



# uploading file through webpage
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



#upload file through admin dashboard
def down(request):
    context = {'file':FilesAdmin.objects.all()}
    return render(request, 'evo/down.html', context)


#download file
def download (request, path):
    file_path =  os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response =  HttpResponse (fh.read(), content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404