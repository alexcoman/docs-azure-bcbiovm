from bcbiovm.worker import base


class DockerWorker(base.BaseWorker):

    CLOUD_PROVIDER = ["AWS"]

    def __init__(self):
        super(DockerWorker, self).__init__()
