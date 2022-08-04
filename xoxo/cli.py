from typing import List, Union

from xoxo.xoxo import main


def app(argv: Union[List[str], None] = None) -> int:
    """Call the main entry point."""
    return main(argv)
