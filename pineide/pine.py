from pathlib import Path
from typing import Iterable

from textual import events
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Horizontal, Container
from textual.reactive import Reactive
from textual.widgets import Footer, Static

from pineide.header import PineHeader
from pineide.sidebar import Sidespace
from pineide.panels import Files, VersionControl
from pineide.editor import Editor


class Terminal(Static):
    def compose(self) -> ComposeResult:
        yield Static("Terminal")


class Body(Container):
    def compose(self) -> ComposeResult:
        yield Editor(classes="empty-screen")
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
            yield Sidespace(shrink=True)
            yield Body()
        yield Footer()
