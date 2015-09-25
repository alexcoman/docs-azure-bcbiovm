bcbio-nextgen-vm - Architecture Proposal
--------------------------------------------------

Table of content:

- [I. Architecture](https://stackedit.io/editor#i-architecture)
    - [I.1. Architecture proposal](https://stackedit.io/editor#i1-architecture-proposal)
    - [I.2. The current architecture](https://stackedit.io/editor#i2-the-current-architecture)
        - [I.2.a. The bcbiovm.client module](https://stackedit.io/editor#i2a-the-bcbiovmclient-module)
        - [I.2.b. The bcbiovm.common module](https://stackedit.io/editor#i2b-the-bcbiovmcommon-module)
        - [I.2.c. The bcbiovm.docker module](https://stackedit.io/editor#i2c-the-bcbiovmdocker-module)
        - [I.2.d The bcbiovm.provider module](https://stackedit.io/editor#i2d-the-bcbiovmprovider-module)
- [II. Workflow](https://stackedit.io/editor#ii-workflow)
    - [II.1. Running the test environment](https://stackedit.io/editor#ii1-running-the-test-environment)
        - [II.1.a. Start or create the environment](https://stackedit.io/editor#ii1a-start-or-create-the-environment)
        - [II.1.b. Stop or destroy the environment](https://stackedit.io/editor#ii1b-stop-or-destroy-the-environment)
    - [II.2. Elasticluster with azure](https://stackedit.io/editor#ii2-elasticluster-with-azure)
        - [II.2.a. Create a cluster](https://stackedit.io/editor#ii2a-create-a-cluster)
        - [II.2.b. Re-run the setup](https://stackedit.io/editor#ii2b-re-run-the-setup)
        - [II.2.c. Destroy the cluster](https://stackedit.io/editor#ii2c-destroy-the-cluster)
- [II.3. Development life cycle](https://stackedit.io/editor#ii3-development-life-cycle)
- [II.4. Travis-CI](https://stackedit.io/editor#ii4-travis-ci)

#I. Architecture

Because the old version of the project was very hard to maintain or improve we decide to change it.

##I.1. Architecture proposal

The architecture proposal can be found here [alexandrucoman/bcbio-architecture-proposal](https://github.com/alexandrucoman/bcbio-architecture-proposal).

After some iteration the proposal was approved by the team.

> Alessandro;
> 
> > Thanks a lot for looking into this effort, we’re trying to be as less invasive
> > as possible on the existing codebase while at the same time avoiding hacks
> > which in the long term will result hard to mantain.
> 
> Absolutely agreed. Your architecture is way better than mine. I only
> wanted to make sure you didn't spend a ton of time on an
> implementation I hope will only be a stopgap.
> 
> > IMO for this use case inheritance and polymorphism can help a lot in defining 
> > common behaviours that can be shared in a hierarchy and tools like the “abc” 
> > module are very useful in enforncing the contracts by means of abstract 
> > classes / methods. I dont want to sound like the usual OOP purist, the beauty 
> > of Python is that it allows to mix different style of design / programming, but 
> > for this specific use case I certanly lean towards classes / inheritance.
> > It has also the advantage of being easeir to understand for code reviewers and
> > potential implementors of additional cloud providers.
> 
> That makes good sense. My experience designing bigger systems is that
> I always make a mess of things when I use OOP and do better when it's
> a more functional/immutable style, so I tend toward the later. But I
> agree that it makes sense here and would give you a clean separation
> -- we don't have to do either or and could mix in your OOP approach for the could provider abstraction.
> 
> > If it works for you, we could come up with an initial basic implementation that
> > can be refactored with a different design if you dont like it. [...]
> > If I got it right, you suggest to focus on the cloud provider abstraction
> > only for the time being leaving the rest as it is? Specifically, quoting from
> > Alex’s initial email and repo:
> >
> >>    - cloud provider: http://goo.gl/XFDXN7
> 
> That sounds great, and I think would give us the abstractions we need
> to get this running on Azure. What do you both think plugging the OOP
> implementation for the cloud provider part into the existing code-base
> and iterating on that?
> 
> Brad


##I.2. The current architecture

The new structure of the project is the following:
```
bcbiovm
├── client
│   ├── base.py
│   ├── commands.py
│   ├── __init__.py
│   ├── subcommands
│   │   ├── aws.py
│   │   ├── azure.py
│   │   ├── cluster.py
│   │   ├── config.py
│   │   ├── docker.py
│   │   ├── factory.py
│   │   ├── icel.py
│   │   ├── __init__.py
│   │   ├── ipython.py
│   │   └── tools.py
│   └── tools.py
├── common
│   ├── cluster.py
│   ├── constant.py
│   ├── constant.pyc
│   ├── exception.py
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── objects.py
│   ├── objectstore.py
│   └── utils.py
├── docker
│   ├── devel.py
│   ├── __init__.py
│   ├── ipythontasks.py
│   ├── manage.py
│   ├── mounts.py
│   ├── multitasks.py
│   ├── remap.py
│   └── run.py
├── __init__.py
├── __init__.pyc
├── ipython
│   ├── batchprep.py
│   └── __init__.py
├── provider
│   ├── aws
│   │   ├── aws_provider.py
│   │   ├── bootstrap.py
│   │   ├── clusterk
│   │   │   ├── clusterktasks.py
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── multitasks.py
│   │   ├── iam.py
│   │   ├── icel.py
│   │   ├── __init__.py
│   │   ├── resources.py
│   │   ├── ship.py
│   │   └── vpc.py
│   ├── azure
│   │   ├── azure_provider.py
│   │   ├── bootstrap.py
│   │   ├── __init__.py
│   │   └── ship.py
│   ├── base.py
│   ├── factory.py
│   ├── __init__.py
│   ├── playbook.py
│   └── ship.py
└── version.py
```

###I.2.a. The `bcbiovm.client` module

The client module has the following structure.
```
├── base.py
├── commands.py
├── __init__.py
├── subcommands
│   ├── aws.py
│   ├── azure.py
│   ├── cluster.py
│   ├── config.py
│   ├── docker.py
│   ├── factory.py
│   ├── icel.py
│   ├── __init__.py
│   ├── ipython.py
│   └── tools.py
└── tools.py
```

In the **base.py** module we can find (beginning of) the contract that commands and parsers must follow.

For example every command must follow the following contract class:

```python
@six.add_metaclass(abc.ABCMeta)
class BaseContainer(object):

    """
    Contract class for all the commands or containers.

    :ivar: items: A list which contains (container, metadata) tuples

    Example:
    ::
        class Example(BaseContainer):

            items = [(ExampleOne, metadata), (ExampleTwo, metadata),
                     (ExampleThree, metadata)]
            # ...
    """

    items = None

    def __init__(self):
        self._name = self.__class__.__name__
        self._parsers = {}
        self._containers = []

        # Setup the current job
        self.setup()

        # Bind all the received jobs to the current job
        for container, metadata in self.items or ():
            if not self.check_container(container):
                LOG.error("The container %(container)r is not recognized.",
                          {"container": container})
                continue
            self.register_container(container, metadata)

    @property
    def name(self):
        """Command name."""
        return self._name

    def task_done(self, result):
        """What to execute after successfully finished processing a task."""
        LOG.info("Execution successful with: %(result)s", result)

    def task_fail(self, exc):
        """What to do when the program fails processing a task."""
        # This should be the default behavior. If the error should
        # be silenced, then it must be done from the derrived class.
        LOG.exception("Failed to run %(name)r: %(reason)s",
                      {"name": self.name, "reason": exc})
        raise exc

    def interrupted(self):
        """What to execute when keyboard interrupts arrive."""
        LOG.warning("Interrupted by the user.")

    def prologue(self):
        """Executed once before the running of the command."""
        pass

    def epilogue(self):
        """Executed once after the running of the command."""
        pass

    @abc.abstractmethod
    def register_container(self, container, metadata):
        """Bind the received container to the current one."""
        pass

    @abc.abstractmethod
    def check_container(self, container):
        """Check if the received container is valid and can be used property.

        Exemple:
        ::
            # ...
            if not isintance(job, Job):
                return False

            return True
        """
        pass

    @abc.abstractmethod
    def setup(self):
        """Extend the parser configuration in order to expose this command."""
        pass

    @abc.abstractmethod
    def work(self):
        """Override this with your desired procedures."""
        pass
```

A short example of what is capable of the new client module can be found in the following:

```python
import argparse
import sys


class Hello(base.Command):

    """Returns a hello message."""

    def setup(self):
        """Extend the parser configuration in order to expose this command."""
        parser = self._parser.add_parser("hello")
        parser.add_argument("name")

    def prologue(self):
        """Executed once before the command run."""
        self.args.name = self.args.name.title()

    def work(self):
        """Override this with your desired procedures."""
        return "Hello {name}!".format(self.args.name)


class Echo(base.Command):

    """Returns the received message."""

    def setup(self):
        """Extend the parser configuration in order to expose this command."""
        parser = self._parser.add_parser("echo")
        parser.add_argument("message")

    def work(self):
        """Override this with your desired procedures."""
        return self.args.message


class Example(base.Container):

    """Utilities to help with develping using bcbion inside of docker."""

    items = [(Hello, "actions"), (Echo, "actions")]

    def setup(self):
        """Extend the parser configuration in order to expose this command."""
        parser = self._parser.add_parser("example")
        actions = parser.add_subparsers(title="[example commands]")
        self._register_parser("actions", actions)


class BCBioClient(base.Client):

    """bcbio-nextgen-vm command line application."""

    commands = [Example, "commands"]

    def setup(self):
        """Extend the parser configuration in order to expose all
        the received commands.
        """
        self._parser = argparse.ArgumentParser(
            description=("Client module example"))
        commands = self._parser.add_subparsers(
            title="[commands]")
        self._register_parser(commands, "commands")


def main():
    """Run the bcbio-nextgen-vm command line application."""
    bcbio = BCBioClient(sys.argv[1:])
    bcbio.run()


if __name__ == "__main__":
    main()

```

###I.2.b. The `bcbiovm.common` module

This modules contains all the objects that are not provider specific.

**bcbiovm.common.cluster** - Manage a cluster's life cycle.

```python
class ElastiCluster(object):

    """Wrapper over the elasticluster functionalities."""


    def get_cluster(self, cluster_name):
        """Loads a cluster from the cluster repository.

        :param cluster_name: name of the cluster
        :return: :class elasticluster.cluster.cluster: instance
        """
        # ...

    @classmethod
    def execute(cls, command, **kwargs):
        """Wrap elasticluster commands to avoid need to call separately."""
        # ...

    @classmethod
    def start(cls, cluster, config=None, no_setup=False):
        """Create a cluster using the supplied configuration.

        :param cluster:   Type of cluster. It refers to a
                          configuration stanza [cluster/<name>].
        :param config:    Elasticluster config file
        :param no_setup:  Only start the cluster, do not configure it.
        """
        # ...

    @classmethod
    def stop(cls, cluster, config=None, force=False, use_default=False):
        """Stop a cluster and all associated VM instances.

        :param cluster:     Type of cluster. It refers to a
                            configuration stanza [cluster/<name>].
        :param config:      Elasticluster config file
        :param force:       Remove the cluster even if not all the nodes
                            have been terminated properly.
        :param use_default: Assume `yes` to all queries and do not prompt.
        """
        # ...

    @classmethod
    def setup(cls, cluster, config=None):
        """Configure the cluster.

        :param cluster:     Type of cluster. It refers to a
                            configuration stanza [cluster/<name>].
        :param config:      Elasticluster config file
        """
        # ...

    @classmethod
    def ssh(cls, cluster, config=None, ssh_args=None):
        """Connect to the frontend of the cluster using the `ssh` command.

        :param cluster:     Type of cluster. It refers to a
                            configuration stanza [cluster/<name>].
        :param config:      Elasticluster config file
        :ssh_args:          SSH command.

        Note:
            If the ssh_args are provided the command will be executed on
            the remote machine instead of opening an interactive shell.
        """
        # ...
```

**bcbiovm.common.exception**:  Custom exceptions used across the project.

The base exception in the bcbiovm project is the following:

```python
class BCBioException(Exception):
    """Base bcbio-nextgen-vm exception

    To correctly use this class, inherit from it and define
    a `template` property.

    That `template` will be formated using the keyword arguments
    provided to the constructor.

    Example:
    ::
        class InvalidCluster(BCBioException):

            template = "Cluster %(cluser_name)r is not defined in %(config)r."


        raise InvalidCluster(cluser_name="Cluster name",
                             config="cluster.config")
    """

    template = "An unknown exception occurred."

    def __init__(self, message=None, **kwargs):
        message = message or self.template

        try:
            message = message % kwargs
        except (TypeError, KeyError):
            # Something went wrong during message formatting.
            # Probably kwargs doesn't match a variable in the message.
            message = ("Message: %(template)s. Extra or "
                       "missing info: %(kwargs)s" %
                       {"template": message, "kwargs": kwargs})

        super(BCBioException, self).__init__(message)
```

**bcbiovm.common.objectstore**: Manage pushing and pulling files from an object store like Amazon Web Services S3 or Azure Blob Service. (It extends `bcbio.distributed.objectstore.py`).

The base class for all the `StorageManagers` from `bcbiovm` is the following:

```python
@six.add_metaclass(abc.ABCMeta)
class StorageManager(object):

    """The contract class for all the storage managers."""

    @abc.abstractmethod
    def exists(self, container, filename, context=None):
        """Check if the received key name exists in the bucket.

        :container: The name of the container.
        :filename:  The name of the item from the container.
        :context:   More information required by the storage manager.
        """
        pass

    @abc.abstractmethod
    def upload(self, path, filename, container, context=None):
        """Upload the received file.

        :path:      The path of the file that should be uploaded.
        :container: The name of the container.
        :filename:  The name of the item from the container.
        :context:   More information required by the storage manager.
        """
        pass

    @abc.abstractmethod
    def load_config(self, sample_config):
        """Move a sample configuration locally, providing remote upload."""
        pass
```

In the future this module will be moved in the provider module.

**bcbiovm.common.utils**: Utilities and helper functions.

Some examples of tools that can be found in this module:

```python
class SSHClient(object):

    """Wrapper over paramiko SHH client."""

    def __init__(self, host=constant.SSH.HOST, port=constant.SSH.PORT,
                 user=constant.SSH.USER):
        """
        :param host:    the server to connect to
        :param port:    the server port to connect to
        :param user:    the username to authenticate as (defaults to
                        the current local username)
        """
        pass

    @property
    def client(self):
        """SSH Client."""
        return self._ssh_client

    def connect(self, bastion_host=None, user='ec2-user'):
        """Connect to an SSH server and authenticate to it.
        :param bastion_host:  the bastion host to connect to

        Note:
            In order to connect from the bastion host to another instance
            without storing the private key on the bastion SSH tunneling
            will be used. More information can be found on the following
            link: http://goo.gl/wqkHEk
        """
        pass

    def close(self):
        """Close this SSHClient and its underlying Transport."""
        pass

    def execute(self, command):
        """Execute a command on the SSH server.

        :param command:   the command to execute
        """
        pass

    def download_file(self, source, destination, **kwargs):
        """Download the source file to the received destination.

        :param source:      the path of the file which should be downloaded
        :param destination: the path where the file should be written
        :param permissions: The octal permissions set that should be given for
                            this file.
        :param open_mode:   The open mode used when opening the file.
        :param utime:       2-tuple of numbers, of the form (atime, mtime)
                            which is used to set the access and modified times
        """
        pass

    def stat(self, path, stat_format=("%s", "%Y", "%n")):
        """Return the detailed status of a particular file or a file system.

        :param path:          path to a file or a file system
        :param stat_format:   a valid format sequences
        """
        pass

    def disk_space(self, path, ftype=None):
        """Return the amount of disk space available on the file system
        containing the received file.

        :param ftype:   limit listing to file systems of the received type.
        :path path:     the path of the file

        :return:        a namedtuple which contains the following fields:
                        filesystem, total, used, available, percentage and
                        mount_point
        """
        pass
```

```python
def get_logger(name=None, format_string=None):
    """Obtain a new logger object.

    :param name:          the name of the logger
    :param format_string: the format it will use for logging.

    If it is not given, the the one given at command
    line will be used, otherwise the default format.
    """
```

```python
def write_file(path, content, permissions=constant.DEFAULT_PERMISSIONS,
               open_mode="wb", utime=None):
    """Writes a file with the given content.

    Also the function sets the file mode as specified.

    :param path:        The absolute path to the location on the filesystem
                        wherethe file should be written.
    :param content:     The content that should be placed in the file.
    :param permissions: The octal permissions set that should be given for
                        this file.
    :param open_mode:   The open mode used when opening the file.
    :param utime:       2-tuple of numbers, of the form (atime, mtime) which
                        is used to set the access and modified times
    """
```

```python
def execute(command, **kwargs):
    """Helper method to shell out and execute a command through subprocess.

    :param attempts:        How many times to retry running the command.
    :param binary:          On Python 3, return stdout and stderr as bytes if
                            binary is True, as Unicode otherwise.
    :param check_exit_code: Single bool, int, or list of allowed exit
                            codes.  Defaults to [0].  Raise
                            :class:`CalledProcessError` unless
                            program exits with one of these code.
    :param command:         The command passed to the subprocess.Popen.
    :param cwd:             Set the current working directory
    :param env_variables:   Environment variables and their values that
                            will be set for the process.
    :param retry_interval:  Interval between execute attempts, in seconds
    :param shell:           whether or not there should be a shell used to
                            execute this command.

    :raises:                :class:`subprocess.CalledProcessError`
    """
```


```python
def write_elasticluster_config(config, output,
                               provider=constant.DEFAULT_PROVIDER):
    """Write Elasticluster configuration file with user and security
    information.
    """
```

```python
def backup(path, backup_dir=None, delete=False, maximum=0):
    """
    Make a copy of the received file.

    :param path:     The absolute path of the file.
    :param backup:   The absolute path to the location on the filesystem
                     wherethe file should be written.
    :param delete:   Delete the source file.
    :param maximum:  The maximum number of backup files allowed.
    """
```

```python
def predict_size(size, convert="K"):
    """Attempts to guess the string format based on default symbols
    set and return the corresponding bytes as an integer.
    """
```


```python
def compress(source, destination=None, compression="gz"):
    """Saves many files together into a single tape or disk archive,
    and can restore individual files from the archive.

    :param source:      the path of the files that will be saved together
    :param destination: the path of the output
    :param compression: the compression level of the file

    :raises:
        If a compression method is not supported, CompressionError is raised.
    """
```


###I.2.c. The `bcbiovm.docker` module

```
├── devel.py
├── __init__.py
├── install.py
├── ipythontasks.py
├── manage.py
├── mounts.py
├── multitasks.py
├── remap.py
└── run.py
```

The docker module contains all the interactions with the docker environment.
This module will be ported to the new architecture and the common functionalities will be moved to common module and the provider specific one will be moved in the provider module.


###I.2.d The `bcbiovm.provider` module

```
├── aws
│   ├── aws_provider.py
│   ├── bootstrap.py
│   ├── clusterk
│   │   ├── clusterktasks.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── multitasks.py
│   ├── iam.py
│   ├── icel.py
│   ├── __init__.py
│   ├── resources.py
│   ├── ship.py
│   └── vpc.py
├── azure
│   ├── azure_provider.py
│   ├── bootstrap.py
│   ├── __init__.py
│   └── ship.py
├── base.py
├── factory.py
├── __init__.py
├── playbook.py
└── ship.py
```


The root directory of the provider module contains the provider base-classes: (Beginning of) the contract that cloud providers must follow, and shared types that support that contract.

For example every cloud provider must contain the following methods:

```python
@six.add_metaclass(abc.ABCMeta)
class BaseCloudProvider(object):

    _CHMOD = "chmod %(mode)s %(file)s"
    _HOME_DIR = "echo $HOME"
    _SCREEN = "screen -d -m -S %(name)s bash -c '%(script)s &> %(output)s'"

    def __init__(self, name=None):
        self._name = name or self.__class__.__name__
        self._flavor = self._set_flavors()
        self._ecluster = clusterops.ElastiCluster(self._name)

    @property
    def name(self):
        """The cloud provider name."""
        return self._name

    @abc.abstractmethod
    def _set_flavors(self):
        """Returns a dictionary with all the flavors available for the current
        cloud provider.

        Example:
        ::
            return {
                "m3.large": Flavor(cpus=2, memory=3500),
                "m3.xlarge": Flavor(cpus=4, memory=3500),
                "m3.2xlarge": Flavor(cpus=8, memory=3500),
            }
        """
        pass

    @abc.abstractmethod
    def information(self, cluster, config):
        """
        Get all the information available for this provider.

        The returned information will be used to create a status report
        regarding the bcbio instances.

        :config:    elasticluster config file
        :cluster:   cluster name

        :return:    an instance of :class bcbio.common.objects.Report:
        """
        pass

    @abc.abstractmethod
    def colect_data(self, cluster, config, rawdir):
        """Collect from the each instances the files which contains
        information regarding resources consumption.

        :param config:    elasticluster config file
        :param cluster:   cluster name
        :param rawdir:    directory where to copy raw collectl data files.

        Notes:
            The current workflow is the following:
                - establish a SSH connection with the instance
                - get information regarding the `collectl` files
                - copy to local the files which contain new information

            This files will be used in order to generate system statistics
            from bcbio runs. The statistics will contain information regarding
            CPU, memory, network, disk I/O usage.
        """
        pass

    @abc.abstractmethod
    def resource_usage(self, bcbio_log, rawdir):
        """Generate system statistics from bcbio runs.

        Parse the files obtained by the :meth colect_data: and put the
        information in :class pandas.DataFrame:.

        :param bcbio_log:   local path to bcbio log file written by the run
        :param rawdir:      directory to put raw data files

        :return: a tuple with two dictionaries, the first contains
                 an instance of :pandas.DataFrame: for each host and
                 the second one contains information regarding the
                 hardware configuration
        :type return: tuple
        """
        pass

    @abc.abstractmethod
    def bootstrap(self, cluster, config, reboot):
        """Install or update the the bcbio code and the tools with
        the latest version available.

        :param config:    elasticluster config file
        :param cluster:   cluster name
        :param reboot:    whether to upgrade and restart the host OS
        """
        pass

    def flavors(self, machine=None):
        if not machine:
            return self._flavor.keys()
        else:
            return self._flavor.get(machine)

    def start(self, cluster, config=None, no_setup=False):
        """Create a cluster using the supplied configuration.

        :param cluster:   Type of cluster. It refers to a
                          configuration stanza [cluster/<name>].
        :param config:    Elasticluster config file
        :param no_setup:  Only start the cluster, do not configure it.
        """
        pass

    def stop(self, cluster, config=None, force=False, use_default=False):
        """Stop a cluster and all associated VM instances.

        :param cluster:     Type of cluster. It refers to a
                            configuration stanza [cluster/<name>].
        :param config:      Elasticluster config file
        :param force:       Remove the cluster even if not all the nodes
                            have been terminated properly.
        :param use_default: Assume `yes` to all queries and do not prompt.
        """
        pass

    def setup(self, cluster, config=None):
        """Configure the cluster.

        :param cluster:     Type of cluster. It refers to a
                            configuration stanza [cluster/<name>].
        :param config:      Elasticluster config file
        """
        pass

    def ssh(self, cluster, config=None, ssh_args=None):
        """Connect to the frontend of the cluster using the `ssh` command.

        :param cluster:     Type of cluster. It refers to a
                            configuration stanza [cluster/<name>].
        :param config:      Elasticluster config file
        :ssh_args:          SSH command.

        Note:
            If the ssh_args are provided the command will be executed on
            the remote machine instead of opening an interactive shell.
        """
        pass

    def run_script(self, cluster, config, script):
        """Run a script on the frontend node inside a screen session.

        :param cluster:     Type of cluster. It refers to a
                            configuration stanza [cluster/<name>].
        :param config:      Elasticluster config file
        :param script:      The path of the script.
        """
        pass
```

On the **azure** and **aws** module we can find the implementation of those cloud providers.


#II. Workflow

We use two branches **master** and **develop**.

- The **master** branch will contain always the properly tested version.
- The **develop** branch will contains the features which can cause problems and they will be merged in the **master** after they become stable

> Alex;
>  
> Thanks for all this work, really brilliant. I added you as a
> collaborator, so feel free to setup branches and pull requests (or
> direct pulls) in the easiest way for you. I definitely don't want to
> slow you down with the merging/adding and this way we can get the
> correct git structure in place and them move over from development to
> master as we test and confirm everything looks good. 
> 
> Thank you again,
> Brad

In order to test the project without manually setup the environment can be used one of the following Vagrant files:

- [Default Python Environment](https://github.com/alexandrucoman/vagrant-environment/blob/master/bcbio-azure/Vagrantfile)
- **[Conda Environement](https://github.com/alexandrucoman/vagrant-environment/blob/master/bcbio-conda-azure/Vagrantfile)**

##II.1. Running the test environment

###II.1.a. Start or create the environment
```
$ git clone https://github.com/alexandrucoman/vagrant-environment.git
$ cd vagrant-environment/bcbio-azure
$ vagrant box update
$ vagrant up
```

```
==> bcbio-azure: Reinstall python-setuptools
==> bcbio-azure: bcbio-nextgen-vm==0.1.0a0
==> bcbio-azure: Removing the old version of bcbio-nextgen-vm.
==> bcbio-azure: Cloning the bcbio-nextgen-vm project.
==> bcbio-azure: Replace the elasticluster version from requirements.txt
==> bcbio-azure: Installing bcbio-nextgen-vm requirements.
==> bcbio-azure: Installing pybedtools in order to avoid MemoryError.
==> bcbio-azure: Installing the bcbio-nextgen-vm project.
==> bcbio-azure: Remove the current version of elasticluster.
==> bcbio-azure: Install azure-elasticluster.
==> bcbio-azure: Enforce ansible version 1.7.2
==> bcbio-azure: Remove the current version of ansible.
==> bcbio-azure: Copy managementCert.cer from /vagrant/provision/.shared.
==> bcbio-azure: Copy managementCert.pem from /vagrant/provision/.shared.
==> bcbio-azure: Change permisions for ~/.ssh directory.
==> bcbio-azure: Change permisions for managementCert
==> bcbio-azure: Change permisions for ~/.ansible
==> bcbio-azure: The /home/vagrant/.bcbio/elasticluster/azure.config already exists.
==> bcbio-azure: Vagrant is using the last version of elasticluster config.
```

###II.1.b. Stop or destroy the environment
```
$ vagrant halt
```

```
$ vagrant destroy
```

##II.2. Elasticluster with azure

###II.2.a. Create a cluster
```
$ vagrant ssh
$ elasticluster --storage /home/vagrant/.bcbio/elasticluster/storage \
                --config /home/vagrant/.bcbio/elasticluster/azure.config \
                --verbose start bcbio
```

```
Starting cluster `bcbio` with 2 compute nodes.
Starting cluster `bcbio` with 1 frontend nodes.
(this may take a while...)
INFO:gc3.elasticluster:Starting node compute001.
INFO:gc3.elasticluster:Starting node compute002.
INFO:gc3.elasticluster:Starting node frontend001.
[...]
```

###II.2.b. Re-run the setup

```
$ elasticluster --storage /home/vagrant/.bcbio/elasticluster/storage
                --config /home/vagrant/.bcbio/elasticluster/azure.config
                --verbose setup bcbio
```

```
Configuring cluster `bcbio`...

PLAY [Collecting facts] *******************************************************

GATHERING FACTS ***************************************************************
ok: [compute002]
ok: [frontend001]
ok: [compute001]
[...]
```

###II.2.c. Destroy the cluster
```
$ elasticluster --storage /home/vagrant/.bcbio/elasticluster/storage \
                --config /home/vagrant/.bcbio/elasticluster/azure.config \
                --verbose stop bcbio
```

```
Do you want really want to stop cluster bcbio? [yN] Y
Destroying cluster `bcbio`
INFO:gc3.elasticluster:shutting down instance `bcbio_vm0000_bcbio-compute001`
INFO:gc3.elasticluster:shutting down instance `bcbio_vm0001_bcbio-compute002`
INFO:gc3.elasticluster:shutting down instance `bcbio_vm0002_bcbio-frontend001`
```


##II.3. Development life cycle

- create a new branch with one of the following prefixes: **feature\\**, **bug\\**, **refactor\\**
- finish the changes for the current task
- open a new pull request with the changes on the develop branch
- if the Travis-CI build is ok and the code locks fine it will be merged to **develop** branch
- else go back to step 2

##II.4. Travis-CI

On every change in the bcbio-nextgen-vm repository the [build.py](https://github.com/alexandrucoman/bcbio-dev-conda/blob/master/build.py) script from [bcbio-dev-conda](https://github.com/alexandrucoman/bcbio-dev-conda) is runned.

The workflow is the following:

- mock conda recipes is if required
- setup the conda environment in order to use our packages
- build our recipes
- upload them to our channel **bcbio-dev** (if the branch is **develop**)

```
$ git clone https://github.com/alexandrucoman/bcbio-dev-conda build
    Cloning into 'build'...
    remote: Counting objects: 242, done.
    remote: Compressing objects: 100% (12/12), done.
    remote: Total 242 (delta 14), reused 5 (delta 5), pack-reused 225
    Receiving objects: 100% (242/242), 40.37 KiB | 0 bytes/s, done.
    Resolving deltas: 100% (89/89), done.
    Checking connectivity... done.
    before_install.9
$ if [ "$TRAVIS_BRANCH" == "develop" ]; then
    python build/build.py --bcbio-repo "$BCBIO_REPO" \
                          --upload --token "$BINSTAR_TOKEN" \
                          --numpy "$NUMPY";
  else 
      python build/build.py --bcbio-repo "$BCBIO_REPO" \
                            --bcbio-branch "$TRAVIS_BRANCH" \
                            --numpy "$NUMPY";
  fi

    [i] Mocking bcbio-nextgen-vm with {
        'source': {
            'git_url': 'https://github.com/alexandrucoman/bcbio-nextgen-vm.git',
            'git_tag': 'refactor/docker-devel'}}.
    [i] Trying to build Recipe(
        name='elasticluster',
        path='/home/travis/miniconda/conda-bld/linux-64/elasticluster-0.1.3bcbio-py27_100.tar.bz2',
        build=100,
        version='0.1.3bcbio') recipe.
    [i] Trying to build Recipe(
        name='bcbio-nextgen',
        path='/home/travis/miniconda/conda-bld/linux-64/bcbio-nextgen-0.9.2a-np19py27_100.tar.bz2',
        build=100,
        version='0.9.2a') recipe.
    [i] Trying to build Recipe(
        name='bcbio-nextgen-vm',
        path='/home/travis/miniconda/conda-bld/linux-64/bcbio-nextgen-vm-0.1.0a-py27_100.tar.bz2',
        build=100,
        version='0.1.0a') recipe.
$ export PACKAGE=$(conda build --output build/bcbio-nextgen-vm --numpy "$NUMPY")
```
The building history can be found [here](https://travis-ci.org/alexandrucoman/bcbio-nextgen-vm).
