from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.html import Column, e, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from .parser import PROPERTY_NAMES, WaypointGraph, is_waypoint_graph, neighbours, parse_waypoint_graph


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 8
def _records(graph: WaypointGraph) -> list[dict]:
    linked = neighbours(graph)
    records: list[dict] = []
    for waypoint in graph.waypoints:
        links = sorted(linked.get(waypoint.key, ()))
        records.append({
            "key": waypoint.key,
            "name": waypoint.name,
            "x": waypoint.x,
            "y": waypoint.y,
            "z": waypoint.z,
            "property": waypoint.property,
            "property_name": PROPERTY_NAMES.get(waypoint.property, f"0x{waypoint.property:02X}"),
            "is_sub_waypoint": waypoint.is_sub_waypoint,
            "is_escape": waypoint.is_escape,
            "links": links,
            # Empty sorts last.
            "link_count": len(links) or None,
        })
    return records


class WaypointBwpHandler(PreviewHandler):
    def _strings(self) -> dict:
        return load_handler_strings(self.lang, _LANG_DIR)

    def _columns(self) -> list[Column]:
        cols = self._strings()["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["x"], "num", sort_key="x"),
            Column(cols["y"], "num", sort_key="y"),
            Column(cols["z"], "num", sort_key="z"),
            Column(cols["property"], sort_key="property_name"),
            Column(cols["subWaypoint"], sort_key="is_sub_waypoint"),
            Column(cols["links"], sort_key="link_count"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        # The old instance dungeon templates are left unread: they hold no data
        # (see the Notes of docs/file-formats/other/waypoint_bwp.md).
        if not is_waypoint_graph(data):
            return []
        return _records(parse_waypoint_graph(data))

    def render_data_page(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        page: int,
        page_size: int,
    ) -> str:
        if not is_waypoint_graph(data):
            return self._old_layout_page()
        return super().render_data_page(data, entry, companions, page, page_size)

    def render_sorted_page(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        page: int,
        page_size: int,
        sort: TableSort,
    ) -> str:
        # The table opens sorted by default, so the old-layout notice is needed here too.
        if not is_waypoint_graph(data):
            return self._old_layout_page()
        return super().render_sorted_page(data, entry, companions, page, page_size, sort)

    def _old_layout_page(self) -> str:
        meta = self._strings()["messages"]["oldLayout"]
        return table(meta, self._columns(), [])

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        values = self._strings()["values"]
        yes, no = values["yes"], values["no"]
        # Every linked pair is listed on both of its waypoints.
        links = sum(record["link_count"] or 0 for record in records)
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), links=links // 2)
        rows = [
            [
                e(record["key"]),
                e(record["name"] or _EMPTY),
                e(f"{record['x']:,.1f}"),
                e(f"{record['y']:,.1f}"),
                e(f"{record['z']:,.1f}"),
                e(record["property_name"]),
                e(yes if record["is_sub_waypoint"] else no),
                text_list_cell(record["links"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for record in slice_
        ]
        return table(meta, self._columns(), rows)
