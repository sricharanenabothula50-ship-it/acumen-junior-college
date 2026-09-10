---
name: Academic Distinction
colors:
  surface: '#faf9fe'
  surface-dim: '#dad9df'
  surface-bright: '#faf9fe'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f8'
  surface-container: '#eeedf2'
  surface-container-high: '#e8e7ed'
  surface-container-highest: '#e3e2e7'
  on-surface: '#1a1b1f'
  on-surface-variant: '#43474f'
  inverse-surface: '#2f3034'
  inverse-on-surface: '#f1f0f5'
  outline: '#747781'
  outline-variant: '#c4c6d1'
  surface-tint: '#3e5e95'
  primary: '#00193c'
  on-primary: '#ffffff'
  primary-container: '#002d62'
  on-primary-container: '#7796d1'
  inverse-primary: '#abc7ff'
  secondary: '#115cb9'
  on-secondary: '#ffffff'
  secondary-container: '#659dfe'
  on-secondary-container: '#003370'
  tertiary: '#330e00'
  on-tertiary: '#ffffff'
  tertiary-container: '#541d02'
  on-tertiary-container: '#d4815d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#abc7ff'
  on-primary-fixed: '#001b3f'
  on-primary-fixed-variant: '#24467c'
  secondary-fixed: '#d7e2ff'
  secondary-fixed-dim: '#acc7ff'
  on-secondary-fixed: '#001a40'
  on-secondary-fixed-variant: '#004491'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb597'
  on-tertiary-fixed: '#360f00'
  on-tertiary-fixed-variant: '#743417'
  background: '#faf9fe'
  on-background: '#1a1b1f'
  surface-variant: '#e3e2e7'
  heritage-navy: '#001B3A'
  achievement-orange: '#F27141'
  intellect-gold: '#F2A900'
  growth-green: '#7DB741'
  surface-neutral: '#F8FAFC'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Montserrat
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.04em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-padding: 80px
---

## Brand & Style

This design system is built for an educational institution that bridges traditional academic excellence with modern pedagogical innovation. The visual narrative centers on **Academic Distinction**, targeting ambitious students and discerning parents who value precision, mentorship, and success.

The aesthetic follows a **Corporate / Modern** style, leaning into a "New Academic" look. It utilizes high-density information layouts balanced by generous whitespace to ensure clarity and focus. The design avoids unnecessary decorative flourishes, opting instead for structural integrity, crisp typography, and subtle depth to convey a sense of institutional permanence and professional growth.

**Key visual principles:**
- **Authority through Precision:** Perfectly aligned grids and consistent spacing.
- **Trust through Clarity:** High contrast and legible type scales.
- **Modern Mentorship:** A clean, vibrant approach to traditional academic color palettes.

## Colors

The palette is anchored by **Heritage Navy** and **Academic Blue**, providing a foundation of stability and professional depth. This primary core is elevated by a suite of functional accent colors derived from the institution's visual identity:

- **Primary (Deep Navy/Blue):** Used for headers, navigation, and primary CTAs to establish authority.
- **Achievement Orange:** Reserved for high-impact calls to action, deadline alerts, and "New" badges.
- **Growth Green:** Utilized for success states, "Results" highlights, and positive performance metrics.
- **Intellect Gold:** Used sparingly for premium designations, "Top Ranker" highlights, and honors.

Neutral tones are cool-leaning grays that maintain the "clean" institutional feel, preventing the interface from feeling muddy or overly sterile.

## Typography

The typography system pairs **Montserrat** for headlines with **Inter** for body text. This combination strikes a balance between the bold, confident geometric structures of Montserrat (representing the institution's strength) and the highly legible, systematic nature of Inter (representing the clarity of instruction).

- **Headlines:** Use Semi-Bold and Bold weights in Heritage Navy to anchor sections.
- **Body:** Use Inter for all long-form content. High-contrast dark grays are preferred over pure black to reduce eye strain during long reading sessions.
- **Labels:** Small caps or medium-weight Inter should be used for metadata like "Faculty Name" or "Subject Code" to differentiate from body narrative.

## Layout & Spacing

The design system utilizes a **12-column fixed grid** for desktop and a **4-column fluid grid** for mobile. 

The spacing logic follows a strict 8px base unit. Section vertical padding is intentionally generous (80px - 120px) to allow the "premium" positioning of the brand to breathe. Faculty cards and result modules should use a "nested grid" approach, maintaining consistent gutters of 24px between items to ensure high readability even in data-dense sections.

**Breakpoints:**
- **Mobile:** 0px - 599px (16px margins)
- **Tablet:** 600px - 1023px (32px margins)
- **Desktop:** 1024px+ (Centred container, 1280px max-width)

## Elevation & Depth

To convey a sense of modern mentorship, depth is handled through **Tonal Layers** and **Ambient Shadows**.

1.  **Level 0 (Base):** The primary background color (White or Surface Neutral).
2.  **Level 1 (Cards/Containers):** Pure white backgrounds with a subtle, ultra-soft shadow (Y: 4px, Blur: 20px, Opacity: 4% Heritage Navy). This is used for Faculty profiles and Course cards.
3.  **Level 2 (Interactive/Floating):** Used for hovering states or dropdown menus. Shadows become more defined (Y: 8px, Blur: 24px, Opacity: 8% Heritage Navy) to indicate reachability.

Avoid harsh black shadows or heavy borders. Instead, use thin, 1px borders in a very light gray (#E2E8F0) to define card boundaries on Level 1.

## Shapes

The design system uses a **Soft (1)** shape language. The subtle rounding (4px - 12px) softens the corporate feel without losing the "authority" that sharp corners provide. 

- **Primary Buttons & Inputs:** 4px radius (Small) to feel precise.
- **Faculty & Result Cards:** 8px radius (Large) to feel approachable.
- **Feature Banners:** 12px radius (Extra Large) for a modern, contained look.

## Components

### Buttons
- **Primary:** Solid Heritage Navy background, white text. No gradient. Focus on crisp 4px corners.
- **Secondary:** Transparent background with a 2px Heritage Navy border.
- **Accent:** Solid Achievement Orange, used only for critical conversion points like "Apply Now."

### Cards
- **Faculty Card:** Image at top (circular or slightly rounded), followed by name in Montserrat Bold. Use a light gray top-border to separate the image from the text content.
- **Result Card:** High-contrast containers using Growth Green for rank highlights. Background should be Level 1 elevation.

### Inputs
- **Text Fields:** 1px border (#CBD5E1) that transitions to 2px Academic Blue on focus. Labels should always be visible above the input using `label-lg`.

### Chips & Badges
- Used for "Course Status" or "Exam Category." Use low-saturation background tints of the named colors (e.g., 10% opacity Orange background with 100% opacity Orange text).

### Lists
- Use custom iconography for bullet points (e.g., a small geometric arrow in Academic Blue) rather than standard browser bullets to reinforce the premium feel.