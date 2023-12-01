from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from .Four import create_video as vid
from wsgiref.util import FileWrapper
from .models import VideoRequest
import mimetypes
import os

def index(request):
	return HttpResponse("<h1>Введите текст в url-строку</h1>")


def runtex(request):
	input_text = request.GET.get('text', 'Default Text')
	file = vid(input_text)
	#сохранение в БД
	video_request = VideoRequest(text=input_text)
	video_request.save()

	chunk_size = 8192
	response = StreamingHttpResponse(FileWrapper(open(file, 'rb'), chunk_size), content_type=mimetypes.guess_type(file)[0])
	response['Content-Length'] = os.path.getsize(file)
	response['Content-Disposition'] = "attachment; filename=%s" % file

	return response

def bd(request): 
	pass