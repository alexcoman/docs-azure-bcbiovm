"""
Cluster manager base-classes:
    (Beginning of) the contract that cluster managers must follow, and shared
    types that support that contract.
"""
import abc

import six


@six.add_metaclass(abc.ABCMeta)
class BaseCluster(object):

    """Base class for the cluster managers."""

    def __init__(self):
        self.command

    @abc.abstractmethod
    def bootstrap(self, config, cluster, no_reboot=False, verbose=True):
        """Update a bcbio AWS system with the latest code and tools.

        :param no_reboot: update the cluster host OS and reboot only if
                          it is `False`
        :param config:    bcbio configuration file
        :param cluster:   cluster name
        """
        pass

    @abc.abstractmethod
    def command(self, config, cluster, script):
        """Run a script on the bcbio frontend node inside a screen session.

        :param config:  bcbio configuration file
        :param cluster: cluster name
        :param script:  local path of the script to run

        Notes:
            The screen session name is the basename of the script.
        """
        pass

    @abc.abstractmethod
    def setup(self, config, cluster, verbose):
        """Rerun cluster configuration steps.

        :param econfig: bcbio configuration file
        :param cluster: cluster name
        :param verbose: if is `True` the output will be suppressed
                        when running Ansible playbooks
        """
        pass

    @abc.abstractmethod
    def start(self, config, cluster, no_reboot=False, verbose=True):
        """Start a bcbio-nextgen cluster.

        :param config:    bcbio configuration file
        :param cluster:   cluster name
        :param no_reboot: update the cluster host OS and reboot only if
                          it is `False`
        :param verbose:   if is `True` the output will be suppressed
                          when running Ansible playbooks
        """
        pass

    @abc.abstractmethod
    def stop(self, config, cluster, verbose):
        """Stop a bcbio-nextgen cluster.

        :param config: bcbio configuration file
        :param cluster: cluster name
        :param verbose: if is `True` the output will be suppressed
                        when running Ansible playbooks
        """
        pass

    @abc.abstractmethod
    def ssh(self, config, cluster, verbose, *command):
        """Connect to the frontend of the cluster using `ssh`

        :param config:  bcbio configuration file
        :param cluster: cluster name
        :param verbose: if is `True` the output will be suppressed
                        when running Ansible playbooks
        :param command: the command with the required arguments

        Notes:
            If `param: command` is provided this method will execute
            the received command on the remote machine instead of
            opening an interactive shell.
        """
        pass
