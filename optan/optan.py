import argparse
import logging
import os.path
from datetime import datetime as dt
from typing import Any, Dict, Optional, Sequence

import pandas as pd


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
    def __init__(self, fmt: str = r"%Y%m%d%H%M%S", *args, **kwargs):
        """Argument parser.

        Args:
            fmt (str, optional): Datetime format. Defaults to r"%Y%m%d%H%M%S".
        """
        super().__init__(*args, **kwargs)

        self._params = _Params()
        self._datetime = dt.now().strftime(fmt)

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
        namespace = super().parse_args(args, namespace)
        self._params.add_params((vars(namespace)), overwrite=False)

        return namespace

    @property
    def params(self):
        return self._params.params

    def add_param(self, key: str, value: Any, overwrite: bool = False):
        """Add parameter.

        Args:
            key (str): Parameter key
            value (Any): Parameter value
            overwrite (bool, optional): Overwrite if key already exists. Defaults to False.
        """
        self._params.add_param(key, value, overwrite)

    def add_params(self, params: Dict[str, Any], overwrite: bool = False):
        """Add parameters.

        Args:
            params (Dict[str, Any]): Parameters dict
            overwrite (bool, optional): Overwrite if key already exists. Defaults to False.
        """
        self._params.add_params(params, overwrite)

    def write(self, path: str):
        """Write params to .csv-file.

        Args:
            path (str): Path to output .csv-file
        """
        df = pd.read_csv(path) if os.path.exists(path) else pd.DataFrame()

        series = pd.Series({"#": str(len(df) + 1), "datetime": self._datetime, **self._params.params})
        df = df.append(series, ignore_index=True)[series.index.to_list()]

        df.to_csv(path, index=False)
        logging.info("Parameters saved to {}.".format(path))
