# PoolPartyAttributes

<br>

**When you have many attributes in PoolParty, it's easy to accidentally duplicate them because there's no attribute search interface, just a browsing interface:**

<img src="illos/ppatts.png" width="500px">

<br>

**However, PoolParty lets you export your entire ontology (attributes, relations, and classes) to several different formats, including RDF-JSON (.rj):**

<img src="illos/rdf-json.png" width="400px">

<br>

**This very simple script extracts all attribute names from a PoolParty .rj file and outputs a sorted list to a plain text file. To run this script, you need *Python 3* with its *json* and *sys* libraries installed.**

<br>
<br>

## Usage

1. Export your PoolParty ontology to RDF-JSON format (.rj)
2. Download `ppatts.py` to the same folder
3. Open your terminal in the same folder, and enter the command:

```Bash
$ python3 ppatt.py your_filename.rj
```

4. Open the output file (`ppatt_out.txt`), note the total# extracted terms at the top of the document, and check this total against your PoolParty ontology stats
