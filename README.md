# 🕒 UNIX Timestamp Converter (JSON Edition)

This Python script converts UNIX timestamps in the `Created_date` field of a JSON dataset into human-readable date format (`YYYY-MM-DD HH:MM:SS`). The output is saved as a new JSON file, preserving all other fields and structure.

---

## 📂 Input Format

The input file should be a JSON array of objects (like tickets or messages), each containing a `Created_date` field.

### Example: `raw_tickets.json`

```json
[
  {
    "Created_date": 1753423234,
    "Customer_Email": "johndoe@gmail.com"
  },
]

 Sample  Output: 
 
[
  {
    "Created_date": "2025-07-25 08:01:02",
    "Customer_Email": "johndoe@gmail.com"
  }
]
