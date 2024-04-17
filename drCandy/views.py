from django.views.generic.base import View
from django.shortcuts import render


class MainPageView(View):
    def get(self, request):
        return render(request, 'main_page/main_page.html')
