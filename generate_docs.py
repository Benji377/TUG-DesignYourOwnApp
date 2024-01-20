"""Program to generate `Docs` using `pdoc3` and crate a central `index.html`"""

import os
from pathlib import Path
# THIS SCRIPT REQUIRE pdoc3 TO BE INSTALLED
from pdoc import _render_template, import_module
from typing import List


def generate_docs_and_central_index(modules_to_process: List[str]) -> None:
    """Method to generate `docs` folder with central `index.html`

    Parameters:
        modules_to_process (list[str]): List of modules to process
    """

    modules = [import_module(module, reload=True) for module in modules_to_process]
    out_dir = "docs/html"
    template_dir = "docs/pdoc_templates"

    # Generate the docs for each module under docs folder
    command = f'pdoc --html --skip-errors --force --output-dir {out_dir} --template-dir {template_dir} {" ".join(modules_to_process)}'
    os.system(command=command)

    # Create a single base `index.html`
    with open(Path(out_dir, "index.html"), "w", encoding="utf-8") as index:
        # module.__name__
        index.write(_render_template("/html.mako", modules=sorted((f"{module.__name__}/index.html", "") for module in modules)))


if __name__ == "__main__":
    module_list = ["01-datatypes", "02-variables", "03-functions",
                   "04-tests", "05-conditionals", "06-loops", "07-collections", "project"]
    generate_docs_and_central_index(module_list)
