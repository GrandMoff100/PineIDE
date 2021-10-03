from os.path import abspath, basename, join

from rich.console import RenderableType
from rich.syntax import Syntax
from rich.traceback import Traceback

from textual.app import App
from textual.widgets import Header, Footer, FileClick, ScrollView, DirectoryTree


class PineIDE(App):
    """The PineIDE app class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = abspath(join(basename(__file__), "../../../"))
        self.foot = Footer()
        self.head = Header()
        self.directory = DirectoryTree(self.path, "Code")
        self.body = ScrollView()

    async def on_load(self) -> None:
        """Sent before going in to application mode."""

        await self.bind("b", "view.toggle(sidebar)", "Toggle File View")
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:
        """Call after terminal goes in to application mode"""

        await self.view.dock(self.head, edge="top")
        await self.view.dock(self.foot, edge="bottom")

        # Note the directory is also in a scroll view
        await self.view.dock(
            ScrollView(self.directory), edge="left", size=48, name="sidebar"
        )
        await self.view.dock(self.body, edge="top")

    async def handle_file_click(self, message: FileClick) -> None:
        """A message sent by the directory tree when a file is clicked."""

        syntax: RenderableType
        try:
            # Construct a Syntax object for the path in the message
            syntax = Syntax.from_path(
                message.path,
                line_numbers=True,
                word_wrap=True,
                indent_guides=True,
                theme="monokai",
            )
        except Exception:
            syntax = Traceback(theme="monokai", width=None, show_locals=True)
        self.app.sub_title = basename(message.path)
        await self.body.update(syntax)



