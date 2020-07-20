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
                fol_res = get_git_uti_obj().get_followers(github_username)
            else:
                return JsonResponse({'message': "params, github_username missing" }, status = 422)
        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return JsonResponse({'message':res.get('msg'),'repository': res.get('repository'),"followers": fol_res.get('followers')}, status = res.get('status'))
    else:
        return JsonResponse({'message':"Method Not Allowed"}, status = 405)


def next_page(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            paging_url = body['paging_url']
            if paging_url is not None and paging_url != '':
                res = get_git_uti_obj().get_next_repo(paging_url)
            else:
                return JsonResponse({'message': "params, paging_url missing" }, status = 422)
        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return JsonResponse({'message':res.get('msg'),'data': res.get('data') }, status = res.get('status'))
    else:
        return JsonResponse({'message':"Method Not Allowed"}, status = 405)

def create_repo(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            repo_details = json.loads(body_unicode)
            if repo_details is not None:
                res = get_git_uti_obj().add_new_rep(repo_details)
            else:
                return JsonResponse({'message': "params, repo_details missing" }, status = 422)
        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return JsonResponse({'message':res.get('msg')}, status = res.get('status'))
    else:
        return JsonResponse({'message':"Method Not Allowed"}, status = 405)
