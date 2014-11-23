# Python Modules
import json


def json_response(func):
    """
    Convierte la respuesta de la funcion en json usando
    la libreria json.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = json.dumps(objects)
            if 'callback' in request.GET:
                data = '%s(%s);' % (request.GET['callback'], data)
        except:
            data = json.dumps(str(objects))
        if 'just_the_json_plz' in kwargs:
            return data
        if 'just_the_data_plz' in kwargs:
            return objects
        if 'callback' in request.GET or 'callback' in request.POST:
            #jsonp
            return HttpResponse(data, "text/javascript")
        else:
            #json
            return HttpResponse(data, "application/json")
    return decorator
