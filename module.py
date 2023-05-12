from py2cfg import CFGBuilder
from py2cfg.model import CFG
import ast

# Add the build_from_code method to CFGBuilder
def build_from_code(self, name: str, code_str: str) -> CFG:
        """
        Build a CFG from code 

        Args:
            name: The name of the CFG being built.
            code_str: The code to build the CFG from.

        Returns:
            The CFG produced from the source file.
        """
        tree = ast.parse(code_str)
        cfg = self.build(name, tree)
        return cfg

CFGBuilder.build_from_code = build_from_code

def get_cfg(file_name: str, code_str: str) -> CFG:
    cfg_builder = CFGBuilder()
    cfg = cfg_builder.build_from_code(file_name, code_str)
    cfg.build_visual("output/" + file_name, "png")
    return file_name
