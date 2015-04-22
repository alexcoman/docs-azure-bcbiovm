# bcbio-nextgen-vm - Architecture Proposal

In order to add support for other cloud providers the current architecture of `bcbio-nextgen-vm` must be changed.

##Architecture proposal:
The new module structure is the following:

```
    .
    ├── api.py
    ├── client
    │   ├── __init__.py
    │   ├── parser.py
    │   └── utils.py
    ├── cluster
    │   ├── base.py
    │   ├── elasticluster.py
    │   ├── factory.py
    │   └── __init__.py
    ├── common
    │   ├── constant.py
    │   ├── exception.py
    │   ├── __init__.py
    │   ├── objects.py
    │   └── utils.py
    ├── provider
    │   ├── aws
    │   │   ├── aws_provider.py
    │   │   └── __init__.py
    │   ├── base.py
    │   ├── factory.py
    │   └── __init__.py
    └── worker
        ├── base.py
        ├── docker
        │   ├── docker_worker.py
        │   └── __init__.py
        ├── factory.py
        └── __init__.py
```
