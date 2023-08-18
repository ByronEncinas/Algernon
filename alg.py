""" 
#!/usr/bin/env python
 """
""" Algernon should run GUI when: $ alger-gui """

import logging
import sys, os

from typing import Dict, Callable

from rich.console import Console
from rich.logging import RichHandler

from interpreter import Shell

from app import MainWindow, App


console = Console()
log = logging.getLogger()
path = os.getcwd()

logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler(markup=True, rich_tracebacks=True)])


# be non case specific
sys.argv = [elem.lower() for elem in sys.argv]

# log treatment to avoid possible errors

# Differentiate between CLI and GUI
if len(sys.argv) >= 2: # if argument given
    if sys.argv[1] == "non": # if that argument is 'non'
        App()
    else: # if argument is for the CLI
        getattr(Shell, sys.argv[1])() # then do the same git does
else:
    getattr(Shell, "help")()

# test setting
if __name__ == '__main__':
    pass

    