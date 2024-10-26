import os as _os, sys as _sys


_HELP = '''
Available commands to use:
    > AwesomeAiogram hello-world # Hello world test func
'''


def _hello_world(*args, **kwargs):
    print('Hello world')


def _help(*args, **kwargs):
    print(_HELP)


class ConsoleCommandExecutor:
    def __init__(self):
        self.path = _os.getcwd()

    def __call__(self):
        for index, arg in enumerate(_sys.argv):
            _callable = {
                # Base Commands:
                'hello-world': _hello_world,  # Type in console `AwesomeAiogram hello-world` to run.
                'help': _help,
            }.get(arg)

            if _callable is None:
                continue

            _callable(self.path, )
            break

        else:
            print("No available command! Use 'AwesomeAiogram help' to see available commands!")


main = ConsoleCommandExecutor()
