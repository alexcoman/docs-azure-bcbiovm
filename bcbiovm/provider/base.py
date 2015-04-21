"""
Provider base-classes:
    (Beginning of) the contract that cloud providers must follow, and shared
    types that support that contract.
"""
import abc

import six


@six.add_metaclass(abc.ABCMeta)
class BaseCloudProvider(object):

    def __init__(self, name=None):
        self._name = name or self.__class__.__name__
        self._flavor = self._set_flavors()

    @abc.abstractmethod
    def _set_flavors(self):
        """Returns a dictionary with all the flavors available for the current
        cloud provider.

        Example:
        ::
            return {
                "m3.large": Flavor(name="m3.large", cpus=2, memory=3500),
                "m3.xlarge": Flavor(name="m3.xlarge", cpus=4, memory=3500),
                "m3.2xlarge": Flavor(name="m3.2xlarge", cpus=8, memory=3500),
            }
        """
        pass

    @abc.abstractmethod
    def information(self, config, cluster):
        """
        Get all the information available for this provider.

        :param config: bcbio configuration file
        :param cluster: cluster name
        """
        pass

    def network_setup(self, config, cluster, recreate, network):
        """Create private network and associated resources.

        If it is possible a placement group or affinity group
        should be created as well. A placement group is a logical
        grouping of instances within a single availability zone.

        :param config:   bcbio configuration file
        :param cluster:  cluster name
        :param recreate: remove and recreate the network
        :param network:  network address in CIDR notation (a.b.c.d/e)
        """
        pass

    def flavors(self, machine=None):
        if not machine:
            return self._flavor.keys()
        else:
            return self._flavor.get(machine)
