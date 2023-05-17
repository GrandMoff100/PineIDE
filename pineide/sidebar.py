
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
        with ContentSwitcher(initial="files", id="panels"):
            yield from self.app.sidebar_panels


class Sidespace(Static):
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield SidebarButtons()
            yield Sidebar()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        for panel in self.app.sidebar_panels:
            if panel.panel_id == event.button.id:
                panels = self.query_one("#panels")
                sidebar = self.query_one(Sidebar)

                if panels.current == panel.panel_id and sidebar.styles.display == "block":
                    sidebar.add_class("hidden")
                    self.add_class("without-sidebar")
                else:
                    sidebar.remove_class("hidden")
                    self.remove_class("without-sidebar")

                panels.current = panel.panel_id
                break
