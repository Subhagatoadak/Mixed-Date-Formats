# MixedDateFormats
## Overview
MixedDateFormats is a Python module designed to convert and standardize date formats in a Pandas DataFrame. It allows users to transform date columns into a new format while saving the modified dataset as a CSV file.

Key Features
✅ Handles mixed date formats in datasets
✅ Easily converts date formats using a simple method
✅ Supports customizable column names for transformed dates
✅ Exports the updated dataset to a new CSV file

## Installation
1. Install Dependencies
Ensure you have Python installed along with the required packages:

```sh
pip install pandas
```
## Usage
1. Import the Module and Create an Instance
```python
from mixed_date_formats import MixedDateFormats  
```
## Load dataset
```python
t5 = MixedDateFormats("C:/something/a***/Desktop/SLO_Data.csv")  
```

2. Convert Date Format in a Specific Column
```python
t5.dateformatchange("DATE", old_date_format='%m/%d/%Y', new_date_format='%Y-%m-%d', new_var_name="Date1", final_filename="gfinal.csv")  
```
Parameters:
"DATE" → Column name containing the date values
old_date_format='%m/%d/%Y' → Original date format
new_date_format='%Y-%m-%d' → Desired output format
new_var_name="Date1" → New column name for the formatted date
final_filename="gfinal.csv" → Output filename

Customization
Modify date column names as per your dataset
Adjust date format strings (compatible with Python’s strftime formats)
Contributing
Pull requests are welcome! To contribute:

Fork the repository
Create a new feature branch
Commit and push your changes
Submit a pull request
License
This project is licensed under MIT License. See LICENSE for details.
