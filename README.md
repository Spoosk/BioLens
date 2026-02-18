# 🌿 BioLens Trail Cam Processor

BioLens is a modern, nature-themed software for processing and visualizing wildlife camera trap data from **Wildlife Insights**. It provides an intuitive interface for data cleaning, exploratory analysis, and interactive visualization.

## ✨ Features

- **Clean UI with Nature Theme**: Forest green and earth-tone color palette throughout
- **CSV Data Processing**: Automatically cleans and validates Wildlife Insights exports
- **Interactive Dashboard**: Explore data by time periods, species, taxonomy, and more
- **Responsive Design**: Beautiful, modern interface that works on all devices
- **Real-time Filtering**: Filter data by Class, Order, Family, Genus, or Species
- **Time-series Analysis**: View observations grouped by day, month, or year

## 🎨 Design

The entire application features a cohesive **nature theme** with:
- Forest green accents (#4a7c59)
- Warm cream backgrounds (#f5f5f0)
- Smooth transitions and hover effects
- Accessible color contrasts (WCAG AA compliant)
- Wildlife-themed emoji for intuitive navigation

For detailed theme documentation, see [NATURE_THEME.md](NATURE_THEME.md).

## 🚀 Quick Start

### Requirements
- Python 3.7+
- pandas
- plotly
- dash
- PySide6
- pywebview

### Installation

```bash
pip install pandas plotly dash PySide6 pywebview
```

### Running BioLens

```bash
python BioLens_UI.py
```

1. A launcher window will appear
2. Click **📁 Select File** to choose your Wildlife Insights CSV export
3. Click **⚙️ Process and Open Dashboard** to clean and visualize the data
4. The dashboard will open in a new window with interactive charts

## 📊 Usage

### Launcher Window
- **Select File**: Browse and choose a `.csv` file from Wildlife Insights
- **Process**: Cleans the data and launches the interactive dashboard
- **Status**: Real-time feedback on processing status

### Dashboard
- **Group by Time**: Switch between day, month, or year-level aggregation
- **Filter Controls**: 
  - Class: Mammalia, Aves, Reptilia, etc.
  - Order, Family, Genus, Species: Drill down into taxonomy
- **Interactive Graph**: Hover for details, zoom, pan, and download as PNG

## 📁 Project Structure

```
BioLens/
├── BioLens_UI.py              # Main launcher with nature-themed interface
├── Trailcam_Grapher.py        # Interactive Dash dashboard
├── CSVDateCleaner.py          # Data cleaning utilities
├── Sample_Data.csv            # Example dataset
├── NATURE_THEME.md            # Theme documentation & color palette
└── README.md                  # This file
```

## 🔧 Customization

To customize colors, edit the hex codes in:
- **UI Window**: `BioLens_UI.py` (search for `#4a7c59`)
- **Dashboard**: `Trailcam_Grapher.py` (search for `NATURE_CSS` and `#4a7c59`)

See [NATURE_THEME.md](NATURE_THEME.md) for the complete color palette.

## 🐛 Troubleshooting

**"No module named PySide6"**
```bash
pip install PySide6
```

**Dashboard won't open**
- Ensure port 8050 is available
- Check that all dependencies are installed

**Data cleaning errors**
- Verify the CSV is from Wildlife Insights export
- Check for unusual characters or encoding issues

## 📝 Data Format

BioLens expects CSV files from Wildlife Insights with columns including:
- `timestamp`: When the image was captured
- `species`: The detected species
- `class`, `order`, `family`, `genus`: Taxonomic classification
- `common_name`: Human-readable species name
- And others (location, behavior, etc.)

## 🌍 Wildlife Insights

Learn more about Wildlife Insights at: https://www.wildlifeinsights.org/

## 📄 License

[Add your license info here]

## 🤝 Contributing

Contributions welcome! For feature requests or bug reports, please open an issue.

---

**Made for wildlife researchers and conservation professionals** 🦌🦙🐆
