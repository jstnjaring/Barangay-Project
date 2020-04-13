from django.shortcuts import render
import json
from barangayProject.config import ref
from django.http import *
from django.core.exceptions import *


def save_brgy_announcement(request):
    try:
        data = json.loads(request.body)
        _data = {
            "announcement": {
                "date": data["date"],
                "description": data["description"],
                "user_id": data["user_id"]
            },
            "brgy_name": data["brgy_name"]
        }
        post_announcement = ref.child('barangay')
        post_announcement.push().set(_data)
        return HttpResponse("<html><body>Successfuly Save %s.</body></html>" % _data)

    except:
        if json.decoder.JSONDecodeError:
            raise Http404("There's no Value")
        else:
            raise Http404()


def get_brgy_announcement(request):
    get_announcement = ref.child('barangay')
    return JsonResponse(get_announcement.get())


def update_brgy_announcement(request, _id):
    try:
        data = json.loads(request.body)
        _data = {
            "announcement": {
                "date": data["date"],
                "description": data["description"],
                "user_id": data["user_id"]
            },
            "brgy_name": data["brgy_name"]
        }
        post_announcement = ref.child('barangay')
        post_announcement.child(_id).update(_data)
        return HttpResponse("<html><body>Successfuly Updated ID %s.</body></html>" % _id)
    except:
        raise Http404()


def delete_brgy_announcement(request, _id):
    remove_announcement = ref.child('barangay')
    remove_announcement.child(_id).delete()
    return HttpResponse("<html><body>Successfuly Deleted ID: %s.</body></html>" % _id)
