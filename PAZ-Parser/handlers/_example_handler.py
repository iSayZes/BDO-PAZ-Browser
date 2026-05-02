# Example custom handler — rename to something like myformat_handler.py and implement.
#
# Drop any *.py file (not starting with _) here and it is loaded at browser startup.
# Each file can call register_handler() for one or more filenames or extensions.
#
# Keys:
#   "somefile.dbss"  — exact filename match (checked first)
#   ".dbss"          — extension fallback (used if no filename match exists)
#
# Companion files:
#   Override companions() to declare additional files the handler needs.
#   The browser will load them from the PAZ archive (by internal path) and pass
#   them to render() in the `companions` dict, keyed by filename (basename).
#   Disk files pre-loaded by the browser (e.g. languagedata_en.loc, located at
#   <paz_folder_parent>/ads/languagedata_en.loc) are also merged in automatically.
#
# from __future__ import annotations
# import html
# from pathlib import Path
# from bdo_models import PazEntry
# from bdo_preview import PreviewHandler, register_handler
#
#
# class MyHandler(PreviewHandler):
#
#     def companions(self, entry: PazEntry) -> list[str]:
#         # Return internal PAZ paths of files needed alongside the main file.
#         # folder = entry.internal_path.rsplit("/", 1)[0]
#         # return [f"{folder}/myindex.dbss"]
#         return []
#
#     def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
#         # companions["myindex.dbss"]        — PAZ-internal companion (if loaded)
#         # companions["languagedata_en.loc"]  — pre-loaded disk file (if found)
#         #
#         # Return an HTML string to display in the preview panel.
#         # Use html.escape() on any user-visible data.
#         return f'<div>{len(data):,} bytes</div>'
#
#
# register_handler("myfile.myext", MyHandler())   # by filename
# register_handler(".myext",       MyHandler())   # by extension (fallback)
