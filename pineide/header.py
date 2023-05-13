"""Provides a Textual application header widget."""

from __future__ import annotations

from datetime import datetime

from rich.text import Text

from textual.app import RenderResult
from textual.events import Mount
from textual.reactive import Reactive
from textual.widget import Widget


class Icon(Widget):
    """Display an 'icon' on the left of the header."""

    icon = Reactive("")

    def render(self) -> RenderResult:
        return Text.from_markup(self.icon)


class Title(Widget):
    """Display the title / subtitle in the header."""

    text: Reactive[str] = Reactive("")
    sub_text = Reactive("")

    def render(self) -> RenderResult:
        text = Text(self.text, no_wrap=True, overflow="ellipsis")
        if self.sub_text:
            text.append(" — ")
            text.append(self.sub_text, "dim")
        return text


class PineHeader(Widget):
    """A header widget with icon and clock."""

    def __init__(
        self,
        *,
        name: str | None = None,
        id: str | None = None,
    ):
        super().__init__(name=name, id=id)

    def compose(self):
        yield Icon()
        yield Title()

    def _on_mount(self, _: Mount) -> None:
        def set_title(title: str) -> None:
            self.query_one(Title).text = str(title)

        def set_sub_title(sub_title: str) -> None:
            self.query_one(Title).sub_text = str(sub_title)
        
        def set_icon(icon: str) -> None:
            self.query_one(Icon).icon = icon

        self.watch(self.app, "title", set_title)
        self.watch(self.app, "sub_title", set_sub_title)
        self.watch(self.app, "icon", set_icon)