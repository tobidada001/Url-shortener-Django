from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from .models import ShortenedUrl
from urllib.parse import urlparse
import uuid
# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='index.html')

    def post(self, request, *args, **kwargs):
        url = request.POST.get('url')
        if url:
            data = ShortenedUrl.objects.create(url = url, short_url = str(uuid.uuid4())[:8])
            print(str(get_current_site(request)) + data.short_url)
            return HttpResponse(str(get_current_site(request)) +'/'+ data.short_url)
        else:
            return JsonResponse({ 'error' : 'Url field must not be empty.'})


def redirect_to_link(request, part):
    link = get_object_or_404(ShortenedUrl, short_url = part)
    
    parsed = urlparse(link.url)

    if not parsed.scheme:
        scheme = "https" if request.is_secure() else "http"
        return redirect(f'{scheme}://'+ link.url)
    return redirect(link.url)
