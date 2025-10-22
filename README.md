# Video Games Market Analysis

An end-to-end data analysis project exploring trends and patterns in the global video games market (1980-2019).

## 🎯 Insights Discovered

- **Sales Peak**: Video game sales reached their peak around 2008-2010
- **Genre Dominance**: Action and Sports genres lead global sales
- **Regional Preferences**: Japan shows distinct genre preferences compared to other regions
- **Critic-User Correlation**: Moderate correlation between critic scores and user ratings

## 🛠️ Project Structure
```videogames_analysis/
├── data/
│   └── games.csv
├── notebooks/
│   ├── 01_exploratory_analysis_original.ipynb
│   └── 02_analysis_with_modules.ipynb
├── src/
│   ├── data_cleaning.py
│   └── visualization.py
└── README.md
```
## 🚀 Quick Start

1. **Clone and setup**:
   ```bash
   git clone https://github.com/Scarleth6o6/videogames_analysis
   cd videogames_analysis

2. **Run analysis**:

    ```python
    # In your notebook
    from src.data_cleaning import load_and_clean_data
    from src.visualization import plot_essentials

    df = load_and_clean_data('data/raw/video_games.csv')
    fig = plot_essentials(df)

## 💡 Technical Highlights
- **Modular Design**: Separated data processing from analysis

- **Data Quality**: Handled missing values, duplicates, and data type conversions

- **Visual Storytelling**: Clear, labeled visualizations that communicate insights effectively

## 📊 Key Features
- Sales trend analysis across decades

- Regional market comparisons

- Genre performance analysis

- Critic vs user score evaluation

## 🌐 Language Note
The initial exploratory analysis in `01_exploratory_analysis_original.ipynb` is documented in Spanish, showcasing the complete data exploration process. The code and subsequent analysis are language-agnostic.