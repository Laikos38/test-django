import importlib.util

mypy_package = importlib.util.find_spec("mypy")
if mypy_package:
    from djangoresttest.core.checks.mypy_check import mypy  # noqa
