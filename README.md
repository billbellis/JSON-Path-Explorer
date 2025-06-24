for Greek see README-gr.md
# JSON-Path-Explorer

## Description
**JSON-Path-Explorer** is a recursive tool for analyzing JSON files, written in Python.  
It visually displays the structure of a JSON file — no matter how complex — and generates the Python syntax path for directly accessing each value.

---

## Features
- Analysis of JSON files with nested dictionaries and lists.
- Display of the structure with recursive indentation.
- Presentation of the access path for each value in Python syntax.
- Option to save the result to a file.

---

## Requirements
- Python 3.x

---

## Usage Instructions
- Place the `data.json` file in the same folder as the script.  
- Run the program:
  ```bash
  python working_with_JSON_v4.py
  ```
- The result will appear in the terminal, and you can optionally save it to a file.

### Example  
For the JSON:
```json
{
  "name": "Example",
  "details": {
    "age": 30,
    "hobbies": ["reading", "cycling"]
  }
}
```

The program will display:
```
Dictionary:
  Key: 'name'
    Simple value: 'Example'
    path: data['name']
  Key: 'details'
    Dictionary:
      Key: 'age'
        Simple value: 30
        path: data['details']['age']
      Key: 'hobbies'
        List:
          Item #1:
            Simple value: 'reading'
            path: data['details']['hobbies'][0]
          Item #2:
            Simple value: 'cycling'
            path: data['details']['hobbies'][1]
```

---

## License
Distributed under the MIT License.

---

## Ideas for Extensions
- Add a search function for keys or values within the structure.
- Support for JSON path syntax (e.g., `$.details.hobbies[0]`).
- Graphical user interface (e.g., using `tkinter` or `PyQt`).
- Option to select the JSON file via command-line argument.
- Display of statistics (e.g., total number of keys, maximum depth, etc.)

---

## Contact
For suggestions or improvements: **vassilisbellis56@gmail.com**
