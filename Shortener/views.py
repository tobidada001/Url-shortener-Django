from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .models import ShortenedUrl
from urllib.parse import urlparse
import uuid
# Create your views here.

domain = 'localhost:8000/'

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='index.html')

    def post(self, request, *args, **kwargs):
        url = request.POST['url']
        data = ShortenedUrl.objects.create(url = url, short_url = str(uuid.uuid4())[:8])
        return HttpResponse(domain + data.short_url)


def redirect_to_link(request, part):
    link = get_object_or_404(ShortenedUrl, short_url = part)
    
    parsed = urlparse(link.url)

    if not parsed.scheme:
        scheme = "https" if request.is_secure() else "http"
        return redirect(f'{scheme}://'+ link.url)
    return redirect(link.url)
