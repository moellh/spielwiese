# Numerical Operations Library -- NoLib

NoLib is a multipurpose math library for arbitrary math problems, written in
python.

## Building, Installing

```bash
python -m venv venv
source venv/bin/activate
pip install wheel
pip install setuptools
pip install twine
pip install pytest
pip install pytest-runner
python setup.py bdist_wheel
pip install $(find -name "*.whl" | head -n 1)
```

# Testing

```bash
python setup.py pytest
```
