# PoolPartyAttributes

When you have many attributes in PoolParty, it's easy to accidentally duplicate them because there's no attribute search interface, just a browsing interface:

<img src="ppatts.png" width="500px">

However, attributes can be exported to an RDF-JSON format (.rf). This script extracts all attribute names from a PoolParty .rf file.

## Usage

```Bash
python3 ppatt.py filename.rf
```
