import argparse
from typing import Optional, Sequence


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
