import SOAPpy
def hello():
    return "Hello World"
server = SOAPpy.SOAPServer(("localhost", 8080))
server.config.debug = 1
server.registerFunction(hello)
server.serve_forever()