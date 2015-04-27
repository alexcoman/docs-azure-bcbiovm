"""
Parse the command line and return an object with the given options.
"""
import abc

import six

from bcbiovm.common import exception


@six.add_metaclass(abc.ABCMeta)
class AbstractCommand(object):

    """Abstract base class for command.

    Example:
    ::
        class Hello(AbstractCommand):

            def __init__(self):
                super(Hello, self).__init__(name="hello",
                                            help_msg="print `Hello World!`")

            def process(self):
                print("Hello World!")
    """

    def __init__(self, parrent, name=None, help_msg=None):
        self._help = help_msg
        self._name = name or self.__class__.__name__.lower()
        self._parent = parrent

    @property
    def args(self):
        return self._parent.args

    @property
    def command_line(self):
        return self._parent.command_line

    def _process(self):
        """Wrapper over the `process`."""
        try:
            result = self.process()
        except KeyboardInterrupt:
            self.interrupted()
        except (exception.BCBioException, Exception) as exc:
            self.command_fail(exc)
        else:
            self.command_done(result)
        return result

    def add_subparser(self, parser):
        """Setup a new subparser."""
        subparser = parser.add_parser(self._name, self._help)
        self.setup(subparser)
        subparser.set_defaults(func=self._process)

    def setup(self, subparser):
        """Setup the subcommand parser.

        Example:
        ::
            # ...
            subparser.add_option(
                "--quiet", action="store_const", const=0, dest="verbose")
            subparser.add_option(
                "--verbose", action="store_const", const=1, dest="verbose")
            subparser.add_option(
                "--noisy", action="store_const", const=2, dest="verbose")
            # ...
        """
        pass

    @abc.abstractmethod
    def process(self):
        """Override this with your desired procedures."""
        pass

    def prologue(self):
        """Executed once before processing the arguments.

        Example:
        ::
            # ...
            if self.command_line[1] == constants.SPECIAL_COMMAND:
                self._command_line.append(constants.SPECIAL_ARGUMENT)
            # ...
        """
        pass

    def epilogue(self):
        """Executed once after processing the arguments."""
        pass

    def command_done(self, task, result):
        """What to execute after successfully finished processing a command."""
        pass

    def command_fail(self, task, exc):
        """What to do when the program fails processing a command."""
        pass

    def interrupted(self):
        """What to execute when keyboard interrupts arrive."""
        pass


class AbstractParser(object):

    COMMANDS = None

    def __init__(self, command_line):
        self._command_line = command_line
        self._args = None
        self._commands = []
        self._parser = None

        self.setup()

    @property
    def command_line(self):
        return self._command_line

    @property
    def args(self):
        return self._args

    @abc.abstractmethod
    def check_command(self, command):
        """Check if the received command is valid and can be used property.

        Exemple:
        ::
            # ...
            if not isintance(command, AbstractCommand):
                return False

            return True
        """
        pass

    @abc.abstractmethod
    def init_parser(self):
        """Setup the argument parser.

        Exemple:
        ::
            # ...
            self._parser = argparse.ArgumentParser(description=description)
            self._parser.add_argument("--example", help="just an example")
            # ...
        """
        pass

    @abc.abstractmethod
    def get_subparsers(self):
        """Setup and return a subparsers container.

        Example:
        ::
            # ...
            subparsers = self.parser.add_subparsers(title="[sub-commands]")
            return subparsers
        """
        pass

    def setup(self):
        """Setup the parser."""
        self.init_parser()
        if not self.COMMANDS:
            return

        subparser = self.get_subparser()
        for command in self.COMMANDS:
            self.register_command(command, subparser)

    def register_command(self, command, parser):
        if not self.check_command(command):
            return False

        command.setup(parser)
        self._commands.append(command(self))

    def prologue(self):
        """Executed once before the main procedures."""
        for command in self._commands:
            command.pre_parse()

    def epilogue(self):
        """Executed once after the main procedures."""
        for command in self._commands:
            command.post_parse()

    def run(self):
        self.prologue()
        self._args = self._parser.parse_args(self.command_line)
        self.epilogue()
