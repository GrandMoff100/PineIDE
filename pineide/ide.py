from os.path import abspath, basename, join

from rich.console import RenderableType
from rich.syntax import Syntax
from rich.traceback import Traceback

from textual.app import App
from textual.widgets import Footer, FileClick, ScrollView, DirectoryTree
from .custom_widgets import CustomHeader


class PineIDE(App):
    """The PineIDE app class"""

    async def on_load(self) -> None:
        """Sent before going in to application mode."""

        await self.bind("b", "view.toggle('sidebar')", "Toggle File View")
        await self.bind("q", "quit", "Quit")
        
        self.path = abspath(join(basename(__file__), "../../../"))
        self.directory = DirectoryTree(self.path, "Code")
        self.body = ScrollView()

    async def on_mount(self) -> None:
        """Call after terminal goes in to application mode"""

        await self.view.dock(CustomHeader(), edge="top")
        await self.view.dock(Footer(), edge="bottom")

        # Note the directory is also in a scroll view
        await self.view.dock(
            ScrollView(self.directory),
            edge="left",
            size=48,
            name="sidebar"
        )
        await self.view.dock(self.body, edge="top")

    async def handle_file_click(self, message: FileClick) -> None:
        """A message sent by the directory tree when a file is clicked."""




