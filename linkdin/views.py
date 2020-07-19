from django.shortcuts import render
from django.http import JsonResponse
import json

from .utility import GitUtility

# Create your views here.

def home(request):
    return JsonResponse({"key":"value"})

def get_git_uti_obj():
    return GitUtility()

def repository(request):
    if request.method == 'GET':
        try:
            req_params = request.GET.dict()
            github_username = req_params['github_username']
            if github_username is not None and github_username != '':
                res = get_git_uti_obj().get_repo(github_username)
        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return JsonResponse({'message':res.get('msg'),'data': res.get('data') }, status = res.get('status'))
    else:
        return JsonResponse({'message':"Method Not Allowed"}, status = 405)


def next_page(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            req_params = request.GET.dict()
            paging_url = body['paging_url']
            if paging_url is not None and paging_url != '':
                res = get_git_uti_obj().get_next_repo(paging_url)
        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return JsonResponse({'message':res.get('msg'),'data': res.get('data') }, status = res.get('status'))
    else:
        return JsonResponse({'message':"Method Not Allowed"}, status = 405)
