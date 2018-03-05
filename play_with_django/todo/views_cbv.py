import os

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView


class PostListView1(View):
    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        # html = '''
        #     <h1>Django</h1>
        #     <p>{name}</p>
        #     <p>장고 연습하기: CBV 직접 문자열로</p>
        # '''.format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
            <h1>Django</h1>
            <p>{name}</p>
            <p>장고 연습하기: CBV 직접 문자열로</p>
        '''


post_list1 = PostListView1.as_view()


class PostListView2(TemplateView):
    template_name = 'todo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유 cbv'
        return context


post_list2 = PostListView2.as_view()


class PostListView3(View):
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': False})

    def get_data(self):
        return {
            'message': 'hello, python, django and CBV',
            'items': ['Python', 'Django', 'Celery', 'Azure', 'AWS'],
        }


post_list3 = PostListView3.as_view()


class ExcelDownloadView(View):
    excel_path = os.path.join(settings.BASE_DIR, 'gdplev.xls')

    def get(self, request):
        filename = os.path.basename(self.excel_path)
        with open(self.excel_path, 'rb') as f:
            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachement; filename = "{}"'.format(filename)
            return response
