"""
Shared constants across the bcbio-nextgen-vm project.
"""


class DEFAULT:

    CLUSTER_MANAGER = 'Elasticluster'
    CLOUD_PROVIDER = 'AWS'


class LOG:

    NAME = "bcbiovm"
    LEVEL = 10
    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    FILE = ""
