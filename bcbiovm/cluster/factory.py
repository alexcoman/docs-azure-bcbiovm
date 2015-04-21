"""Cluster factory."""

from bcbiovm.common import utils

__all__ = ['get_cluster_manager']

CLUSTER_MANAGER = {
    'elasticluster': 'bcbiovm.cluster.elasticluster.ElastiCluster'
}


def get_cluster_manager(name):
    # TODO(alexandrucoman): Check if received name is valid
    return utils.load_class(CLUSTER_MANAGER.get(name))
