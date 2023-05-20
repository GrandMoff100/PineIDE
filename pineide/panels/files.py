from ..sidebar import SidebarPanel
from textual.app import ComposeResult
from textual.widgets import DirectoryTree
from textual import events

__all__ = ["Files"]


class CustomDirectoryTree(DirectoryTree):
    pass


class Files(SidebarPanel):
    panel_id = "files"
    icon = "📁"

    def compose(self) -> ComposeResult:
        yield CustomDirectoryTree(path=self.app.path)

    def _on_mount(self, _: events.Mount) -> None:
        tree = self.query_one("DirectoryTree")
        tree.show_root = False
        tree.show_guides = False
        tree.guide_depth = 1
