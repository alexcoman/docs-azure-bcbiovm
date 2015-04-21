"""Handles all requests relating to compute tasks using one cloud provider."""

from bcbiovm.common import constant
from bcbiovm.cluster import factory as cluster_factory
from bcbiovm.provider import factory as provider_factory

__all__ = ['API']


class BaseAPI(object):

    def dispatch(self, arguments):
        pass


class API(BaseAPI):

    def __init__(self, cluster_manager=constant.DEFAULT.CLUSTER_MANAGER,
                 cloud_provider=constant.DEFAULT.CLOUD_PROVIDER):
        super(API, self).__init__()
        self._cluster = cluster_factory.get_cluster_manager(cluster_manager)
        self._provider = provider_factory.get_cloud_provider(cloud_provider)

    def cluster_bootstrap(self, config, cluster, no_reboot, verbose):
        """Update a bcbio AWS system with the latest code and tools."""
        self._cluster.bootstrap(config, cluster, no_reboot)

    def cluster_command(self, config, cluster, script):
        """Run a script on the bcbio frontend node inside a screen session."""
        self._cluster.command(config, cluster, script)

    def cluster_setup(self, config, cluster, verbose):
        """Rerun cluster configuration steps."""
        self._cluster.setup(config, cluster, verbose)

    def cluster_start(self, config, cluster, no_reboot, verbose):
        """Start a bcbio-nextgen cluster."""
        self._cluster.start(config, cluster, no_reboot, verbose)

    def cluster_stop(self, config, cluster, verbose):
        """Stop a bcbio-nextgen cluster."""
        self._cluster.stop(config, cluster, verbose)

    def cluster_ssh(self, config, cluster, verbose, *command):
        """Connect to the frontend of the cluster using `ssh`."""
        self._cluster.ssh(config, cluster, verbose, *command)
