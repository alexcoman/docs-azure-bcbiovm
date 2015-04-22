"""Worker factory."""

from bcbiovm.common import utils

__all__ = ['get_worker']

WORKERS = {
    'docker': 'bcbiovm.worker.docker.docker_worker.DockerWorker'
}


def get_worker(name):
    # TODO(alexandrucoman): Check if received name is valid
    return utils.load_class(WORKERS.get(name))
