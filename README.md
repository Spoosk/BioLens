# 🌿 BioLens Trail Cam Processor

BioLens is an analytical tool for processing and visualizing wildlife camera trap data from **Wildlife Insights**. It provides an intuitive interface for data cleaning, exploratory analysis, and interactive visualization.

## Features

- **CSV Data Processing**: Automatically cleans and validates Wildlife Insights exports (note: metadata inaccuracies will be overwritten with upload date)
- **Interactive Dashboard**: Explore data by time periods, species, taxonomy, and more
- **Real-time Filtering**: Filter data by Class, Order, Family, Genus, or Species
- **Time-series Analysis**: View observations grouped by day, month, or year

## Quick Start

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

## Usage

### Launcher Window
- **Select File**: Browse and choose a `.csv` file from Wildlife Insights
- **Process**: Cleans the data and launches the interactive dashboard
- **Status**: Real-time feedback on processing status

### Dashboard
- **Group by Time**: Switch between day, month, or year-level aggregation (day-to-day acccuracy is limited by camera metadata accuracy)
- **Filter Controls**: 
  - Class: Mammalia, Aves, Reptilia, etc.
  - Order, Family, Genus, Species: more specific taxonomy
- **Interactive Graph**: Hover for details, zoom, pan, and download as PNG

## 📁 Project Structure

```
BioLens/
├── BioLens_UI.py              # Main launcher
├── Trailcam_Grapher.py        # Interactive Dash dashboard
├── CSVDateCleaner.py          # Data cleaning utilities
├── Sample_Data.csv            # Example dataset
├── NATURE_THEME.md            # Theme documentation & color palette
└── README.md                  # This file
```

## Customization

To customize colors, edit the hex codes in:
- **UI Window**: `BioLens_UI.py` (search for `#4a7c59`)
- **Dashboard**: `Trailcam_Grapher.py` (search for `NATURE_CSS` and `#4a7c59`)

See [NATURE_THEME.md](NATURE_THEME.md) for the complete color palette.

## Troubleshooting

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

## Wildlife Insights

Learn more about Wildlife Insights at: https://www.wildlifeinsights.org/

## 🤝 Contributing

Contributions welcome! For feature requests or bug reports, please open an issue.

---

**Made for wildlife researchers and conservation professionals, as well as casual observers!**
