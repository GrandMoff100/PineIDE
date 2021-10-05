from os.path import abspath, basename, join

from textual.app import App
from textual.widgets import Footer, FileClick, ScrollView, DirectoryTree, Header
from textual.reactive import Reactive, watch
from .custom_widgets import CustomHeader


class PineIDE(App):
    """The PineIDE app class"""

    async def on_load(self) -> None:
        """Sent before going in to application mode."""

        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:
        """Call after terminal goes in to application mode"""

        await self.view.dock(CustomHeader(), edge="top")




