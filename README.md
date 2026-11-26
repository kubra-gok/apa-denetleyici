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

1. Make sure Python is installed on your computer.
2. Download this project from GitHub: click the green **Code** button and choose **Download ZIP**. Then unzip the folder.
3. Open the terminal in the project folder and install the required libraries:
   ```
   pip install -r requirements.txt
   ```
4. Run the program:
   ```
   python apa_projesi.py
   ```
5. A window will open. Choose the Word (.docx) file you want to check. The mistakes will be listed in the terminal.

You can try it with `deneme_kaynakca.docx`, a sample reference list with six intentional mistakes.

## How I used AI

I developed this project with Claude (an AI assistant) as a helper.

- **Ideas:** I chose the topic from my own editing experience at Sakarya University Press. The AI helped me plan the steps.
- **Code:** At first, the AI wrote most of the code and explained it line by line. Later I started writing parts myself (for example the file check, the font rule and the DOI clean-up), and the AI reviewed them.
- **My decisions:** The rules come from mistakes I saw as an editor. The DOI verification method (comparing the title from Crossref with the reference) is the method I used by hand as an editor. The idea that the program should ask before changing anything was also mine.
- **Finding bugs:** I found several false positives myself. For example, the word "Doing" was detected as an old DOI format, and an italic title in the wrong place was not detected.
- **Testing:** The AI created a sample reference list with known mistakes. I used it to test my program and three similar tools.
- **Where the AI was wrong:** Some AI suggestions were incorrect, so I checked them. For example, the AI first thought there was no Turkish tool for this, but my research showed there is one.

## Limitations and future work

**Current limitations**
- The program is designed for English references. In Turkish references, APA uses "ve" instead of "&", so some rules give false warnings.
- The program only finds mistakes. It does not fix them yet.
- It checks the reference list only, not the citations in the text.
- Books usually have no DOI, so they cannot be verified with Crossref.

**Future work**
- **Language settings:** Adjust the rules for Turkish and English references.
- **Fixing DOIs:** When a DOI is wrong or missing, search Crossref with the title and suggest the correct DOI. As an editor, I did this by hand by trying possible corrections.
- **Human in the loop:** Show each correction and ask the user "Fix this? (y/n)". The program will save the approved changes to a new Word file and never change the original.
- **In-text citations:** Check that every citation in the text matches a reference in the list.

## Similar tools

I tested three similar tools with the same sample file (`deneme_kaynakca.docx`, six known mistakes).

| Check | Kaynakça Doğrula | Recite (free) | Edifix (paid) | This program |
|---|---|---|---|---|
| Year in parentheses | ❌ | ✅ | ✅ fixed | ✅ |
| "&" before last author | – | ✅ | ✅ fixed | ✅ |
| Italic journal/book title | ❌ | ❌ | ✅ fixed | ✅ |
| Same font | – | ❌ | ❌ (plain text only) | ✅ |
| Old DOI format | – | ❌ | ✅ fixed | ✅ |
| DOI exists (Crossref) | ✅ | ❌ (paid only) | ✅ | ✅ |
| In-text citations | – | ✅ | – | ❌ |

**What I learned:**
- Free tools missed most formatting mistakes.
- Edifix was the strongest tool. It also fixes the mistakes. But it is paid, it works with plain text (so it cannot check fonts), and it did not recognize the Turkish "ve".
- Recite is very good at matching in-text citations, but it did not recognize the Turkish heading "Kaynakça".
- My program is free, reads the Word file directly on the user's computer, and checks fonts. Fixing mistakes is the next step.