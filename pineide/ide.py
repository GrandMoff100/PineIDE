from os.path import abspath, basename, join

from rich.console import RenderableType
from rich.syntax import Syntax
from rich.traceback import Traceback

from textual.app import App
from textual.widgets import Footer, FileClick, ScrollView, DirectoryTree
from textual.reactive import Reactive, watch
from .custom_widgets import CustomHeader


class PineIDE(App):
    """The PineIDE app class"""
    states = Reactive({
        'show_file_sidebar': True
    })
    async def on_load(self) -> None:
        """Sent before going in to application mode."""

        await self.bind("b", "toggle_sidebar", "Toggle File View")
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
            name="sidebar",
            z=1
        )
        await self.view.dock(self.body, edge="top")

    async def action_toggle_sidebar(self):
        self.states.update(show_toggle_sidebar=not self.states.get('show_toggle_sidebar'))

    async def update_sidebar(self, states: dict):
        self.bar.animate("layout_offset_x", 0 if states.get('show_toggle_sidebar') else -48)

    async def handle_file_click(self, message: FileClick) -> None:
        """A message sent by the directory tree when a file is clicked."""




