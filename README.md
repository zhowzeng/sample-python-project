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

Edit `dependencies` in `pyproject.toml`.

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

## Local Usage

```bash
mygit <command>
```

## Containerization

```bash
# build
docker build -t zhow/mygit --build-arg "GID=$(id -g)" --build-arg "UID=$(id -u)" .
# run command
docker run -it -u $(id -g):$(id -u) --env-file .env zhow/mygit mygit <command>
```
