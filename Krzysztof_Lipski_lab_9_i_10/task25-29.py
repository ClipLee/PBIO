from Bio import Entrez

Entrez.email = "s20901@pjwstk.edu.pl"

handle = Entrez.esearch(db="pubmed", term="colon cancer", retmax=10)
record = Entrez.read(handle)

handle = Entrez.efetch(db="pubmed", id=record["IdList"],
                       rettype="medline", retmode="text")
records = handle.read()

for record in records.split("\n\n"):
    if record.strip():
        title = ""
        authors = ""
        date = ""

        for line in record.split("\n"):
            if line.startswith("TI"):
                title = line[6:].strip()
            elif line.startswith("AU"):
                authors = line[6:].strip()
            elif line.startswith("DP"):
                date = line[6:].strip()

        print("Tytuł:", title)
        print("Autorzy:", authors)
        print("Data publikacji:", date, '\n')
