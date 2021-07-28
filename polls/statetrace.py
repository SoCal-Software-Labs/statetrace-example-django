def action_meta(request):
    return {"my custom action meta": {"arbitary json": 123}}

def session_meta(request):
    return {"my custom session meta": {"some json": 456}}


def filter_func(request):
    return request.method in ["POST"]