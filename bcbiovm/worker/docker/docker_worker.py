from bcbiovm.common import util
from bcbiovm.worker import base

LOG = util.get_logger("DockerWorker")


class DockerWorker(base.BaseWorker):

    CLOUD_PROVIDER = ["AWS"]

    def __init__(self):
        super(DockerWorker, self).__init__()
