# Locating Restriction Sites 

This project provides a Python script to identify **reverse palindromic sequences** in a DNA string (from FASTA format). It’s a common problem in bioinformatics, especially for locating **restriction enzyme recognition sites**.

---

## What is a Reverse Palindrome?

In DNA:
- A pairs with T
- C pairs with G

A reverse palindrome is a DNA segment that is equal to its **reverse complement**.

### Example
Sequence: `GCATGC`
- Reverse: `CGTACG`
- Complement: `GCATGC`  (Same as original)

---

## 🧾 Problem Statement
**Given**: A DNA sequence in FASTA format (length ≤ 1000 bp)

**Return**: The starting position (1-based) and length of every reverse palindrome having length between **4 and 12**.

---

## Input Format
FASTA format string:
```
>Rosalind_ID
TCAATGCATGCGGGTCTATATGCAT
```

---

## Output Format
Each line contains two numbers:
- Starting position (1-based)
- Length of the reverse palindrome

### Example Output
```
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
```

---

## How to Run

1. Clone the repository or download the script:
```bash
git clone https://github.com/Shouryanpatil/restriction-sites
cd restriction-sites
```

2. Run the script:
```bash
python restriction_sites.py
```

3. You can paste or hardcode your FASTA string in the script.

---

## Files
- `restriction_sites.py`: Python script to detect reverse palindromes.
- `README.md`: This file.

---

