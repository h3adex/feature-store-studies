# Feature Store Studies
In this repository I investigate the functionality of feature stores 
in more detail for my paper in the module Data Engineering

# Dependencies
 - [python3.10+](https://www.python.org/downloads/release/python-3106/)
 - [pipenv](https://pypi.org/project/pipenv/)

# Install Dependencies
```bash
pipenv shell && pipenv install
```

## Create Test-Dataset
```bash
python create_student_osnabrueck.py
```

## Apply features
```bash
cd StudentStore && feast apply
```

## Run Notebooks
```bash
jupyter notebook
```