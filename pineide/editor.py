"""Module for the editor."""

import time

from textual.app import ComposeResult
from textual.widgets import Static, ContentSwitcher, TabbedContent, TabPane, Markdown, Tabs
from textual.containers import Vertical
from textual.reactive import Reactive
from pineide.panels.files import Files

from pyfiglet import Figlet

from pathlib import Path
from rich.syntax import Syntax

class Date(Static):
    def render(self) -> str:
        return str(time.time())

    def on_mount(self) -> None:
        self.set_interval(0.1, callback=self.refresh)


class DefaultScreen(Static):
    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static(
                Figlet(font="isometric3", ).renderText("pine"),
                id="brand",
            )
            yield Static("Welcome to PineIDE!", id="welcome")
            yield Static(f"Press {Files.icon} to view your files.", id="open")
            yield Date(id="date")


class ClosableTabbedFiles(TabbedContent):
    """Tabbed content that can be closed with ."""

    open_files: list[Path] = Reactive([Path("README.md")])

    def compose(self) -> ComposeResult:
        with TabbedContent(id="files"):
            for i, file in enumerate(self.open_files):
                with TabPane(file.name, id=f"file-{i}"):
                    with file.open("r") as fp:
                        code = fp.read()
                        yield Static(Syntax(
                            code,
                            Syntax.guess_lexer(str(file.absolute()), code),
                            line_numbers=True
                        ))

    def watch_open_files(self, value: list[Path]) -> None:
        """When the open files change, update the tabs."""
        self.tabs = [file.name for file in value]


class Editor(Static):
    """The editor."""

    def compose(self) -> ComposeResult:
        with ContentSwitcher(id="editor", initial="default"):
            yield ClosableTabbedFiles(id="files")
            yield DefaultScreen(id="default")
