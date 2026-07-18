"""Shared helpers for loading explicitly selected local Python modules."""

import importlib.util


def load_python_module(name, path):
    """Load one Python source file as a module.

    The caller remains responsible for deciding which local directory is trusted
    and for handling import errors at the plugin or agent boundary.
    """
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot create a loader for {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
