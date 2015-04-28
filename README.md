# bcbio-nextgen-vm - Architecture Proposal

In order to add support for other cloud providers the current architecture of `bcbio-nextgen-vm` must be changed.

##Architecture proposal:
The new module structure is the following:

```
    .
    ├── client
    │   ├── base.py
    │   └── __init__.py
    ├── common
    │   ├── constant.py
    │   ├── exception.py
    │   ├── __init__.py
    │   └── utils.py
    └── provider
        ├── base.py
        └── __init__.py
```
