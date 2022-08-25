from diagrams import Diagram
from diagrams.aws.compute import EC2
import sys
if getattr(sys, 'frozen', False):
    import os
    path = os.environ.get('PATH')
    print("path={}".format(path))
    if path:
         path = path + os.pathsep + sys._MEIPASS
    else:
         path = sys._MEIPASS
    os.environ['PATH'] = path

with Diagram("Network Diagram"):
    EC2("web")
