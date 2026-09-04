# Excel Messy Data Cleaning Automation

## Project Overview     

This project automates the cleaning process using Python and Pandas, reducing repetitive manual Excel work and producing a clean dataset ready for reporting and analysis.

##  Workflow
```
Messy Excel Files
        ↓
Read Multiple Excel Files
        ↓
Combine Data
        ↓
Remove Duplicates
        ↓
Remove Empty Rows
        ↓
Standardize Columns & Text
        ↓
Handle Missing / Invalid Values
        ↓
Clean Quantity & Unit Price
        ↓
Clean Order Dates
        ↓
Validate Data
        ↓
Cleaned Excel File
        ↓
Archive Processed Files
```

## Technologies Used
- Python
- Pandas
- OS
- Glob
- Shutil
- OpenPyXL


## Key Features
- Reads multiple .xlsx files automatically
- Combines data from multiple source files
- Removes duplicate records
- Removes completely empty rows
- Standardizes column names
- Standardizes text formatting
- Handles missing Customer IDs,  names, cities
- Validates Customer Names and City values  
- Extracts numeric values from messy Quantity data
- Converts Quantity and Unit Price into numeric data types
- Fills missing Quantity using category-level median
- Fills missing Unit Price using category-level median
- Converts Order Date into a proper datetime format
- Removes records with invalid Order Dates
- Fills missing Order Status using the mode
- Saves the cleaned dataset as an Excel file
- Archives processed source files automatically


## Project Structure
```
Excel-Messy-Data-Cleaning/
│
├── Data/
│   ├── Source/
│   │   └── *.xlsx
│   │
│   └── Archive/
│
├── Output/
│   └── cleaned_data.xlsx
│
│──── ScreenShots/
│          │── cleaned_data.png
│          └── raw_messy_data.png   
│
├── Excel_files_cleaner.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## How to Run

1. Clone the Repository
git clone https://github.com/AkshaywithData/Excel-Messy-Data-Cleaner

2. Install Dependencies
pip install -r requirements.txt

3. Add Source Files
Place your Excel files inside:
Data/Source/

4. Run the Script
Excel_files_cleaner.py

5. Check the Output

The cleaned Excel file will be created in:

Output/cleaned_data.xlsx

Processed source files will be moved to:

Data/Archive/

## Future Improvements

Possible future improvements include:

- Logging system
- Automated email delivery
- MySQL database integration
- Automated reporting and dashboards

##  License

This project is licensed under the MIT License.

See the LICENSE file for details.

## Author

**Akshay Gawand**


