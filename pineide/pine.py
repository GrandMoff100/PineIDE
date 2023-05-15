from pathlib import Path
from typing import Iterable

from textual import events
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Horizontal, Vertical, Container
from textual.reactive import Reactive
from textual.widgets import Footer, Static, DirectoryTree
from textual.widget import Widget

from pineide.header import PineHeader
from pineide.sidebar import Sidespace
from pineide.panels import Files, VersionControl


class Terminal(Static):
    def compose(self) -> ComposeResult:
        yield Static("Terminal")


class FileTabs(Static):
    def compose(self) -> ComposeResult:
        yield Static("example.py")


class Body(Container):
    def compose(self) -> ComposeResult:
        yield FileTabs()
        yield Terminal()


class Pine(App):
    CSS_PATH = "pine.css"
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    icon = Reactive("")
    sidebar_panels = [
        Files(),
        VersionControl(),
    ]

    def __init__(self, *, path: str, **kwargs):
        super().__init__(**kwargs)
        self.path = Path(path).absolute()

    def compose(self) -> ComposeResult:
        self.title = "PineIDE"
        self.sub_title = self.path.as_posix()
        self.icon = "🌲"
        yield PineHeader(id="header")
        with Horizontal():
            yield Sidespace()
            yield Body()
        yield Footer()
