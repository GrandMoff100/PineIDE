from pathlib import Path
from typing import Iterable

from textual import events
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Horizontal, Vertical, Container
from textual.reactive import Reactive
from textual.widgets import Footer, Static, DirectoryTree
from textual.widget import Widget

from pineide.header import PineHeader


class Terminal(Static):
    def compose(self) -> ComposeResult:
        yield Static("Terminal")


class FileTabs(Static):
    def compose(self) -> ComposeResult:
        yield Static("example.py")


class SideButtons(Static):
    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static("📄")
            yield Static("📄")
            yield Static("📄")
            yield Static("📄")
            yield Static("📄")
            yield Static("📄")
            yield Static("📄")
            yield Static("📄")
            yield Static("📄")
            yield Static("📄")
            yield Static("📄")


class Sidebar(Static):
    def compose(self) -> ComposeResult:
        yield DirectoryTree(path=self.app.path)

    def _on_mount(self, _: events.Mount) -> None:
        tree = self.query_one("DirectoryTree")
        tree.show_root = False
        tree.show_guides = False
        tree.guide_depth = 1


class Pine(App):
    CSS_PATH = "pine.css"
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    icon = Reactive("")

    def __init__(self, *, path: str, **kwargs):
        super().__init__(**kwargs)
        self.path = Path(path).absolute()

    def compose(self) -> ComposeResult:
        self.title = "PineIDE"
        self.sub_title = self.path.as_posix()
        self.icon = "🌲"
        yield PineHeader(id="header")
        with Horizontal():
            yield SideButtons()
            yield Sidebar()
            with Container():
                yield FileTabs(id="file-tabs")
                yield Terminal(id="terminal")
        yield Footer()
