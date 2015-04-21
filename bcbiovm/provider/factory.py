"""Cloud provider factory."""

from bcbiovm.common import utils

__all__ = ['get_cloud_provider']

CLOUD_PROVIDER = {
    'AWS': 'bcbiovm.provider.aws.aws_provider.AWSProvider'
}


def get_cloud_provider(name):
    # TODO(alexandrucoman): Check if received name is valid
    return utils.load_class(CLOUD_PROVIDER.get(name))
