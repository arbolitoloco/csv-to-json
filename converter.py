import os, csv, json

def simple_convert(csv_file, json_file, root_name):
    """ Converts a given CSV file into JSON structured file.

    Files have to be in the root directory. Output will also go to the root directory. JSON is generated as-is, no nesting is provided.

    Parameters
    -----------
    csv_file : str
        Filename of csv to be converted (without extension).
    json_file : str
        Desired name for generated JSON file (without extension).
    root_name : str
        Desired name for root element grouping all entries.
        
    """
    # Read the CSV and add data to a dictionary
    csv_file = csv_file+".csv"
    with open(csv_file) as csv_file:
      csv_reader = csv.DictReader(csv_file)

      # Add data to a root node
      root = {}
      root[root_name] = [row for row in csv_reader]
      
      # # Write data to JSON file
      json_file = json_file+".json"
      with open(json_file, "w") as json_file:
        json_file.write(json.dumps(root, indent=4))
      print("Converted file")

# """ Usage example (function call):
simple_convert("example-spreadsheet", "example", "objects")