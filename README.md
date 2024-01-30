# DD2480_DECIDE
## Setup
```
docker compose up
# delete the container
docker compose down
```

## Docs
To generate documentation, first install dependencies with:
```
pip install -r requirements.txt
```
Then, to generate a PDF, run from the docs/ folder:
```
make latexpdf
```
or
```
.\make.bat latexpdf
```
on Windows platform.
To generate html files, replace latexpdf with html in the last commands.
Generated files are then available in docs/_build/ folder.
