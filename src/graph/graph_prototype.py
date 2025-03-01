# src/graph/graph_prototype.py
import networkx as nx
import logging

logger = logging.getLogger(__name__)

def create_prototype_graph():
    G = nx.DiGraph()
    # Add a patch node
    patch_node_id = "Patch_001"
    G.add_node(patch_node_id, vendor="vendorx", product="producta", fixed_version="1.2.3")
    
    # Add a vulnerability node
    cve_node_id = "CVE-2023-XXXX"
    G.add_node(cve_node_id, severity="High", description="Sample vulnerability")
    
    # Create an edge indicating that the patch fixes the vulnerability
    G.add_edge(patch_node_id, cve_node_id, relation="FIXES")
    
    return G

if __name__ == "__main__":
    G = create_prototype_graph()
    for source, target, data in G.edges(data=True):
        logger.info(f"Edge from {source} to {target} with relation {data.get('relation')}")
    print("Nodes:", G.nodes(data=True))
