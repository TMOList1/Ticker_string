from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from .Four import create_video as vid
from wsgiref.util import FileWrapper
import mimetypes
import os

def index(request):
	return HttpResponse("<h1>Введите текст в url-строку</h1>")
# Create your views here.

# def runtex_video(request):
# 	# runtex_video(request)

# 	return HttpResponse("<h4>Пспс</h4>")



def runtex(request):
	# runtex_video(request)
	input_text = request.GET.get('text', 'Default Text')

	file = vid(input_text)

	chunk_size = 8192
	print(file)

	response = StreamingHttpResponse(FileWrapper(open(file, 'rb'), chunk_size), content_type=mimetypes.guess_type(file)[0])
	response['Content-Length'] = os.path.getsize(file)
	response['Content-Disposition'] = "attachment; filename=%s" % file

	return response
