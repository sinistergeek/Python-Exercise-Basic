SCRIPT_MAP = {
    'demo':demo_app,
    'static':static_app,
    'index.html':welcome_app,
}

def routing(environ,start_response):
    top_level = wsgiref.util.shift_path_info(environ)
    app = SCRIPT_MAP.get(top_level,welcome_app)
    content = app(environ,start_response)
    return content
