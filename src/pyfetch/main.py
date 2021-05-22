import enum

from pyfetch.utils import (
    get_user_hostname_info,
    get_memory_info,
    get_cores,
)


class Colors:
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def run():
    print(Colors.BLUE, end='')
    print(get_user_hostname_info())
    print(Colors.RESET, end='')
    print()
    print(Colors.GREEN, end='')
    print(f'Memory: {get_memory_info()}')
    print(Colors.RESET, end='')
    print(Colors.YELLOW, end='')
    print(f'Cores: {get_cores()}')
    print(Colors.RESET, end='')
