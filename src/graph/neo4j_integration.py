# src/graph/neo4j_integration.py
from py2neo import Graph, Node, Relationship
import logging
from src.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

logger = logging.getLogger(__name__)
graph_db = Graph(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def create_patch_and_vulnerability():
    patch_node = Node("Patch", id="Patch_001", vendor="vendorx", product="producta", fixed_version="1.2.3")
    cve_node = Node("Vulnerability", id="CVE-2023-XXXX", severity="High", description="Sample vulnerability")
    
    graph_db.create(patch_node)
    graph_db.create(cve_node)
    
    fixes_rel = Relationship(patch_node, "FIXES", cve_node)
    graph_db.create(fixes_rel)
    
    logger.info("Nodes and relationship created in Neo4j")

if __name__ == "__main__":
    create_patch_and_vulnerability()
