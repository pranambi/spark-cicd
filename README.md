# spark-cicd

A CI/CD pipeline demo for a PySpark word count job using GitHub Actions and Docker.

![CI](https://github.com/pranambi/spark-cicd/actions/workflows/ci.yml/badge.svg)

## Overview

This project demonstrates a real-world CI/CD pattern used in Hadoop/Spark environments:

- **CI** — automatically runs unit tests on every push and pull request to `main`
- **CD** — manually triggered to build and push a versioned Docker image to Docker Hub

## Architecture

```
Feature Branch
      ↓
Pull Request → CI runs pytest automatically
      ↓
Merge to main
      ↓
Human triggers CD (staging / production)
      ↓
Docker image built and pushed to Docker Hub
psnambiar/spark-wordcount:v1.0.YYYYMMDDHHMMSS
```

## Project Structure

```
spark-cicd/
├── job/
│   └── word_count.py          # PySpark word count job
├── tests/
│   └── test_word_count.py     # pytest unit tests
├── Dockerfile                 # Packages job into a Docker image
├── requirements.txt           # PySpark and pytest dependencies
├── pytest.ini                 # pytest path configuration
└── .github/workflows/
    ├── ci.yml                 # CI pipeline — runs on push and PR
    └── cd.yml                 # CD pipeline — manually triggered
```

## CI Pipeline

Triggered automatically on every push and pull request to `main`.

**Steps:**
1. Checkout code
2. Set up Python 3.11
3. Install dependencies (`pip install -r requirements.txt`)
4. Run unit tests (`pytest tests/ -v`)

## CD Pipeline

Manually triggered via **Actions → CD → Run workflow**.

**Design decisions:**
- Restricted to `main` branch only — cannot run on feature branches
- Requires environment selection: `staging` or `production`
- CI already validates code before it reaches `main`, so tests are not duplicated in CD
- Docker image tagged with both a version timestamp and `latest`

**Steps:**
1. Checkout code
2. Log in to Docker Hub using repository secrets
3. Build Docker image
4. Push versioned tag (`v1.0.YYYYMMDDHHMMSS`) and `latest` tag to Docker Hub

## Docker Image

```bash
# Pull and run
docker pull psnambiar/spark-wordcount:latest
docker run psnambiar/spark-wordcount:latest

# Explore inside the container
docker run -it --entrypoint bash psnambiar/spark-wordcount:latest
```

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Run the Spark job directly
python job/word_count.py
```

## Secrets Required

| Secret | Description |
|--------|-------------|
| `DOCKERHUB_USERNAME` | Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub personal access token |
# test
