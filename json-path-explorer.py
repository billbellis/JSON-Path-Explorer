#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
json-path-explorer-en.py

Description:
  This program reads a JSON file (data.json) and displays its structure visually — no matter how complex (with nested lists and dictionaries) — using a recursive function.
  It also generates, for each value, the Python syntax path required to access it.

Input:
  The 'data.json' file must be located in the same folder as the script and contain valid JSON data.

Output:
  Displays the JSON structure in the terminal with proper indentation, data type indicators, and the access path for each value.

Author: Vassilis Bellis
Date: 23/06/2025

Requirements:
  Python 3.x
"""

import json


def analyze_content(data, path_str="data", level=0, output=None):
    """
    Recursively analyzes the structure of a JSON object and generates a report with indentation.
    It also generates, for each value, the Python path to access it.

    Args:
        data: The JSON data (dict, list, or simple value)
        path_str: The access path for each value
        level: The indentation depth level
        output: List to append the analysis result (optional)

    Returns:
        output (list): List of lines describing the data structure and access paths
    """
    output = output or []
    indent = "  " * level

    if isinstance(data, dict):
        output.append(f"{indent}Dictionary:")
        for key, value in data.items():
            output.append(f"{indent}  Key: '{key}'")
            new_path = f"{path_str}['{key}']"
            analyze_content(value, new_path, level + 1, output)

    elif isinstance(data, list):
        output.append(f"{indent}List:")
        for index, item in enumerate(data):
            output.append(f"{indent}  Item #{index + 1}:")
            new_path = f"{path_str}[{index}]"
            analyze_content(item, new_path, level + 1, output)

    else:
        output.append(f"{indent}Simple value: {repr(data)}")
        output.append(f"{indent}path: {path_str}")
    return output


def main():
    """
    Main function that reads the file and calls analyze_content.
    """
    try:
        with open("data.json", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: The file 'data.json' was not found.")
        return
    except json.JSONDecodeError as e:
        print(f"Error: The file does not contain valid JSON data. ({e})")
        return

    result = analyze_content(data)

    # Display result in terminal
    for line in result:
        print(line)

    # Option to save to file
    save_choice = input("\nDo you want to save the result to a file? (Y/N): ").strip().lower()
    if save_choice == "y":
        with open("structure_output.txt", "w", encoding="utf-8") as out_file:
            out_file.write("\n".join(result))
        print("The structure was saved to 'structure_output.txt'.")


if __name__ == "__main__":
    main()