# titleoffset.dbss Format

## Purpose

Maps title IDs to their location inside `title.dbss`.

## Record Structure

| Offset | Type | Name     | Description                 |
| ------ | ---- | -------- | --------------------------- |
| +0x00  | u32  | title_id | Title identifier            |
| +0x04  | u32  | offset   | Byte offset into title.dbss |
| +0x08  | u32  | size     | Block size                  |

## Example

title_id: 3161
offset: 676622
size: 296

## Usage

title_id → lookup offset → read block from title.dbss

## Open Questions

- None currently
