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

    def __init__(self, name=None, help_msg=None):
        self._args = None
        self._help = help_msg
        self._name = name or self.__class__.__name__.lower()

    @property
    def args(self):
        return self._args

    def _process(self):
        """Wrapper over the `process`."""
        self.prologue()

        try:
            result = self.process()
        except KeyboardInterrupt:
            self.interrupted()
        except (exception.BCBioException, Exception) as exc:
            self.command_fail(exc)
        else:
            self.command_done(result)

        self.epilogue()
        return result

    def _setup(self, parser):
        """Wrapper over the `setup`."""
        subparser = parser.add_parser(self._name, self._help)
        self.setup(subparser)
        subparser.set_defaults(func=self.process)

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

    def pre_parse(self, command_line):
        """What to execute before the `parse_args`."""
        pass

    def post_parse(self, arguments):
        """What to execute after the `parse_args`."""
        self._args = arguments

    def prologue(self):
        """Executed once before the main procedures."""
        pass

    @abc.abstractmethod
    def process(self):
        """Override this with your desired procedures."""
        pass

    def epilogue(self):
        """Executed once after the main procedures."""
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
