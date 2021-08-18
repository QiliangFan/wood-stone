from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, JsonResponse
# Create your views here.

class SeriesView(View):

    def get(self, request: HttpRequest):
        """ 获取指定范围内的序列, 如果start或者end为None, 表示无边界
        :param request:
            {
                "name": required,
                "start": optional,
                "end": optional,
            }
        :return:
        """
        name: str = request.GET.get("name")
        start_time: int = request.GET.get("start")
        end_time: int =request.GET.get("end")

    def options(self, request: HttpRequest):
        """ 处理跨域时的OPTIONS请求
        :param request:
        :return:
        """
        return JsonResponse({
            "status": 200
        })