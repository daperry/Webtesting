
application(https://sites-uat.ualberta.ca/~daperry/, 200)

def application(environ, start_response):
    from Flinx.flinx_lib.environ_parse import Environ_Parse

    penv = Environ_Parse(environ)
    # oh my god the syntax
    data = router.route_request(penv)(environ, penv, config, sys_plugins)

    # blah, always return 200 for now.
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
return iter([data])


