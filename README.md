# Sample Python Project

## Development

### Installation

```bash
# use virtual environment
python3.10 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -U pip
pip install -r requirements.txt

# editable self installation
pip install -e .

# environment variable
cp .env.copy .env
```

### Adding dependency

Edit `[project]` -> `dependencies` in `pyproject.toml`.

```bash
pip install -e .
# or
pip install <package>
```

### Freezing dependencies

```bash
pip freeze --exclude-editable > requirements.txt
```

### Packaging

```bash
pip install -U build
python -m build
```

## Usage

```bash
my-cli <command>
```

## Containerization

```bash
# build
docker build -t <image-tag> --build-arg "GID=$(id -g)" --build-arg "UID=$(id -u)" .
# run command
docker run -it -u $(id -g):$(id -u) --env-file .env <image-tag> <command>

# run bash for debugging
docker run -it -u $(id -g):$(id -u) --entrypoint bash <image-tag> <command>
```
