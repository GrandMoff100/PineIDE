import datetime

from textual.widget import Widget
from textual import events
from textual.reactive import watch, Reactive

from rich.table import Table


class CustomHeader(Widget):
    style = Reactive("#ffffff on #222222")

    def __init__(self):
        super().__init__()
        self.started_at = datetime.datetime.now()

    def calculate_time_elapsed(self):
        delta = datetime.datetime.now().replace(microsecond=0) - self.started_at.replace(microsecond=0)
        return str(delta).split('.')[0]

    def render(self):
        header_table = Table.grid(expand=True)
        header_table.style = self.style
        header_table.add_column(justify="left", ratio=0, width=12)
        header_table.add_column("title", justify="center", ratio=1)
        header_table.add_column("time_elapsed", justify="right", width=12)
        header_table.add_row(
            "PineIDE :evergreen_tree:", "<opened_file>", self.calculate_time_elapsed()
        )
        return header_table

    async def on_mount(self, event: events.Mount) -> None:
        self.set_interval(1.0, callback=self.refresh)

        async def set_title(title: str) -> None:
            self.title = title

        async def set_sub_title(sub_title: str) -> None:
            self.sub_title = sub_title

        watch(self.app, "title", set_title)
        watch(self.app, "sub_title", set_sub_title)

