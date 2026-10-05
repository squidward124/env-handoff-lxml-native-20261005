# Atlas Release App

Small application package for the Atlas release pipeline.

## Setup

Create a virtual environment and install the pinned dependency:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --no-index --find-links .pip-cache -r requirements.txt
PYTHONPATH=src .venv/bin/python -m unittest discover -s tests
```
