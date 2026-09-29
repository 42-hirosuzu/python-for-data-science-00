# ft_package

A sample test package for Python for Data Science - 0, ex09.

## Build

```sh
pip install -r requirements.txt
python -m build
```

## Install

```sh
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```
