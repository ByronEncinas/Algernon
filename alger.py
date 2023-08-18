""" 
#!/usr/bin/env python3
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


#log.inf('')

# log treatment to avoid possible errors

print(sys.argv)

# Differentiate between CLI and GUI
if len(sys.argv) > 1:
    if sys.argv[1] == 'non':
        App()
    else:
        try: # exists argument alger %%%%%
            sys.argv[2]
        except IndexError: # no?
            getattr(Shell, 'help') # then do the same git does
        try:
                getattr(Shell, sys.argv[1])()  
        except AttributeError:
                print(AttributeError)
        finally:
            print("App Terminated")    
else:
     getattr(Shell, 'help')

# test setting
if __name__ == '__main__':
    pass

    