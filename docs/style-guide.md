# Visual Style Guide

A reference for the color palette, typography, spacing, and UI patterns used across this project.

---

## Color Palette

### Backgrounds

| Role                       | Value                 | Notes                       |
| -------------------------- | --------------------- | --------------------------- |
| Page / app background      | `#1a1a1a`             | Darkest level               |
| Panel / sidebar background | `#1e1e1e`             | Slightly lighter            |
| Surface / card background  | `#2a2a2a`             | Input fields, tags, buttons |
| Elevated surface           | `#242424`             | Hover rows, subtle lift     |
| Hover state                | `#252525` – `#363636` | Slight lift on hover        |
| Divider / separator        | `#2a2a2a` – `#333`    | Borders between sections    |

### Text

| Role                     | Value     |
| ------------------------ | --------- |
| Primary text             | `#e0e0e0` |
| Secondary / label text   | `#ccc`    |
| Muted / placeholder      | `#aaa`    |
| Disabled / very muted    | `#666`    |
| Heading / white emphasis | `#fff`    |
| Body (row items)         | `#ddd`    |

### Brand / Accent

| Role                          | Value                 |
| ----------------------------- | --------------------- |
| Primary accent (green)        | `#2dbe6c`             |
| Primary accent hover          | `#33d977`             |
| Primary accent (dark bg tint) | `#1a3d2a`             |
| Cyan accent                   | `#00d4c8`             |
| Cyan accent (dark bg tint)    | `#0d2a2a` / `#1a4040` |
| Editor pin / info blue        | `#22d3ee`             |
| Purple accent                 | `#a78bfa`             |
| Purple accent (dark bg tint)  | `#1a1a2a`             |

### Semantic States

| State                 | Foreground | Background | Border    |
| --------------------- | ---------- | ---------- | --------- |
| Success / complete    | `#2dbe6c`  | `#1a3d2a`  | `#2dbe6c` |
| Warning / orange      | `#e09050`  | `#2a1a10`  | `#e09050` |
| Error / danger (soft) | `#e74c3c`  | `#2a1010`  | `#7a2020` |
| Error / danger (bold) | `#ff6b6b`  | —          | `#e74c3c` |

---

## Typography

### Font Stack

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
```

Monospace (coordinates, debug overlays):

```css
font-family: monospace;
```

### Font Sizes

| Role                       | Size   |
| -------------------------- | ------ |
| Panel heading              | `18px` |
| Body / default             | `14px` |
| Secondary labels / filters | `13px` |
| Tags / badges              | `12px` |
| Fine print / footnotes     | `11px` |

---

## Spacing

The project uses a loose 4px base grid.

| Use                      | Value                     |
| ------------------------ | ------------------------- |
| Tight gap (icon + label) | `4px`                     |
| Standard gap             | `8px`                     |
| Medium gap               | `10px`                    |
| Large gap                | `16px`                    |
| Data table row height    | User setting, `20–64px`   |
| Panel section padding    | `10px 16px` – `14px 16px` |
| Input padding            | `7px 10px`                |
| Tag/badge padding        | `2px 8px`                 |
| Small button padding     | `3px 12px`                |
| Button padding           | `6px 14px`                |

---

## Borders & Radius

| Element                    | Radius        |
| -------------------------- | ------------- |
| Inputs, dropdowns          | `4px`         |
| Buttons                    | `3px` – `4px` |
| Pill badges / tags         | `12px`        |
| Tooltips / floating panels | `5px` – `6px` |
| Progress / bar elements    | `3px`         |

Standard border color: `1px solid #444` (default), `#333` (panel edges), `#555` (interactive borders).

Focus border: `#666`.

---

## Components

### Buttons

**Default (ghost)**

```css
background: #2a2a2a;
color: #aaa;
border: 1px solid #555;
border-radius: 4px;
font-size: 13px;
padding: 6px 14px;
```

**Hover**

```css
background: #363636;
color: #fff;
```

**Active / selected (primary green)**

```css
background: #2dbe6c;
color: #000;
border-color: #2dbe6c;
```

**Active hover**

```css
background: #33d977;
border-color: #33d977;
```

---

### Inputs & Selects

```css
background: #2a2a2a;
border: 1px solid #444;
border-radius: 4px;
color: #e0e0e0;
padding: 7px 10px;
```

Focus:

```css
border-color: #666;
```

Checkbox / radio accent color: `#2dbe6c`

---

### Panels / Sidebars

```css
background: #1e1e1e;
border-right: 1px solid #333;
```

Section header:

```css
padding: 14px 16px 10px;
border-bottom: 1px solid #333;
font-size: 18px;
color: #fff;
```

Section divider:

```css
border-bottom: 1px solid #2a2a2a;
```

---

### Tags / Badges

Default:

```css
padding: 2px 8px;
border-radius: 12px;
font-size: 12px;
background: #2a2a2a;
color: #aaa;
border: 1px solid #444;
```

Active (green):

```css
background: #1a3d2a;
color: #2dbe6c;
border-color: #2dbe6c;
```

Active (cyan):

```css
background: #0d2a2a;
color: #00d4c8;
border-color: #1a4040;
```

Active (orange):

```css
background: #2a1a10;
color: #e09050;
border-color: #e09050;
```

---

### Floating / Overlay Panels

```css
background: rgba(20, 20, 20, 0.92);
border: 1px solid #333;
border-radius: 5px;
padding: 10px 14px;
```

Dark overlay (map):

```css
background: rgba(0, 0, 0, 0.7);
color: #ccc;
border-radius: 3px;
padding: 4px 8px;
font-family: monospace;
font-size: 12px;
```

---

### Scrollbars

```css
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: #2a2a2a;
}
::-webkit-scrollbar-thumb {
  background: #444;
  border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
  background: #555;
}
```

---

### Selected Row (tree / list)

```css
box-shadow:
  inset 3px 0 0 #2dbe6c,
  0 0 0 1px rgba(45, 190, 108, 0.25);
background: #252525;
```

---

## Design Principles

- **Dark-first.** All UI is dark mode only; no light mode variant (cuz I like not to flashbang my self).
- **Flat surfaces.** No gradients or drop shadows on static UI elements. Shadows only on floating/overlay panels.
- **Green as the single primary accent.** `#2dbe6c` drives all interactive affordances (checkboxes, active states, progress).
- **Muted by default, bright on interaction.** Resting text is `#aaa`–`#ccc`; active/selected states elevate to `#fff` or the accent color.
- **Consistent border hierarchy.** `#333` for outer panel walls → `#444` for inputs/cards → `#2a2a2a` for in-panel row separators.
