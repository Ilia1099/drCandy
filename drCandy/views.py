from django.views.generic.base import View
from django.shortcuts import HttpResponse


class MainPageView(View):
    def get(self, request):
        return HttpResponse("Main page")
