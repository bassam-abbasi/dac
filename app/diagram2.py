from diagrams import Diagram
from diagrams.generic.network import Router
from diagrams.generic.network import Switch
from diagrams.generic.network import Firewall

with Diagram("Edge topo", show=False, direction="TB"):
    [Router("RTEIDW001"),
                  Switch("L2Switch")] >> Firewall("EdgeFW")
