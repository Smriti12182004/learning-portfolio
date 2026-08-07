# Lab 4 – Command Line and Bash

## Status

**Completed**

---

## Objective

Learn Linux command-line utilities and Bash scripting by processing text files, building command pipelines, and automating word frequency analysis.

---

## Problem Statement

Create a parameterized Bash script (`top_words.sh`) that accepts a text file as input and an optional count (default: 10) and prints the most frequently occurring words using standard Unix command-line tools.

---

## Tasks Performed

- Downloaded text files using `curl`
- Counted lines, words, and characters using `wc`
- Built a command pipeline using `tr`, `sort`, `uniq`, and `head`
- Developed a reusable Bash script (`top_words.sh`)
- Accepted a filename and optional count as command-line arguments
- Made the script executable using `chmod +x`
- Executed the script on two different text files
- Documented the workflow with screenshots

---

## Commands Used

```bash
curl
wc
tr
sort
uniq
head
chmod +x
```

---

## Script Usage

Default (Top 10 words)

```bash
./top_words.sh pg11.txt
```

Custom count

```bash
./top_words.sh pg11.txt 15
```

---

## Screenshots

- Text file download
- Word frequency pipeline
- Word count statistics
- Script execution with custom count
- Script execution on a second text file

---

## Learning Outcomes

After completing this lab, I gained practical experience in:

- Using Linux command-line tools.
- Processing text with Unix pipelines.
- Writing parameterized Bash scripts.
- Making shell scripts executable.
- Automating repetitive text-processing tasks.
- Working with command-line arguments.

---

## Technologies Used

- Ubuntu Linux
- Bash
- Visual Studio Code
- Git
- GitHub

---

## Resources Used

- Project Gutenberg
- Bash Manual
- GNU Coreutils Documentation
- Ubuntu Documentation
