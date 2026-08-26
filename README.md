# Unified Military Analytics

An end-to-end data analytics project integrating military, economic, demographic, and geopolitical data to analyze and compare 145 countries.

## Project Overview

Unified Military Analytics brings together multiple datasets to create a unified country-level view of military capability and economic strength.

The project focuses on:

- Military power and rankings
- Defense budgets and defense spending
- Active and reserve military personnel
- GDP and GDP per capita
- Population and demographic indicators
- NATO-related indicators
- Comparison of military capability and economic position

## Objectives

- Integrate multiple military, economic, demographic, and country-level datasets
- Clean and standardize country-level data
- Create a unified analytical dataset covering 145 countries
- Engineer meaningful KPIs for military and economic comparison
- Compare military capability with economic indicators
- Develop interactive Tableau dashboards for country-level exploration and comparison

## Project Workflow

Multiple Data Sources  
↓  
Data Cleaning & Standardization  
↓  
Data Integration  
↓  
KPI Engineering  
↓  
Unified Analytical Dataset  
↓  
Analysis & Visualization  
↓  
Interactive Tableau Dashboard

## Repository Structure

```text
Unified-Military-Analytics/
│
├── README.md
│
├── Data/
│   ├── military_cleaned.csv
│   ├── military_master.csv
│   ├── military_final.csv
│   └── military_final.xlsx
│
├── Python/
│   ├── merge_data.py
│   ├── kpi_engineering.py
│   └── generate_kpis.py
│
├── Tableau/
│   └── Unified_Military_Analytics.twbx
│
├── Storyboard/
│   └── Storyboard.pdf
│
└── Screenshots/
    ├── Nation Overview.png
    └── Compare Power.png
```
## Data

The project integrates multiple datasets containing military, economic, demographic, geographic, and country-level information.

### military_cleaned.csv

Cleaned and standardized military dataset.

### military_master.csv

Integrated master dataset created by combining the required datasets.

### military_final.csv

Final analytical dataset prepared for KPI analysis and visualization.

### military_final.xlsx

Excel version of the final analytical dataset.

## Python Data Processing

Python was used for data cleaning, integration, transformation, and KPI engineering.

### merge_data.py

Used to integrate the required datasets and create the master dataset.

### kpi_engineering.py

Used to create derived analytical features and KPIs for military and economic analysis.

### generate_kpis.py

Used to generate the final KPI-enhanced dataset for analysis and visualization.

## Key KPIs

The project includes indicators such as:

- Global Military Power Rank
- Power Index Score
- GDP
- GDP Rank
- GDP per Capita
- Defense Budget
- Defense Budget as a Percentage of GDP
- Active Military Personnel
- Reserve Personnel
- Total Military Personnel
- Population
- NATO Contribution Rank
- Interoperability Score
- Training Exercises per Year
- Power Index Rank Gap

### Power Index Rank Gap

The Power Index Rank Gap compares a country's military ranking with its economic ranking.

Power Index Rank Gap = Global Firepower Rank − GDP Rank

This KPI provides an additional perspective for comparing military capability with economic position.

## Tableau Dashboard

The project includes an interactive Tableau dashboard designed to analyze military and economic indicators across 145 countries.

### Nation Overview

Provides a detailed country-level profile using key military, economic, demographic, and geopolitical indicators.

### Compare Power

Enables comparative analysis between countries using military power, defense spending, personnel, economic indicators, and other key metrics.

Interactive filters allow users to explore and compare countries based on different indicators.

### Tableau Workbook

The complete Tableau workbook is available in:

Tableau/Unified_Military_Analytics.twbx

## Dashboard Preview

### Nation Overview

![Nation Overview](Screenshots/Nation%20Overview.png)

### Compare Power

![Compare Power](Screenshots/Compare%20Power.png)

### Coalition Builder

![Coalition Builder](Screenshots/Coalition%20Builder.png)

### Quick Stats

![Quick Stats](Screenshots/Quick%20Stats.png)

## Storyboard

The project includes a dashboard storyboard defining the planned dashboard layouts, visual structure, and user experience.

The storyboard is available in:

Storyboard/Storyboard.pdf

## Technologies Used

- Python
- Pandas
- NumPy
- Tableau
- Microsoft Excel
- Git
- GitHub

## Skills Demonstrated

- Data Cleaning
- Data Integration
- Data Transformation
- KPI Engineering
- Exploratory Data Analysis
- Comparative Analysis
- Data Visualization
- Tableau Dashboard Development
- Analytical Storytelling
- Git & GitHub

## Project Scope

| Attribute | Details |
|---|---|
| Countries Analyzed | 145 |
| Project Type | Data Analytics & Visualization |
| Programming | Python |
| Visualization | Tableau |
| Data Formats | CSV, Excel |
| Version Control | Git & GitHub |

## My Contribution

This was developed as a collaborative analytics project. My contributions focused on the data preparation, KPI engineering, and visualization workflow.

- Data cleaning and preparation
- Dataset integration
- KPI engineering
- Creation of the unified analytical dataset
- Tableau dashboard development
- Dashboard filters and interactive analysis
- Data visualization
- Analytical storytelling

## Future Improvements

- Add historical military and economic data for trend analysis
- Automate data updates
- Add predictive analytics
- Develop advanced statistical analysis
- Expand the dashboard with additional analytical views
- Deploy the dashboard for wider accessibility

## Data Sources

The project uses publicly available datasets related to military, economic, demographic, geographic, and country-level information.

Appropriate attribution should be maintained for the original sources of the datasets used in the project.
