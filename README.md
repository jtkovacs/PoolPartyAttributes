# PoolPartyAttributes

When you have many attributes in PoolParty, it's easy to accidentally duplicate them because there's no attribute search interface, just a browsing interface:

<img src="ppatts.png" width="500px">

However, attributes can be exported to an RDF-JSON format (.rf). This script extracts all attribute names from a PoolParty .rf file.

## Usage

1. Download ppatts.py
2. Export your PoolParty ontology to RDF-JSON format (.rf)
3. Make sure your .rf file is in the same folder as ppatts.py
4. Open your terminal in the same folder
5. Enter the command:

```Bash
python3 ppatt.py your_filename.rf
```

6. If you run into problems, make sure that you have **Python 3** with its **json** and **sys** libraries installed.
