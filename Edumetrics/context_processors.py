

def renders_processor(request):
    try:
        request.session['base']
    except KeyError:
        request.session['base'] = 'base.html'
    return {}