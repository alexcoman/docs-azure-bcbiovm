# bcbio-nextgen-vm - Architecture Proposal

In order to add support for other cloud providers the current architecture of `bcbio-nextgen-vm` must be changed.

##Architecture proposal:
The new module structure is the following:

```
    .
    ├── client
    │   ├── __init__.py
    │   ├── parser.py
    │   └── utils.py
    ├── common
    │   ├── constant.py
    │   ├── exception.py
    │   ├── __init__.py
    │   ├── objects.py
    │   └── utils.py
    └── provider
        ├── aws
        │   ├── aws_provider.py
        │   └── __init__.py
        ├── base.py
        ├── factory.py
        └── __init__.py
```
