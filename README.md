# 🐍 XML to Markdown converter and viceversa

## 🧑‍💻 Install project (Pipenv Required)

### Make

```bash
make setup
```

### Pipenv

```bash
pipenv install --dev
```

## 🚀 Run project

### Make

```bash
make run-local
```

### Pytest

```bash
pipenv run python -m src
```

## 🧪 Tests

### Make

```bash
make tests
```

### Pytest

```bash
pipenv run pytest
```

Run tests with coverage:

```bash
pipenv run pytest --cov
```

## 🎨 Linter

### Make

```bash
make lint
```

### Autopep

```bash
pipenv run autopep8 -i -r ./
```

### Flake

```bash
pipenv run flake8 ./
```

## 📝 Setup project

- ### [Setup python guide](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

- ### [Make manual](https://es.wikipedia.org/wiki/Make)

## 💩 Troubleshooting

- [Setup of the project from 0](https://sourcery.ai/blog/python-best-practices/)
- [Select VSCode Interpreter (modules not found after installation)](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
- [PkgResourcesDeprecationWarning](https://askubuntu.com/questions/1406952/what-is-the-meaning-of-this-pkgresourcesdeprecationwarning-warning-from-pipenv)

## 🧐 References

- [Markdownify](https://pypi.org/project/markdownify/)
