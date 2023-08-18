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
   [green]clone     [yellow]Clone a repository into a new directory
   [green]init      [yellow]Create an empty Git repository or reinitialize an existing one

[yellow]work on the current change (see also: git help everyday)
   [green]add       [yellow]Add file contents to the index
   [green]mv        [yellow]Move or rename a file, a directory, or a symlink
   [green]restore   [yellow]Restore working tree files
   [green]rm        [yellow]Remove files from the working tree and from the index""")