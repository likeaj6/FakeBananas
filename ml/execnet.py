# tl;dr to call python2 from a python3 script (& vice vesa)


import execnet

'''
example usage:

result = call_python_version("2.7", "my_module", "my_function", ["Mr", "Bear"])
print(result)

my_module = the name of the folder your code is in
'''

def call_python_version(Version, Module, Function, ArgumentList):
    gw      = execnet.makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec("""
        from %s import %s as the_function
        channel.send(the_function(*channel.receive()))
    """ % (Module, Function))
    channel.send(ArgumentList)
    return channel.receive()

