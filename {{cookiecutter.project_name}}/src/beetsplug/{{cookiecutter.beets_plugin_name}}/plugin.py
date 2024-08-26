"""{{ cookiecutter.friendly_name }}.

This example code is from https://beets.readthedocs.io/en/stable/dev/plugins.html.
"""

from optparse import Values
from typing import List
from typing import Optional

from beets.library import Library  # type: ignore
from beets.plugins import BeetsPlugin  # type: ignore
from beets.ui import Subcommand  # type: ignore


my_example_command = Subcommand("{{ cookiecutter.beets_plugin_name }}", help="do something")


def say_hi(lib: Library, opts: Values, args: List[str]) -> None:
    """Say hi."""
    print("Hello everybody! I'm a plugin!")


my_example_command.func = say_hi


class {{ cookiecutter.camel_case }}Plugin(BeetsPlugin):  # type: ignore
    """{{ cookiecutter.friendly_name }}."""

    def __init__(self, name: Optional[str] = "{{ cookiecutter.beets_plugin_name }}") -> None:
        super().__init__(name)
        self.register_listener("pluginload", self.loaded)
        self.template_funcs["initial"] = _tmpl_initial

    def loaded(self) -> None:
        """Display plugin loaded message."""
        self._log.info("Plugin loaded!")

    def commands(self) -> List[Subcommand]:
        """Return beets subcommands."""
        return [my_example_command]


def _tmpl_initial(text: str) -> str:
    """Return the uppercase initial letter of the text."""
    if text:
        return text[0].upper()
    else:
        return ""
