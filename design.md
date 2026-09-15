# Quiz Master Premium Frontend Design

## Design Direction

Quiz Master should feel like a focused study command center: polished, calm, and credible, while still being simple enough for a college project. The premium cue is not heavy animation or complicated UI; it is crisp hierarchy, disciplined spacing, strong contrast, and dashboards that make content feel managed.

## Token System

### Color

- `Obsidian` `#111827` for navigation, hero depth, and primary text.
- `Porcelain` `#F7F4EE` for the main page background.
- `Paper` `#FFFFFF` for cards and table surfaces.
- `Mist` `#E8EEF2` for soft borders and quiet bands.
- `Verdigris` `#0F766E` for primary actions and active states.
- `Saffron` `#D89A2B` for premium highlights and dashboard accents.

### Type

- Display and interface: `Manrope`, chosen for a modern academic-product feel with clear numerals.
- Body fallback: system sans-serif stack for reliability if the web font fails.
- Headings use strong weight and tight hierarchy, but no oversized dashboard text.

### Layout

Landing page:

```text
┌─────────────────────────────────────────────┐
│ brand                         login action  │
│                                             │
│ big promise             live quiz preview   │
│ supporting copy         score strip/cards   │
│ primary action                              │
│                                             │
│ feature rail peeks below first viewport     │
└─────────────────────────────────────────────┘
```

Admin dashboard:

```text
┌─────────────────────────────────────────────┐
│ nav                                         │
│ heading + action                            │
│ metric strip                                │
│ subject panels with chapters table          │
└─────────────────────────────────────────────┘
```

User dashboard:

```text
┌─────────────────────────────────────────────┐
│ nav                                         │
│ heading + readiness summary                 │
│ available quiz cards                        │
└─────────────────────────────────────────────┘
```

Content stays mostly left aligned for speed and seriousness. The landing page uses a split hero only because the product benefits from an immediate preview of the quiz-taking experience.

## Principles

- Make the first screen useful, not decorative.
- Use cards only for real objects: quizzes, subjects, stats, preview panels.
- Keep copy short and functional.
- Let contrast and spacing create the premium feeling.
- Use no gradients; premium styling should come from solid surfaces, spacing, borders, and shadows.
- Avoid adding backend complexity; use existing Jinja data wherever possible.

## Implementation Notes

- The redesign is implemented in `static/css/main.css`.
- Landing page structure is in `templates/home.html`.
- Dashboard structure is in `templates/admin_dashboard.html` and `templates/user_dashboard.html`.
- Navigation markup remains simple but receives stronger visual treatment.
