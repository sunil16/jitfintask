from django.shortcuts import render
from django.http import JsonResponse
import json
from .utility import GitUtility

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
                res['message'] = "params, github_username missing"
                res['status'] = 422
        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return JsonResponse({'message':res.get('msg'),'repository': res.get('repository') if res.get('repository') else {},"followers": fol_res.get('followers') if fol_res.get('followers') else {}}, status = res.get('status'))
    else:
        return JsonResponse({'message':"Method Not Allowed"}, status = 405)

def next_page(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            repo_paging_url = body.get('repo_paging_url')
            follower_paging_url = body.get('follower_paging_url')
            if repo_paging_url is not None and repo_paging_url != '':
                res = get_git_uti_obj().get_next_repo(repo_paging_url)
            elif follower_paging_url is not None and follower_paging_url != '':
                res = get_git_uti_obj().get_next_followers(follower_paging_url)
            else:
                res['message'] = "params missing"
                res['status'] = 422
        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return JsonResponse({'message':res.get('msg'), 'repository': res.get('repository') if res.get('repository') else {},"followers": res.get('followers') if res.get('followers') else {} }, status = res.get('status'))
    else:
        if request.method == 'OPTIONS':
            return JsonResponse({"Content-Type": "application/json"}, status = 200)
        return JsonResponse({'message':"Method Not Allowed"}, status = 405)

def create_repo(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            repo_details = json.loads(body_unicode)
            if repo_details is not None:
                res = get_git_uti_obj().add_new_rep(repo_details)
            else:
                res['message'] = "params, paging_url missing"
                res['status'] = 422
        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return JsonResponse({'message':res.get('msg')}, status = res.get('status'))
    else:
        if request.method == 'OPTIONS':
            return JsonResponse({"Content-Type": "application/json"}, status = 200)
        return JsonResponse({'message':"Method Not Allowed"}, status = 405)

def update_repo(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            repo_details = json.loads(body_unicode)
            if repo_details is not None:
                res = get_git_uti_obj().update_repo(repo_details)
            else:
                res['message'] = "params, paging_url missing"
                res['status'] = 422
        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return JsonResponse({'message':res.get('msg')}, status = res.get('status'))
    else:
        if request.method == 'OPTIONS':
            return JsonResponse({"Content-Type": "application/json"}, status = 200)
        return JsonResponse({'message':"Method Not Allowed"}, status = 405)
