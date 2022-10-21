from django.shortcuts import redirect
from rest_framework.reverse import reverse

from datamanager import settings


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL
        self.open_urls = [self.login_url] + getattr(settings, 'OPEN_URLS', [])

    def __call__(self, request):
        # print(request.user.is_authenticated)
        # print(self.open_urls)
        # print(request.path_info)
        if not request.user.is_authenticated and request.path_info not in self.open_urls:
            return redirect(reverse(self.login_url))
        return self.get_response(request)
