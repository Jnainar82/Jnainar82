# Seasonal Demand Prediction

## Overview
This project analyzes seasonal demand fluctuations in order data, applying a seasonal factor to account for holidays and seasonal variations. The dataset is generated with random order quantities, and feature engineering is performed to prepare data for predictive modeling.

## Features
- **Seasonal Factor Calculation**: Adjusts demand based on holidays and seasonal trends.
- **Feature Engineering**:
  - Extracts month and day of the week.
  - Includes past order quantities for trend analysis.
  - Shifts data to estimate future demand.
- **Data Export**: Saves processed data to an Excel file for further analysis.

## Installation
### Prerequisites
Ensure you have Python 3.12 installed along with the required libraries:
```bash
pip install pandas numpy openpyxl
```

## Usage
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```
2. Run the script:
   ```bash
   python seasonal_demand.py
   ```
3. The output file `seasonal_demand_predictions.xlsx` will be created in the working directory.

## Code Explanation
- **`get_easter_date(year)`**: Calculates Easter Sunday for a given year.
- **`is_holiday_season(date)`**: Determines if a given date is near a major holiday.
- **`seasonal_factor(date)`**: Assigns a seasonal adjustment factor based on holidays and seasonal trends.
- **Data Processing**:
  - Generates order data.
  - Applies seasonal factors.
  - Creates new features for machine learning models.
  - Exports the final dataset.

## File Structure
```
├── seasonal_demand.py  # Main script
├── seasonal_demand_predictions.xlsx  # Output file
└── README.md  # Project documentation
```

## Future Enhancements
- Implement machine learning models for demand forecasting.
- Use real-world datasets instead of random generation.
- Add visualization of demand trends.

## License
This project is licensed under the MIT License.


