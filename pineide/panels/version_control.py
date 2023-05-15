from ..sidebar import SidebarPanel
from textual.app import ComposeResult
from textual.widgets import Static
from textual import events

__all__ = ["VersionControl"]


class VersionControl(SidebarPanel):
    panel_id = "version_control"
    icon = "🏷️ "

    def compose(self) -> ComposeResult:
        yield Static("Version Control")
