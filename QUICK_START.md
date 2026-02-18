# 🌿 BioLens Nature Theme - Quick Start Guide

## What's Been Done ✨

Your BioLens application now has **a complete, cohesive nature theme** across:

### 1. **Main Application Window** (BioLens_UI.py)
- Forest green buttons with smooth hover effects
- Warm cream background (#f5f5f0)
- Professional typography and spacing
- Emojis for intuitive navigation (🌿 📁 ⚙️ 🔄)
- Responsive button sizing (45px min height for accessibility)

### 2. **Interactive Dashboard** (Trailcam_Grapher.py)
- Nature-themed CSS styling for all controls
- Forest green dropdown menus with smooth transitions
- Beautiful data visualization with matching colors
- Smooth box-shadow effects on hover
- Cream plot backgrounds for comfortable viewing

### 3. **Documentation & Tools**
- **NATURE_THEME.md** - Complete visual design guide
- **COLOR_PALETTE.html** - Interactive color preview
- **THEME_IMPLEMENTATION.md** - Detailed implementation summary
- **theme_colors.py** - Programmatic color definitions
- **generate_color_palette.py** - Regenerate color previews

## 🎨 Color Palette Overview

```
┌──────────────────┬──────────┬────────────────────────────┐
│ Color Name       │ Hex Code │ Example Usage              │
├──────────────────┼──────────┼────────────────────────────┤
│ Primary Green    │ #4a7c59  │ Buttons, borders, bars     │
│ Dark Forest      │ #2d5a3d  │ Headings, titles           │
│ Dark Sage        │ #2d3d2d  │ Primary text               │
│ Light Background │ #f5f5f0  │ Main page/window bg        │
│ Cream White      │ #ffffff  │ Cards, input fields        │
│ Soft Green       │ #e8f0e8  │ Hover effects, accents     │
│ Forest Dark      │ #3a6a49  │ Button hover state         │
│ Deep Forest      │ #2a5a39  │ Button pressed state       │
│ Light Grid       │ #e8e8e0  │ Chart grid lines           │
└──────────────────┴──────────┴────────────────────────────┘
```

## 🚀 Running the Application

### Step 1: Install Dependencies
```bash
pip install pandas plotly dash PySide6 pywebview
```

### Step 2: Launch the Application
```bash
python BioLens_UI.py
```

### Step 3: Process Your Data
1. Click **📁 Select File** and choose a Wildlife Insights CSV
2. Click **⚙️ Process and Open Dashboard**
3. The dashboard opens with your data visualized in the nature theme

## 👀 Preview the Colors

To see the color palette in your browser:

```bash
# Generate the color palette HTML (if needed)
python generate_color_palette.py

# Open in your browser (Windows)
start COLOR_PALETTE.html
```

## 📁 New Files Created

```
✨ NEW FILES:
├── NATURE_THEME.md                 - Design documentation
├── THEME_IMPLEMENTATION.md         - Implementation details
├── COLOR_PALETTE.html              - Interactive color preview
├── generate_color_palette.py       - Palette generator script
├── theme_colors.py                 - Color definitions (for Python)
└── QUICK_START.md                  - This file!

✏️ ENHANCED FILES:
├── BioLens_UI.py                   - Nature-themed launcher UI
├── Trailcam_Grapher.py             - Nature-themed dashboard
└── README.md                        - Updated documentation
```

## 🎯 Key Features

✅ **Coherent Design**: Single forest-green color palette throughout
✅ **Beautiful Interactions**: Smooth 0.3s transitions on all elements
✅ **Accessible**: WCAG AA compliant color contrasts
✅ **Professional**: Polished, modern appearance
✅ **Wildlife Themed**: Nature emojis and earth-tone colors
✅ **Well Documented**: Multiple guides and references
✅ **Easy to Customize**: Color definitions in centralized locations

## 🔧 Customizing the Theme

### Change Primary Color (Green → Your Color)

1. Replace `#4a7c59` in **three files**:

   **BioLens_UI.py** (search for):
   ```python
   QColor("#4a7c59")
   ```

   **Trailcam_Grapher.py** (search for):
   ```python
   "#4a7c59"  # appears multiple times in CSS and update_graph()
   ```

   **theme_colors.py** (search for):
   ```python
   "primary_green": "#4a7c59"
   ```

2. Regenerate the color palette preview:
   ```bash
   python generate_color_palette.py
   ```

3. Restart the application for changes to take effect

## 📖 Documentation References

### For Users
- **README.md** - Getting started, features, troubleshooting
- **QUICK_START.md** - This file

### For Designers
- **COLOR_PALETTE.html** - Visual color preview
- **NATURE_THEME.md** - Complete design system documentation
- **THEME_IMPLEMENTATION.md** - What was implemented and how

### For Developers
- **theme_colors.py** - Programmatic color definitions and usage examples
- **BioLens_UI.py** - PySide6 implementation reference
- **Trailcam_Grapher.py** - Dash/Plotly implementation reference

## 💡 Tips & Tricks

### 1. Inspect UI Colors
Open the app → Right-click → Inspect (in browser)
Look for `background-color`, `color`, `border-color` in Styles tab

### 2. Export Graphs as Images
In the dashboard, hover over any graph → Click camera icon to download PNG

### 3. Use Color Variables in New Components
Import from `theme_colors.py`:
```python
from theme_colors import COLORS, COMPONENT_COLORS

button_color = COLORS["primary_green"]  # #4a7c59
```

### 4. Extend the Theme
Add new components following the existing patterns:
- Use `COLORS["primary_green"]` for main accent
- Use `COLORS["soft_green"]` for hover states
- Use `COLORS["dark_sage"]` for text
- Maintain 0.3s transitions for consistency

## 🎨 Visual Examples

### Button States
```
┌─ NORMAL ────────────────┐
│ 🟢 Forest Green Button   │  Color: #4a7c59
│                          │  Cursor: pointer
└──────────────────────────┘

┌─ HOVER ─────────────────┐
│ 🟢 Forest Green Button   │  Color: #3a6a49 (darker)
│                          │  Shadow: elevated
└──────────────────────────┘

┌─ PRESSED ───────────────┐
│ 🟢 Forest Green Button   │  Color: #2a5a39 (even darker)
│                          │  Shadow: very elevated
└──────────────────────────┘
```

### Color Gradients
```
Window Background (main):    #f5f5f0 (warm cream)
Dashboard Background:        Linear gradient from #f5f5f0 to #f0f5f0
Chart Background:            #f5f5f0 with white cards (#ffffff)
```

## ❓ FAQ

**Q: Can I use a different plant emoji?**
A: Yes! Edit the window title and labels in BioLens_UI.py:
```python
self.setWindowTitle("🌲 BioLens Trail Cam Processor")  # or 🍃 🌱 🌾 etc.
```

**Q: How do I make it darker/lighter?**
A: Edit `COLORS` in theme_colors.py or adjust hex values directly.
- Make darker: Lower hex values (e.g., #4a7c59 → #3a6a49)
- Make lighter: Raise hex values (e.g., #4a7c59 → #5a8c69)

**Q: Can I add more colors?**
A: Yes! Add to the `COLORS` dict in theme_colors.py and update references in BioLens_UI.py and Trailcam_Grapher.py.

**Q: What if colors don't show up?**
A: 
1. Clear browser cache (Ctrl+Shift+Del)
2. Restart the application
3. Check that PySide6 QPalette was applied before showing window

## 📞 Support

For theme-related issues:
1. Check **NATURE_THEME.md** for design specifications
2. Review **THEME_IMPLEMENTATION.md** for implementation details
3. Check **theme_colors.py** for color definitions
4. Open **COLOR_PALETTE.html** to verify colors visually

---

**🌿 Welcome to the Green! Your BioLens app now has a beautiful nature theme.**

Version: 1.0 (February 18, 2026)
Status: ✅ Complete and ready to use!
