# XML Runtime Readiness Check

This repository is a small validation harness for the release pipeline. It checks that the pinned XML runtime can be installed in an isolated toolchain and exercised by the project tests.

## Prepare the toolchain

Create a private runtime directory named `.toolchain`:

```bash
python3 -m venv .toolchain
```

Install the pinned runtime package from the repository's local package cache:

```bash
.toolchain/bin/python -m pip install --no-index --find-links .pip-cache -r requirements.txt
```

## Smoke test

Run the project checks from the repository root:

```bash
PYTHONPATH=src .toolchain/bin/python -m unittest discover -s tests
```

## Expected result

The command should finish with one passing test and no test failures. The repository source is separate from the pinned runtime package.
