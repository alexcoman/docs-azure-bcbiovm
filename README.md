# bcbio-nextgen-vm - Architecture Proposal

In order to add support for other cloud providers the current architecture of `bcbio-nextgen-vm` must be changed.

##Architecture proposal:

The new module structure is the following:
```
    bcbiovm
    ├── client
    │   ├── base.py
    │   ├── commands.py
    │   ├── __init__.py
    │   └── subcommands
    │       ├── aws.py
    │       ├── azure.py
    │       ├── cluster.py
    │       ├── config.py
    │       ├── docker.py
    │       ├── factory.py
    │       ├── icel.py
    │       ├── __init__.py
    │       └── ipython.py
    ├── common
    │   ├── cluster.py
    │   ├── constant.py
    │   ├── exception.py
    │   ├── __init__.py
    │   ├── objects.py
    │   ├── objectstore.py
    │   └── utils.py
    ├── docker
    │   ├── defaults.py
    │   ├── devel.py
    │   ├── __init__.py
    │   ├── install.py
    │   ├── ipythontasks.py
    │   ├── manage.py
    │   ├── mounts.py
    │   ├── multitasks.py
    │   ├── remap.py
    │   └── run.py
    ├── __init__.py
    ├── ipython
    │   ├── batchprep.py
    │   └── __init__.py
    └── provider
        ├── aws
        │   ├── aws_provider.py
        │   ├── bootstrap.py
        │   ├── clusterk
        │   │   ├── clusterktasks.py
        │   │   ├── __init__.py
        │   │   ├── main.py
        │   │   └── multitasks.py
        │   ├── iam.py
        │   ├── icel.py
        │   ├── __init__.py
        │   ├── resources.py
        │   ├── ship.py
        │   └── vpc.py
        ├── azure
        │   ├── azure_provider.py
        │   ├── bootstrap.py
        │   ├── __init__.py
        │   └── ship.py
        ├── base.py
        ├── factory.py
        ├── __init__.py
        ├── playbook.py
        └── ship.py
```

The implementation of this architecture can be found [here](https://github.com/alexandrucoman/bcbio-nextgen-vm/).
