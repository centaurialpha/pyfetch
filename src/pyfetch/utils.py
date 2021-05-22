import os
import psutil


def get_username() -> str:
    return os.getenv('USER')


def get_hostname() -> str:
    host_filename = '/etc/hostname'
    with open(host_filename) as host_file:
        return host_file.read().strip()


def get_user_hostname_info() -> str:
    user = get_username()
    host = get_hostname()
    return f'{user}@{host}'


def _get_memory():
    return psutil.virtual_memory()


def _convert_to_gb(value):
    return value / (1024**3)


def _convert_to_mb(value):
    return value / (1024**2)


def get_used_memory():
    mem_obj = _get_memory()
    used = mem_obj.used
    return round(_convert_to_gb(used), 2)


def get_total_memory():
    mem_obj = _get_memory()
    total = mem_obj.total
    return round(_convert_to_gb(total), 2)


def get_memory_info() -> str:
    used_mem = get_used_memory()
    total_mem = get_total_memory()
    return f'{used_mem}GB / {total_mem}GB'


def get_cores() -> str:
    return psutil.cpu_count()
