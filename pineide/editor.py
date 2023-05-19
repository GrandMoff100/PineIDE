"""Module for the editor."""

from textual.app import ComposeResult, RenderResult
from textual.widgets import Static
from textual.containers import Vertical
from pineide.panels.files import Files

from pyfiglet import Figlet


class PineLogo(Static):
    def render(self) -> RenderResult:
        return Figlet(font="isometric3", ).renderText("pine")


class EmptyScreen(Static):
    def compose(self) -> ComposeResult:
        with Vertical():
            yield PineLogo()
            yield Static("Welcome to PineIDE!", id="welcome")
            yield Static(f"Press {Files.icon} to open a file.", id="open")
            

class Editor(Static):
    def compose(self) -> ComposeResult:
        yield EmptyScreen()
