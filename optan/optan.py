import argparse
import logging
from typing import Any, Dict, Optional, Sequence


class _Params:
    def __init__(self):
        """Manage parameters."""
        self._params = {}

    @property
    def params(self):
        return self._params

    def add_param(self, key: str, value: Any, overwrite: bool = False):
        """Add parameter.

        Args:
            key (str): Parameter key
            value (Any): Parameter value
            overwrite (bool, optional): Overwrite if key already exists. Defaults to False.
        """
        if key in self._params and not overwrite:
            if not overwrite:
                logging.warning(
                    "Key {} already exists. If you want to overwrite, set argument 'overwrite' to 'True'.".format(key)
                )
        else:
            self._params[key] = value

    def add_params(self, params: Dict[str, Any], overwrite: bool = False):
        """Add parameters.

        Args:
            params (Dict[str, Any]): Parameters dict
            overwrite (bool, optional): Overwrite if key already exists. Defaults to False.
        """
        for k, v in params.items():
            self.add_param(k, v, overwrite)


class Optan(argparse.ArgumentParser):
    def parse_args(  # type: ignore
        self, args: Optional[Sequence[str]] = None, namespace: argparse.Namespace = None
    ) -> argparse.Namespace:
        """Parse arguments.

        Args:
            args (Optional[Sequence[str]], optional): Optional args. Defaults to None.
            namespace (argparse.Namespace, optional): Optional namespace. Defaults to None.

        Returns:
            argparse.Namespace: Parsed arguments namespace
        """
        return super().parse_args(args, namespace)
