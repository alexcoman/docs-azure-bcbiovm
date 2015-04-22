"""
Worker base-classes:
    (Beginning of) the contract that workers must follow.
"""


class BaseWorker(object):

    """
    Base class for workers.

    Attributes:
        :CLOUD_PROVIDER:    if it is set, the API will use this worker only
                            if the required cloud provider is used
        :CLUSTER_MANAGER:   if it is set, the API will use this worker only
                            if the required cluster manager is used
    """

    CLOUD_PROVIDER = None
    CLUSTER_MANAGER = None

    def __init__(self):
        self._name = self.__class__.__name__
        self._cloud_provider = self.CLOUD_PROVIDER or ()
        self._cluster_manager = self.CLUSTER_MANAGER or ()

    @property
    def name(self):
        return self._name

    @property
    def required_provider(self):
        return self._cloud_provider

    @property
    def required_cluster(self):
        return self._cluster_manager
