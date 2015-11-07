---
layout: page
title: "Environment Setup"
category: doc
date: 2015-11-06 12:00:00
order: 1
---

###I.1. Update the system

```
~ $ sudo apt-get update -y &> /dev/null
~ $ sudo apt-get upgrade -y &> /dev/null
```

###I.2. Install required packages

```
~ $ sudo apt-get install -y git &> /dev/null
~ $ sudo apt-get install -y libatlas-dev libatlas-base-dev &> /dev/null
~ $ sudo apt-get install -y liblapack-dev gfortran &> /dev/null
```

###I.3. Install azure client

```
~ $ sudo apt-get install -y nodejs-legacy npm &> /dev/null
~ $ sudo npm install -gq azure-cli &> /dev/null
```

###I.4. Install miniconda

```
~ $ cd "$HOME"
~ $ wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh &> /dev/null
~ $ chmod +x miniconda.sh
~ $ bash miniconda.sh -b -p "$HOME/miniconda" &> /dev/null
~ $ PATH="$HOME/miniconda/bin:$PATH"
# Add conda to PATH
~ $ echo 'PATH="$HOME/miniconda/bin:$PATH"' >> "$HOME/.bashrc"
# Update conda
~ $ conda update --yes --quiet conda &> /dev/null
```

###I.5. Install additional conda packages

```
~ $ conda install --yes --quiet jinja2 toolz binstar &> /dev/null
~ $ conda install --yes --quiet pep8 pylint &> /dev/null
```
