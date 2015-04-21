# bcbio-nextgen-vm - Architecture Proposal

In order to add support for other cloud providers the current architecture of `bcbio-nextgen-vm` must be changed.

##Architecture proposal:

The new module structure is the following:

```
    .
    ├── api.py
    ├── cluster
    │   ├── base.py
    │   ├── elasticluster.py
    │   ├── factory.py
    │   └── __init__.py
    ├── common
    │   ├── constant.py
    │   ├── exception.py
    │   ├── __init__.py
    │   ├── objects.py
    │   └── utils.py
    └── provider
        ├── aws
        │   ├── aws_provider.py
        │   └── __init__.py
        ├── base.py
        ├── factory.py
        └── __init__.py
```

*Note*: For the moment I have added the abstract base classes for `cluster` and `provider`.

###Cluster

###Provider

###Common