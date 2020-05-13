# csv-to-json

Python function to convert csv files into json format.
Tested with Python 3.

## Dependencies

os, csv, json

## Usage

Basic call:

    simple_convert(csv_file, json_file, root_name)

Converts a given CSV file into JSON structured file.
Files have to be in the root directory. Output will also go to the root directory. JSON is generated as-is, no nesting is provided.

### Parameters

- csv_file : str

  Filename of csv to be converted (without extension).

- json_file : str

  Desired name for generated JSON file (without extension).

- root_name : str

  Desired name for root element grouping all entries.

### Usage example (function call):

    simple_convert("example-spreadsheet", "example", "objects")

Input ([example-spreadsheet.csv](example-spreadsheet.csv)) and output ([example.json](example.json)) available.
