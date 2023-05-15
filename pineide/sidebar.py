
from textual import events
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, ContentSwitcher, Button


class SidebarPanel(Static):
    panel_id = None
    icon = None

    def __init__(self, **kwargs):
        super().__init__(id=self.panel_id, **kwargs)

    def button(self) -> Button:
        return Button(id=self.panel_id, label=self.icon, classes="sidebar-button")

    def compose(self) -> ComposeResult:
        raise NotImplementedError()


class SidebarButtons(Static):
    def compose(self) -> ComposeResult:
        with Vertical():
            for panel in self.app.sidebar_panels:
                yield panel.button()

class Sidebar(Static):
    def compose(self) -> ComposeResult:
        with ContentSwitcher(initial="files"):
            yield from self.app.sidebar_panels

class Sidespace(Static):
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield SidebarButtons()
            yield Sidebar()
