# src/api/main.py
from fastapi import FastAPI
from py2neo import Graph
from src.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

app = FastAPI()
graph_db = Graph(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

@app.get("/patches/{patch_id}")
def get_patch(patch_id: str):
    query = f"MATCH (p:Patch {{id: '{patch_id}'}}) RETURN p"
    result = graph_db.run(query).data()
    return {"patch": result}

@app.get("/vulnerabilities/{cve_id}")
def get_vulnerability(cve_id: str):
    query = f"MATCH (v:Vulnerability {{id: '{cve_id}'}}) RETURN v"
    result = graph_db.run(query).data()
    return {"vulnerability": result}

# To run the API, use: uvicorn src.api.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)
