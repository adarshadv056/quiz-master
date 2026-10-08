# Quiz Master — Design System

**Version:** 1.0  
**Product:** Quiz Master — Premium EdTech / Quiz Platform  
**Purpose:** Visual design system for the frontend redesign of the IITM Modern Application Development I Quiz Master project.

---

## 1. Design Direction

### Product Personality

Quiz Master should feel like a **premium EdTech SaaS product with a playful edge**.

The visual direction combines:

- Modern SaaS dashboards
- Premium learning platforms
- Clean quiz interfaces
- Playful educational illustrations
- Subtle gradients
- Smooth micro-interactions
- Strong visual hierarchy
- Spacious layouts

The goal is to make the project feel like a **real production product**, not a typical college assignment.

### Design Keywords

> Clean · Premium · Playful · Modern · Educational · Interactive · Spacious · Trustworthy

### Reference Influence

The system takes inspiration from three visual directions:

1. **Modern quiz interfaces**
   - Clear question progress
   - Answer states
   - Question navigation
   - Score panels
   - Focused quiz-taking experience

2. **Playful EdTech interfaces**
   - Educational illustrations
   - Friendly onboarding
   - Purple/blue visual identity
   - More personality and warmth

3. **Premium SaaS websites**
   - Large typography
   - Spacious sections
   - Strong hero sections
   - Floating UI visuals
   - Subtle gradients
   - Visual storytelling
   - Refined animations

**Important:** These references are inspiration only. Quiz Master should have its own visual identity.

---

# 2. Color System

## Primary Colors

| Token | Color | Usage |
|---|---|---|
| Primary 600 | `#4F46E5` | Primary buttons, active states, links |
| Primary 500 | `#6366F1` | Secondary emphasis, gradients |
| Primary 400 | `#818CF8` | Decorative elements |
| Primary 100 | `#E0E7FF` | Selected/soft backgrounds |
| Primary 50 | `#EEF2FF` | Very subtle primary backgrounds |

### Brand Gradient

```css
linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
```

Use the gradient selectively for:

- Hero areas
- Primary CTAs
- Score highlights
- Decorative elements
- Visual illustrations
- Important emphasis

Do **not** use gradients on every component.

---

## Accent Colors

| Token | Color | Usage |
|---|---|---|
| Purple | `#8B5CF6` | Secondary accent |
| Cyan | `#06B6D4` | Information / subject accent |
| Green | `#22C55E` | Correct answers / success |
| Amber | `#F59E0B` | Warnings / attention |
| Red | `#EF4444` | Incorrect / destructive states |

Accent colors should support the interface rather than dominate it.

---

## Neutral Colors

| Token | Color | Usage |
|---|---|---|
| Background | `#F8FAFC` | Application background |
| Surface | `#FFFFFF` | Cards / panels |
| Surface Subtle | `#F1F5F9` | Secondary surfaces |
| Text Primary | `#0F172A` | Main text |
| Text Secondary | `#475569` | Supporting text |
| Text Muted | `#94A3B8` | Metadata / placeholders |
| Border | `#E2E8F0` | Borders / dividers |

---

# 3. Typography

## Font

Primary font:

**Plus Jakarta Sans**

Fallback:

```css
font-family: "Plus Jakarta Sans", Inter, sans-serif;
```

The typography should feel modern and slightly premium while remaining highly readable.

## Type Scale

| Element | Size | Weight |
|---|---:|---:|
| Display | 48–64px | 700 |
| H1 | 40–48px | 700 |
| H2 | 30–36px | 700 |
| H3 | 22–24px | 650 |
| Body | 15–16px | 400–500 |
| Small | 13–14px | 400–500 |
| Caption | 12px | 400–500 |

Large headings should be used mainly for marketing/hero sections.

Dashboard pages should use more restrained typography.

---

# 4. Spacing

Use a consistent spacing system.

Recommended base spacing:

```text
4px
8px
12px
16px
20px
24px
32px
40px
48px
64px
80px
96px
120px
```

## Section Spacing

| Type | Spacing |
|---|---:|
| Small | 64px |
| Medium | 96px |
| Large | 120px |

Avoid cramped layouts. Premium design depends heavily on whitespace.

---

# 5. Border Radius

| Token | Radius |
|---|---:|
| XS | 6px |
| SM | 8px |
| MD | 12px |
| LG | 16px |
| XL | 20px |
| 2XL | 24px |
| Pill | 999px |

Recommended usage:

- Buttons: 10–12px
- Cards: 16–20px
- Large panels: 24px
- Badges/tags: pill
- Inputs: 10–12px

Do not make every component extremely rounded.

---

# 6. Shadows

Shadows should be subtle.

```css
/* Small */
0 1px 2px rgba(15, 23, 42, 0.04);

/* Card */
0 8px 30px rgba(15, 23, 42, 0.06);

/* Hover */
0 15px 40px rgba(15, 23, 42, 0.10);
```

Prefer borders + subtle shadows over heavy shadows.

---

# 7. Layout

## Maximum Width

Marketing/public pages:

```text
1200–1280px
```

## Dashboard

Recommended structure:

```text
Sidebar: 240–260px
Main:    Remaining width
```

Dashboard layouts should use generous internal spacing.

---

# 8. Navigation

## Public Navbar

Recommended structure:

```text
Quiz Master

Home    Explore Quizzes    How it Works    About

                         Login   Get Started
```

The navbar should be:

- Minimal
- Sticky
- Responsive
- Slightly translucent when scrolling

Suggested scroll state:

```css
background: rgba(255, 255, 255, 0.82);
backdrop-filter: blur(16px);
border-bottom: 1px solid #E2E8F0;
```

---

# 9. Dashboard Sidebar

User navigation:

```text
QUIZ MASTER

OVERVIEW
  Dashboard
  Explore Quizzes
  My Attempts

LEARNING
  Subjects
  Progress

──────────────

Settings
Logout
```

Active navigation item:

```text
background: #EEF2FF;
color: #4F46E5;
```

The sidebar should feel lightweight rather than visually heavy.

---

# 10. Hero Design

The landing page should follow a **premium SaaS hero** approach.

### Primary message

Example:

> **Test your knowledge.  
> Know where you stand.**

Supporting text:

> Practice smarter with quizzes designed to help you learn, improve and track your progress.

Primary CTA:

```text
Explore Quizzes →
```

### Hero Visual

Use a visual composition rather than a generic stock image.

Possible floating elements:

- Question card
- Score card
- Progress chart
- Quiz category badge
- Achievement card
- Progress indicator

These elements can have subtle floating animations.

---

# 11. Backgrounds & Decorative Elements

Primary application background:

```text
#F8FAFC
```

Use subtle decorative gradients:

```css
radial-gradient(
  circle at 50% 0%,
  rgba(99, 102, 241, 0.12),
  transparent 50%
);
```

Possible decorative elements:

- Soft gradient blobs
- Dotted grids
- Thin curved lines
- Tiny sparkles
- Abstract indigo shapes

Decorations must remain subtle and should never interfere with readability.

---

# 12. Cards

Cards should use:

```text
Background: #FFFFFF
Border: #E2E8F0
Radius: 16–20px
Shadow: subtle
```

Cards should have clear hierarchy.

Avoid putting every piece of content into a separate card.

---

# 13. Subject Cards

Example structure:

```text
┌──────────────────────────────┐
│  Icon                         │
│                              │
│  Data Structures              │
│  12 quizzes · 8 chapters      │
│                              │
│  Progress                     │
│  ███████████░░ 78%            │
│                              │
│  Explore →                    │
└──────────────────────────────┘
```

Subjects may use different accent colors:

- Data Science → Indigo
- Web Development → Cyan
- Python → Green
- Mathematics → Amber

The component structure must remain consistent.

---

# 14. Quiz Interface

The quiz-taking interface is one of the most important screens.

## Header

```text
Quiz Master                              ⏱ 08:42

Data Structures
Chapter 03 · Arrays
```

## Progress

```text
Question 7 of 20

██████████████░░░░░░ 35%
```

## Question

Questions should use large, highly readable text.

## Answer Options

Options should be interactive cards instead of default radio buttons.

Example:

```text
┌─────────────────────────────────────────┐
│ A    Stack                              │
└─────────────────────────────────────────┘
```

Selected state:

```text
border: #4F46E5;
background: #EEF2FF;
```

The selected option should have clear visual feedback.

---

# 15. Question Navigator

Use a compact question grid:

```text
QUESTIONS

01  02  03  04  05
06  07  08  09  10
11  12  13  14  15
```

States:

| State | Color |
|---|---|
| Answered | Green |
| Current | Indigo |
| Unanswered | Gray |
| Incorrect | Red |

---

# 16. Result Screen

The result page should feel like a real analytics experience.

Example:

```text
87%

Excellent work!

You answered 17 of 20 questions correctly.
```

Statistics:

```text
Correct       17
Incorrect      3
Time       08:42
```

Then show:

- Donut chart
- Performance breakdown
- Previous attempt comparison
- Subject/chapter performance
- Recommended next quiz

The result page should visually communicate achievement without becoming overly gamified.

---

# 17. Admin Dashboard

The admin UI uses the same design system but is more information-dense.

Example:

```text
Good morning, Quiz Master 👋

Here's what's happening with your platform.

┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
│ 1,248      │ │ 84         │ │ 312        │ │ 76%        │
│ Users      │ │ Quizzes    │ │ Attempts   │ │ Avg Score  │
└────────────┘ └────────────┘ └────────────┘ └────────────┘
```

Analytics can include:

- Quiz activity
- User growth
- Popular subjects
- Average scores
- Recent attempts

---

# 18. Tables

Avoid default Bootstrap tables.

Use a clean SaaS table style:

```text
┌─────────────────────────────────────────────────────────┐
│ Quiz             Subject       Questions       Actions │
├─────────────────────────────────────────────────────────┤
│ Python Basics    Python        20              •••     │
│ Arrays & Strings DSA           15              •••     │
│ React Basics     Web Dev       25              •••     │
└─────────────────────────────────────────────────────────┘
```

Actions can include:

```text
Edit
View
Duplicate
Delete
```

---

# 19. Forms

Forms should use clear hierarchy.

Example:

```text
Create Subject

Subject name
[ Data Structures                         ]

Description
[ Learn fundamental data structures...    ]

                    Cancel   Create Subject
```

Requirements:

- Visible labels
- Helpful descriptions
- Clear focus state
- Inline validation
- Clear error messages
- Consistent button placement

---

# 20. Authentication Pages

Login/register should use a split-screen premium layout.

### Left side

Branded visual:

> **Learn. Practice. Master.**

Include:

- Quiz illustration
- Floating UI elements
- Brand gradient
- Subtle animation

### Right side

Clean form:

```text
Welcome back

Sign in to continue your learning journey.

Email
[________________________]

Password
[________________________]

Forgot password?

[        Sign In →        ]

Don't have an account?
Create one
```

The authentication experience should remain simple and focused.

---

# 21. Icons

Use **Lucide Icons** consistently.

Recommended:

```text
stroke-width: 1.8–2
```

Do not mix multiple icon libraries unnecessarily.

Avoid using emojis as the primary UI icon system.

---

# 22. Illustrations & Visual Assets

Use illustrations strategically.

### Landing page

Large educational/quiz illustration.

### Empty states

Small contextual illustrations.

### Quiz completion

Celebration/achievement illustration.

### Authentication

One strong branded illustration.

### 404

Small playful quiz-related illustration.

Visual assets should use a consistent illustration style.

---

# 23. Animation System

Animations should feel smooth and purposeful.

## Page Entrance

```text
opacity: 0 → 1
translateY: 12px → 0
duration: 400ms
```

## Card Hover

```text
translateY(-3px)
shadow increases
```

## Buttons

```text
scale(1.02)
```

## Quiz Options

On selection:

- Border transition
- Background transition
- Check icon appears

## Charts

Charts can animate when entering the viewport.

## Hero Floating Elements

Use gentle infinite movement:

```text
6–8 seconds
ease-in-out
infinite
```

---

# 24. Motion Timing

| Type | Duration |
|---|---:|
| Fast | 150ms |
| Normal | 250ms |
| Smooth | 400ms |
| Reveal | 600ms |

### Motion rule

> If an animation does not communicate interaction, hierarchy, state, or feedback, do not add it.

Animations should enhance the experience rather than distract from the quiz.

---

# 25. Buttons

## Primary

```text
[ Start Quiz → ]
```

Indigo background.

## Secondary

```text
[ Explore Quizzes ]
```

White background + border.

## Ghost

```text
[ View all ]
```

Transparent.

## Destructive

```text
[ Delete Quiz ]
```

Red.

Avoid creating many visually different button styles.

---

# 26. Reusable Components

The design system should be implemented through reusable components.

Core components:

```text
Button
Badge
Avatar
Tooltip
Modal
Dropdown
Input
Select
Textarea
Card
StatCard
SubjectCard
QuizCard
ProgressBar
ProgressRing
ChartCard
EmptyState
Toast
Sidebar
Navbar
Breadcrumb
QuestionOption
QuestionNavigator
QuizTimer
ScoreCard
```

Reusable components ensure the entire application remains visually consistent.

---

# 27. CSS Design Tokens

The design system should be represented through CSS variables.

```css
:root {
  --primary: #4F46E5;
  --primary-hover: #4338CA;
  --primary-soft: #EEF2FF;

  --background: #F8FAFC;
  --surface: #FFFFFF;

  --text-primary: #0F172A;
  --text-secondary: #475569;
  --text-muted: #94A3B8;

  --border: #E2E8F0;

  --success: #22C55E;
  --warning: #F59E0B;
  --danger: #EF4444;

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 20px;

  --shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.04);
  --shadow-card: 0 8px 30px rgba(15, 23, 42, 0.06);

  --transition-fast: 150ms;
  --transition-normal: 250ms;
  --transition-smooth: 400ms;
}
```

---

# 28. Responsive Design

The application must work well on:

- Desktop
- Laptop
- Tablet
- Mobile

### Mobile principles

- Sidebar becomes a drawer/bottom navigation where appropriate
- Cards stack vertically
- Tables become scrollable or transform into cards
- Quiz options become single-column
- Question navigator becomes collapsible
- Hero typography scales down
- Decorative visuals reduce on small screens

Do not simply shrink the desktop layout.

---

# 29. Accessibility

The redesign must maintain usable accessibility.

Requirements:

- Sufficient color contrast
- Visible keyboard focus
- Semantic HTML
- Proper form labels
- Buttons should have clear labels
- Interactive elements should have accessible states
- Do not rely only on color to communicate correct/incorrect answers
- Respect `prefers-reduced-motion`

---

# 30. Implementation Philosophy

The existing application is built around:

- Flask
- Jinja2
- HTML
- CSS
- Bootstrap
- SQLite

The redesign should **not unnecessarily replace the backend or application architecture**.

Bootstrap can remain available, but the Quiz Master design system should provide the visual layer.

The goal is:

> **Preserve functionality. Replace the visual experience.**

Existing routes, models, database logic and quiz functionality should remain stable unless a change is explicitly required.

---

# 31. Page Design Roadmap

The redesign should be implemented in this order:

1. Design tokens / global CSS
2. Base typography
3. Navbar
4. Buttons / inputs / cards
5. Public landing page
6. Login
7. Register
8. User dashboard
9. Subject/explore page
10. Quiz interface
11. Quiz result page
12. Attempt history
13. Admin dashboard
14. Subject management
15. Chapter management
16. Quiz management
17. Question management
18. User management
19. Charts/analytics
20. Empty/error/loading states
21. Mobile responsive pass
22. Animation/micro-interaction pass
23. Final visual QA
24. Production deployment

---

# 32. Final Visual Principle

The entire application should follow one core rule:

> **Less UI. More hierarchy. More visual feedback.**

Quiz Master should feel:

**Premium enough for a portfolio.  
Simple enough for students.  
Playful enough to feel like a quiz product.  
Structured enough to feel like a real SaaS application.**
