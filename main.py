# import pkg_resources
# pkg_resources.resource_filename
from chevron import chevron


with open("resources/templates/hello.html", "r") as f:
    ret = chevron.render(f, {'Title': "Hello"})
    print(ret)
