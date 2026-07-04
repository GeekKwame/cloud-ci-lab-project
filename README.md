# Cloud CI Lab Project

A simple Python application with an automated CI/CD pipeline built using **GitHub Actions**.

🔗 Repo: https://github.com/GeekKwame/cloud-ci-lab-project

## Overview

This project simulates how cloud engineering teams validate code changes before deployment.
`app.py` is a minimal cloud service that prints `Cloud CI Pipeline Running`. A test script
(`test_app.py`) confirms the app runs correctly. Every time code is pushed to the repository,
GitHub Actions automatically builds and tests the app — no manual steps required.

This follows **GitOps** principles: the pipeline itself is defined as code
(`.github/workflows/ci.yml`) and version-controlled alongside the application.

## What the Pipeline Does

On every `push` (and pull request) to `main`, the workflow:

1. Checks out the repository code
2. Sets up the Python runtime
3. Prints the runtime version
4. Runs the application (`app.py`)
5. Runs the test suite (`test_app.py`)
6. Prints a build success message

See the full pipeline definition here: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

## Running Locally

```bash
python app.py
python test_app.py
```

## Pipeline Status

Live pipeline runs can be viewed under the repository's **Actions** tab:
https://github.com/GeekKwame/cloud-ci-lab-project/actions

## Project Journey

- ✅ Built and structured the repository
- ✅ Created the cloud app and test script
- ✅ Wrote and committed the GitHub Actions workflow
- ✅ Verified a successful pipeline run
- ✅ Intentionally broke the pipeline, confirmed it failed, then fixed and re-verified it
- ✅ Extended the pipeline with additional steps

## What This Pipeline Automates

This pipeline automates build verification and testing on every push, catching broken code
before it can be merged or deployed — removing the need to manually run and test the app
after every change.

---
*Built as part of the Azubi Africa Cloud Engineering program — Week 9 CI/CD Practical Lab.*