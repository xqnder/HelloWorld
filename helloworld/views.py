from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'HelloWorld'}


@view_config(route_name='helloworld', renderer='templates/helloworld.pt')
def my_view(request):
    return {'message': 'Hello cruel world!'}