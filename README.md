# JSON to Excel Converter

A beginner-friendly Python tool to convert JSON files into Excel spreadsheets.  
Supports both **flat JSON lists** and **nested JSON objects with lists** (e.g. user + orders).

---

## Features
- Reads JSON files (UTF-8 safe).
- Flattens nested structures into rows/columns using `pandas.json_normalize`.
- Handles errors gracefully (missing file or invalid JSON).
- Outputs clean `.xlsx` files ready to open in Excel.

---

## Requirements
Install dependencies with:

```bash
pip install -r requirements.txt
```
---

## **Usage**

Run the script directly:

```bash
python main.py
```

This will:

- Convert sample1.json → output.xlsx
- Convert sample_nested.json → orders.xlsx


You can also call the function in your own code:
```python
from main import json_to_excel

json_to_excel("mydata.json", "result.xlsx")
```

---

## **Examples**

**Input**: sample1.json

```json
[
  {"name": "Arun", "age": 27, "country": "India"},
  {"name": "John", "age": 30, "country": "Canada"},
  {"name": "Sara", "age": 25, "country": "Sweden"}
]
```

**Output Excel:**

name	age	country

Arun	27	India
John	30	Canada
Sara	25	Sweden



---

**Input**: sample_nested.json

```json
{
  "user": {"id": 101, "name": "Arun"},
  "orders": [
    {"order_id": "A-1", "item": "Book", "price": 12.5},
    {"order_id": "A-2", "item": "Pen",  "price": 3.0}
  ]
}
```

**Output Excel:**

**order_id**	**item**    **price**	**user.id** **user.name**

A-1	              Book	      12.5	        101	        Arun
A-2	              Pen	      3.0	        101	        Arun



---

## **Notes**

- Designed as a simple proof-of-work tool for data conversion gigs.
- For more complex nested JSON, adjust record_path and meta inside json_to_excel.
- Excel outputs (.xlsx) are ignored in version control (.gitignore).



---

## **License**

MIT

---