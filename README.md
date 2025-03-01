# Patch Intelligence

## Overview
Patch Intelligence is a system designed to collect, process, and correlate patch information with vulnerabilities. It then exposes that data via a knowledge graph and REST API.

## Project Structure
- **src/**: Source code including modules for data collection, processing, graph integration, API, and scheduling.
- **tests/**: Unit and integration tests.
- **data/**: Folders for raw and processed data.
- **docs/**: Documentation including architecture and API details.
- **Dockerfile** and **docker-compose.yml**: Containerization and deployment configuration.

## Getting Started
1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest`
4. Run the API: `uvicorn src.api.main:app --reload`
5. Run the scheduler: `python src/scheduler/job_scheduler.py`
