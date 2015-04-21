"""Handles all requests relating to compute tasks using one cloud provider."""

from bcbiovm.common import constant
from bcbiovm.common import exception
from bcbiovm.cluster import factory as cluster_factory
from bcbiovm.provider import factory as provider_factory

__all__ = ['API']


class BaseAPI(object):

    _IGNORE_LIST = ['dispatch']

    def __init__(self):
        self._resouces = {}

    def _register_resource(self, resource):
        if resource in self._IGNORE_LIST:
            return

        method = getattr(self, resource, None)
        if not method:
            raise ValueError('Invalid resource name.')

        self._resouces[resource] = method

    def _get_resources(self):
        for method in dir(self):
            if method.startswith('_'):
                # Ignore protected and private methods
                continue
            self._register_resource(method, getattr())

    def dispatch(self, resource, *args, **kwargs):
        if resource not in self._resouces:
            raise AttributeError('Unregistered resource %(resource)s' %
                                 {"resource": resource})
        try:
            return self._resouces[resource](*args, **kwargs)
        except exception.BCBioException:
            # TODO(alexandrucoman): Treat the exception properly
            pass


class API(BaseAPI):

    def __init__(self, cluster_manager=constant.DEFAULT.CLUSTER_MANAGER,
                 cloud_provider=constant.DEFAULT.CLOUD_PROVIDER):
        super(API, self).__init__()
        self._cluster = cluster_factory.get_cluster_manager(cluster_manager)
        self._provider = provider_factory.get_cloud_provider(cloud_provider)

    def bootstrap(self, config, cluster, no_reboot, verbose):
        """Update a bcbio system with the latest code and tools."""
        return self._cluster.bootstrap(config, cluster, no_reboot)

    def command(self, config, cluster, script):
        """Run a script on the bcbio frontend node inside a screen session."""
        return self._cluster.command(config, cluster, script)

    def setup(self, config, cluster, verbose):
        """Rerun cluster configuration steps."""
        return self._cluster.setup(config, cluster, verbose)

    def start(self, config, cluster, no_reboot, verbose):
        """Start a bcbio-nextgen cluster."""
        return self._cluster.start(config, cluster, no_reboot, verbose)

    def stop(self, config, cluster, verbose):
        """Stop a bcbio-nextgen cluster."""
        return self._cluster.stop(config, cluster, verbose)

    def ssh(self, config, cluster, verbose, *command):
        """Connect to the frontend of the cluster using `ssh`."""
        return self._cluster.ssh(config, cluster, verbose, *command)

    def information(self, config, cluster):
        """Get all the information available for this provider."""
        return self._provider.information(config, cluster)

    def network_setup(self, config, cluster, recreate, network):
        """Create private network and associated resources.

        If it is possible a placement group or affinity group
        should be created as well. A placement group is a logical
        grouping of instances within a single availability zone.
        """
        return self._provider.network_setup(config, cluster, recreate,
                                            network)

    def resource_usage(self, cluster, config, verbose, log, outdir, rawdir):
        """Generate system statistics from bcbio runs.

        The statistics will contain information regarding
        CPU, memory, network, disk I/O usage.
        """
        return self._provider.resource_usage(cluster, config, verbose, log,
                                             outdir, rawdir)
