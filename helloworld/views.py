from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/default_pyramid_template.pt')
def default_pyramid_view(request):
    return {'project': 'HelloWorld'}


@view_config(route_name='helloworld', renderer='templates/helloworld.pt')
def hello_world_view(request):
    return {
        'request': request,
        'message': 'Hello cruel world!'
    }