# APA Reference Checker

## Why I built this
I worked as an editor at Sakarya University Press. Part of my job was checking reference lists against APA rules by hand. For every reference, I opened the DOI link and compared the title and journal name with the reference list. It took me a lot of time, and small mistakes were easy to miss. So I asked myself: how can I do this faster and more accurately? This is why I started this project

## What it checks

This program checks reference lists in Word (.docx) files against APA 7 rules and shows the mistakes it finds. It is designed to help editors.

- The year is in parentheses, like (2020).
- "&" is used before the last author, not "and" or "ve".
- The journal or book title is in italics.
- All references use the same font (Times New Roman).
- DOIs use the correct format: https://doi.org/...
- The DOI exists in Crossref and belongs to the right article.

## How DOI verification works
When I worked as an editor, I checked DOIs by hand. The program follows the same steps:

1. **Find the DOI.** Every DOI starts with "10.", followed by numbers and a slash. The program looks for this pattern in each reference. If the DOI ends with a period, the program reports it and removes the period, because APA does not allow it.
2. **Ask Crossref.** Crossref is a database of registered DOIs. The program sends the DOI to Crossref. If Crossref cannot find it, the program reports that the DOI may be wrong or fake.
3. **Compare the titles.** If the DOI exists, Crossref returns the real title of the article. The program checks how many words of this title appear in the reference. If fewer than 70% of the words match, the DOI may belong to a different article. The titles do not need to match exactly, because they are often written differently (for example, in capital letters).
## How to run it

## Limitations and future work