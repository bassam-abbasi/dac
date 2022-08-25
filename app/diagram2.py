from diagrams import Diagram,Cluster
from diagrams.generic.network import Router
from diagrams.generic.network import Switch
from diagrams.generic.network import Firewall

with Diagram("Edge topo", show=False, direction="TB"):
    with Cluster("Data Center"):
        Router("BL1")
        Router("BL2")

    with Cluster("DC Edge"):
        Router("DCI1")
        Router("DCI2")
