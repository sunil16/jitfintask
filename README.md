Github Repositorie service Django REST API
===============================
Github Repositorie service is a django application where you can do following operation.
   - Lists all repositories of a user order by most recently created.
   - List all followers of a user sorted by name.
   - Fetch a follower who the highest number of followers.
      e.g: if A, B and C are followers of Sunil and A has 3 followers, B has 5, and C has 2 followers then this API should return details  of B since its as the highest number of followers.
   - Creates a new repository.
   - Update description of a repository.

Django is a high-performance Python framework for building cloud APIs, smart proxies, and app backends. More information can be found [here](https://github.com/django/django).

Requirements
============

Python version : 3
Django minimum version : 1.8
Github Api version : 3

This project uses [virtualenv](https://virtualenv.pypa.io/en/stable/) as isolated Python environment for installation and running. Therefore, [virtualenv](https://virtualenv.pypa.io/en/stable/) must be installed. And you may need a related dependency library for a Project. See [requirements.txt](https://github.com/sunil16/jitfintask/blob/master/requirements.txt) for details.


Installation
============

Install all the python module dependencies in requirements.txt

```sh
$ git clone https://github.com/sunil16/jitfintask.git
$ cd jitfintask
$ pip3 install -r requirements.txt
```

Start server

```
  $ python manage.py runserver
```

Usage
=====

Get Repositories and Followers and top follower
- Request
```
http://localhost:8000/linkdin/get_repo?github_username=sunil16
```

- Response
```json
{
    "message": "success",
    "repository": {
        "repo": [
            {
                "id": 280710758,
                "node_id": "MDEwOlJlcG9zaXRvcnkyODA3MTA3NTg=",
                "name": "jitfintask",
                "full_name": "sunil16/jitfintask",
                "private": false,
                "owner": {
                    "login": "sunil16",
                    "id": 13816959,
                    "node_id": "MDQ6VXNlcjEzODE2OTU5",
                    "avatar_url": "https://avatars3.githubusercontent.com/u/13816959?v=4",
                },
                "html_url": "https://github.com/sunil16/jitfintask",
                ...
            }
            ...
        ],
        "links": {
	    "next": {
                "url": "https://api.github.com/user/1060/repos?sort=created&direction=desc&page=2",
                "rel": "next"
            },
            "last": {
                "url": "https://api.github.com/user/1060/repos?sort=created&direction=desc&page=10",
                "rel": "last"
            }}
    },
    "followers": {
        "followers": [
            {
                "login": "AdiChat",
                "id": 10634210,
                "avatar_url": "https://avatars3.githubusercontent.com/u/10634210?v=4",
                "url": "https://api.github.com/users/AdiChat"
                ...
            },
           ...
        ],
        "links": {
	    "next": {
                "url": "https://api.github.com/user/2894642/followers?page=2",
                "rel": "next"
            },
            "last": {
                "url": "https://api.github.com/user/2894642/followers?page=361",
                "rel": "last"
            }},
        "top_follower": {
            "login": "AdiChat",
            "name": "Aditya I. Chatterjee",
            "public_repos": 20,
            "public_gists": 2,
            "followers": 3074,
            "following": 17396,
            "created_at": "2015-01-21T16:09:21Z",
            "updated_at": "2020-06-25T06:30:47Z"
        }
    }
}
```

Pagination on Followers

- Request
```shell
curl -XPOST http://localhost:8000/linkdin/get_next_page -H "Content-Type: application/json" -d '{
 "follower_paging_url":"https://api.github.com/user/2894642/followers?page=2"
}'
```
- Response
```json
{
    "message": "success",
    "followers": {
        "followers": [
            {
                "login": "AbhiAgarwal",
                "id": 2313562,
                "node_id": "MDQ6VXNlcjIzMTM1NjI=",
                "avatar_url": "https://avatars3.githubusercontent.com/u/2313562?v=4",
                ...
            }
            ...
        ]
    }
     "links": {
            "prev": {
                "url": "https://api.github.com/user/2894642/followers?page=1",
                "rel": "prev"
            },
            "next": {
                "url": "https://api.github.com/user/2894642/followers?page=3",
                "rel": "next"
            },
            "last": {
                "url": "https://api.github.com/user/2894642/followers?page=361",
                "rel": "last"
            },
            "first": {
                "url": "https://api.github.com/user/2894642/followers?page=1",
                "rel": "first"
            }
        },
        "top_follower": {
            "login": "dongweiming",
            "id": 841395,
            "public_repos": 88,
            "public_gists": 31,
            "followers": 3182,
            "following": 96,
            "created_at": "2011-06-10T03:52:00Z",
            "updated_at": "2020-07-08T11:14:48Z"
            ...
        }
    }
}
}
```
Pagination on Repositories
- Request
```shell
curl -XPOST http://localhost:8000/linkdin/get_next_page  -H "Content-Type: application/json" -d '{
  "repo_paging_url":"https://api.github.com/user/1060/repos?sort=created&direction=desc&page=2"
}'
```
- Response
```json
{
    "message": "success",
    "repository": {
        "repos": [
            {
                "id": 2313562,
                "node_id": "MDQ6VXNlcjIzMTM1NjI=",
                ...
            }
            ...
        ]
    }
     "links": {
            "prev": {
                "url": "https://api.github.com/user/2894642/repos?page=1",
                "rel": "prev"
            },
            "next": {
                "url": "https://api.github.com/user/2894642/repos?page=3",
                "rel": "next"
            },
            "last": {
                "url": "https://api.github.com/user/2894642/repos?page=361",
                "rel": "last"
            },
            "first": {
                "url": "https://api.github.com/user/2894642/repos?page=1",
                "rel": "first"
            }
        }
}
```


Create new Repositories
- Request
```shell
curl -XPOST http://localhost:8000/linkdin/create_repo -H "Content-Type: application/json" -d '{
 "name": "NewRepoTest",
  "description": "This is your first repository",
  "private": true,
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true,
  "client_id":"sunil16",
  "client_secret":"*****"
}'
```
- Response
```json
{
    "message": "Repository NewRepoTest successful created"
}
```

Update Repositories Discription

- Request
```shell
curl -XPOST http://localhost:8000/linkdin/update_repo -H "Content-Type: application/json" -d '{
  "name": "NewRepoTest",
  "description": "This is new discription",
  "client_id":"sunil16",
  "client_secret":"*****"
}'
```
- Response
```json
{
    "message": "Repository discription This is new discription from postman update successful"
}
```
