# Visual Style Guide

The UI's colors, type, spacing and icons. Every value is a CSS custom property
in `PAZ-Parser/ui/css/00-reset-root.css`; component stylesheets use the
properties, never raw hex values. Game-data colors (item grades, worker grades,
`<PAColor>` text) are the exception and stay as the client defines them.

## Color

### Surfaces and Lines

| Token                 | Value     | Use                                         |
| --------------------- | --------- | ------------------------------------------- |
| `--color-bg`          | `#121316` | Window background, inputs                   |
| `--color-sidebar`     | `#16181b` | Sidebar, bars under a panel header          |
| `--color-surface`     | `#191b1f` | Panels, cards, modals                       |
| `--color-row-alt`     | `#1c1e22` | Alternate table rows                        |
| `--color-raised`      | `#212429` | Buttons, table headers                      |
| `--color-hover`       | `#2a2e34` | Hovered buttons and rows                    |
| `--color-line`        | `#2c3036` | Panel edges, row separators                 |
| `--color-line-strong` | `#3a3f47` | Button and input borders                    |
| `--color-line-hover`  | `#4a505a` | Hovered borders                             |

### Text

| Token                 | Value     | Use                                         |
| --------------------- | --------- | ------------------------------------------- |
| `--color-text-strong` | `#ffffff` | Hovered and selected labels                 |
| `--color-text`        | `#e8e6e1` | Body text, values                           |
| `--color-text-soft`   | `#c9c7c2` | Labels, tree names                          |
| `--color-text-2`      | `#a9adb4` | Secondary text, button labels               |
| `--color-text-3`      | `#80858d` | Captions, placeholders, counts              |
| `--color-disabled`    | `#5c6168` | Disabled controls                           |

### Accent and Meaning

| Token                  | Value                    | Use                                                  |
| ---------------------- | ------------------------ | ---------------------------------------------------- |
| `--color-accent`       | `#e2a94f`                | Selection, focus rings, primary buttons, progress    |
| `--color-accent-hover` | `#edbb69`                | Hovered primary buttons                              |
| `--color-accent-soft`  | `rgba(226, 169, 79, 0.14)` | Selected rows and chips behind accent text         |
| `--color-on-accent`    | `#1a1408`                | Text on an accent background                         |
| `--color-data`         | `#5bc8a8`                | Parsed-table icons, offsets and values in details    |
| `--color-loc`          | `#b79cf0`                | LOC file icons                                       |
| `--color-warning`      | `#f07b3f`                | Warnings, such as a missing LOC file                 |
| `--color-danger`       | `#e5484d`                | Errors and destructive buttons                       |

Warning and danger differ from the accent in hue and lightness, so a warning
border never reads as a focus ring.

## Type

| Token         | Stack                                                          |
| ------------- | -------------------------------------------------------------- |
| `--font-sans` | `"IBM Plex Sans", "Malgun Gothic", "Segoe UI", system-ui, sans-serif` |
| `--font-mono` | `"IBM Plex Mono", Consolas, "Malgun Gothic", monospace`        |

IBM Plex Sans (400, 500, 600) and Plex Mono (400, 500) ship in
`PAZ-Parser/ui/fonts/` under the SIL Open Font License (`OFL.txt` there), so
the app needs no network for fonts. They cover Latin and Cyrillic; Malgun
Gothic, which Windows ships, draws Korean, including table text that falls
back to Korean when a LOC file is missing. `index.html` links
`fonts/fonts.css` on its own; `--render` pages inline `style.css` only and fall
back through the stack.

Monospace is for byte offsets, sizes, paths, hex and IDs. Body text is 13px.

## Spacing and Radius

Spacing steps are `--space-1` to `--space-7`: 4, 8, 12, 16, 24, 32 and 48px.

| Token              | Value   | Use                                 |
| ------------------ | ------- | ----------------------------------- |
| `--radius-inner`   | `4px`   | Segments inside a control           |
| `--radius-control` | `7px`   | Buttons and inputs                  |
| `--radius-card`    | `10px`  | Panels                              |
| `--radius-modal`   | `14px`  | Dialogs                             |
| `--radius-pill`    | `999px` | Chips and badges                    |

Table row height is a user setting from 20 to 64px (`--table-row-height`).

## Controls

`PAZ-Parser/ui/css/08-controls.css` styles the shared controls; a component
adds its own rules only for layout.

| Class           | Use                                                                  |
| --------------- | -------------------------------------------------------------------- |
| `button`        | Raised button: `--color-raised` fill, `--radius-control`, 2px accent focus ring |
| `.btn-primary`  | The one main action of a bar or dialog: accent fill, `--color-on-accent` text |
| `.icon-button`  | 30px square button with only an icon; it needs an `aria-label`     |
| `.input-box`    | A label wrapping an icon or caption and an input; accent border and ring on focus |
| `.segmented`    | Two or three exclusive buttons in one track; the chosen one has `.active` |
| `.with-icon`    | Inline-flex row for an icon before its label                         |

Disabled buttons drop their fill and use `--color-disabled`.

## Icons

Icons are one SVG sprite built by `PAZ-Parser/ui/js/core/icons.js`: 24px grid,
1.75 stroke, drawn in `currentColor`, with paths from Lucide (ISC License,
notice in that file). Static markup uses
`<svg class="icon"><use href="#icon-NAME"></use></svg>`; JS uses `iconSvg()`
or `iconElement()`. A button with an icon and a translated label keeps the
label in its own `<span data-i18n>`, because `applyI18n()` replaces the text
of the element that carries `data-i18n`.

The file tree gets its icon names from `_file_icon()` in
`PAZ-Parser/api/bdo_api_helpers.py`: `loc` for LOC files, `parsed` for any
file a registered handler reads, then by extension `image`, `code`, `text`,
`video` and `archive` (`.pac`), and `file` for the rest, including a `.bss` or
`.dbss` without a handler. Folder icons use the accent, parsed tables
`--color-data`, LOC files `--color-loc`, the rest `--color-text-3`; `file` rows
also grey their name to `--color-text-2`.

The UI uses no emoji, in markup or in `ui/lang/*.json`.

## Principles

- Dark only, with no light theme.
- Flat surfaces. Shadows only on floating panels: modals, toasts, menus.
- One accent. Amber marks what is selected, focused or the primary action;
  color with meaning (data, LOC, warning, danger) never doubles as decoration.
- Muted at rest, brighter on interaction: resting labels use `--color-text-2`
  or `--color-text-soft`, hovered and selected ones `--color-text-strong` or
  the accent.
