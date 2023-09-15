# here commands
from rich.console import Console


class Helpers:
    """Helper functions for converter"""

    def parse_format(self, filename: str , data: list, outputformat: str) -> None:
        
        # either json, xml, yaml, toml, ...
        _, self.INPUT_EXT = filename.split(".") 
        _, self.OUTPUT_EXT = filename.split(".")

class Shell(Helpers):

    def __init__(self):
        self.supported = {"JSON":True,
                          "XML": True,
                          "TOML":True,
                          "YAML":True,}
        
        Console().print("""[bold green] 
          o_o
         (_^_) [bold white]( °)>   
               |  U
               (___)   """)

        # if class is created with --objects then declare

    def display(self, filename, format):

        pass


    def help():

        Console().print(""" 
[yellow]usage: [green]alg [orange1][-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--config-env=<name>=<envvar>] <command> [<args>]

[yellow]These are common Git commands used in various situations:

[yellow]start a working area (see also: git help tutorial)
   [green]display     [orange1]Shows data in the format it is read
   [green]tree      [orange1]Will show a hierarchy tree with all the data (looking like git adog command)

[yellow]work on the current change (see also: git help everyday)
   [green]levitate       [orange1]Reads data and asks for the format of the final product
   [green]drop        [orange1]Converts data that has been levitated into the final format
   [green]restore   [orange1]
   [green]rm        [orange1]Remove files from the working tree and from the index""")