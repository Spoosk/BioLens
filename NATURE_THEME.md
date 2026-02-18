# BioLens Nature Theme 🌿

## Overview
The BioLens Trail Cam Processor now features a cohesive nature-inspired design across both the UI launcher and the interactive dashboard.

## Color Palette

| Element | Hex Code | RGB | Usage |
|---------|----------|-----|-------|
| **Primary Green** | `#4a7c59` | 74, 124, 89 | Buttons, accents, borders |
| **Dark Forest** | `#2d5a3d` | 45, 90, 61 | Headings, text emphasis |
| **Soft Sage** | `#2d3d2d` | 45, 61, 45 | Primary text |
| **Light Background** | `#f5f5f0` | 245, 245, 240 | Main background |
| **Cream White** | `#ffffff` | 255, 255, 255 | Card backgrounds |
| **Soft Green** | `#e8f0e8` | 232, 240, 232 | Hover states, light accents |
| **Forest Dark** | `#3a6a49` | 58, 106, 73 | Hover effects |
| **Deep Forest** | `#2a5a39` | 42, 90, 57 | Pressed states |

## UI Components

### 1. **Main Application Window** (`BioLens_UI.py`)
- **Title**: 🌿 BioLens Trail Cam Processor
- **Background**: Warm cream (#f5f5f0)
- **Window Size**: 500x350px with proper spacing
- **Typography**: 
  - Main title: 16pt bold
  - Descriptions: 10-11pt sans-serif
- **Buttons**:
  - **Primary Button** (Process): Forest green (#4a7c59) with smooth hover effects
  - **Secondary Button** (Select File): Light border with green text
  - Min height: 45px for accessibility
  - Smooth transitions and hover effects

### 2. **Dashboard** (`Trailcam_Grapher.py`)

#### Layout
- Gradient background (cream to light sage)
- Max width: 1400px for optimal viewing
- Responsive 20px padding

#### Controls
- Dropdown menus with green borders
- Focus states with glow effects
- Smooth transitions on hover
- Nature-themed option highlighting

#### Graphs
- **Title**: 🌍 Dynamic titles with emoji
- **Plot Background**: Cream (#f5f5f0)
- **Paper Background**: White with rounded corners (12px border-radius)
- **Bar Colors**: Forest green (#4a7c59) with dark forest outline
- **Grid**: Subtle light beige (#e8e8e0)
- **Hover**: Unified hover mode with formatted tooltips
- **Animation**: Box shadow grows on hover for depth

## Features

✨ **Interactive Elements**
- Smooth transitions (0.3s) on all interactive components
- Focus states with glowing effects
- Hover states with color shifts
- Box shadow elevation for depth perception

🎨 **Visual Consistency**
- Single primary color palette used throughout
- Gradient backgrounds add natural depth
- Rounded corners (6-12px) for softness
- Text shadows on headings for readability

📊 **Data Visualization**
- Forest green bars with dark forest outlines
- Light grid lines that don't overwhelm data
- Cream plot background reduces eye strain
- Custom hover templates with clean formatting

🌍 **Emoji Integration**
- 🌿 Forest/nature references
- 🌍 Global/wildlife references
- 📁 File operations
- ⚙️ Processing operations
- 🔄 Loading states

## Accessibility

- **Color Contrast**: All text meets WCAG AA standards
- **Font Sizes**: Minimum 10pt, with 11-16pt for headings
- **Button Sizing**: Minimum 45px height for easy clicking
- **Focus States**: Clear visual indicators for keyboard navigation
- **Grid Lines**: Subtle but visible for readability

## Usage

### Running the Application
```bash
python BioLens_UI.py
```

1. Select a CSV file from WildlifeInsights
2. Click "Process and Open Dashboard"
3. View your wildlife camera data in the nature-themed dashboard

### Customizing Colors
Edit these color definitions in the respective files:
- `BioLens_UI.py`: Lines with `QColor()` definitions
- `Trailcam_Grapher.py`: Color hex codes in `NATURE_CSS` and `update_graph()`

## Browser Compatibility
- Modern browsers (Chrome, Firefox, Edge, Safari)
- The dashboard runs on Dash/Plotly with pywebview for rendering
- Responsive design adapts to different screen sizes

## Future Enhancements
- Dark mode variant with inverted palette
- Additional data visualization charts (scatter, pie, line graphs)
- Customizable color scheme selector
- Export visualizations as high-quality images
- Sidebar navigation for multiple views
