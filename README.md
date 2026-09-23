# COS 184: Introduction to Python - Lecture Notebooks

Lecture materials I wrote and taught as **instructor of record** for COS 184,
*Introduction to Python*.

The course had an assigned textbook, *Murach's Python Programming*, and the
lectures follow and add extra examples to its chapter sequence so students could read
along. The teaching materials supplied with the course were the publisher's 
slide decks. I judged those insufficient for the room I had and replaced them. 
The lecturenotebooks are my own work: the interactive structure, the 
spaced-repetition review that opens each session, and the explanations built 
around where students actually got stuck were written for this course and run
live in front of the class.

## How the lectures are designed

**Notebooks, not slides.** Every lecture is a runnable notebook. Concepts are
introduced with code that executes in front of students, gets deliberately
broken, and is fixed on the spot. Students followed along in Google Colab and
could re-run every example after class.

**Every lecture opens with spaced-repetition review.** Each notebook begins
with a `Review` section that revisits the previous one or two sessions'
material with fresh examples before anything new is introduced. Topics
resurface across several lectures rather than being covered once and left.

**Built around the concepts students reliably trip on.** The sequence and the
depth of each topic were tuned to where students actually struggled, not to
chapter boundaries. The clearest example is references versus copies of
lists. Explaining aliasing in words did not work, so I stopped doing that
and instead drew the memory layout on the whiteboard while the code ran,
showing which variable pointed at which object as each line executed. That
resolved it, and the same approach carried into shallow versus deep copies
of nested lists.

**Named, complete programs.** Most lectures end by assembling the day's
ideas into one small complete program (a test-score calculator, a dice game,
Hangman, a hotel reservation system, a book catalog) followed by a short
in-class activity.

## Lecture index

Lecture 1 was the course introduction: the syllabus, a tour of the Google
Colab environment, and an introduction to Markdown. It had no notebook, which
is why it is not included here.

| # | Notebook | Topics |
|---|----------|--------|
| 2 | [lecture-02](lectures/lecture-02.ipynb) | Comments, `print()`, data types and variables, naming rules, arithmetic and precedence, compound assignment, string concatenation, escape sequences, `sep`/`end`, `input()` |
| 3 | [lecture-03](lectures/lecture-03.ipynb) | Combining the basics into a full program; `int()`, `float()`, `round()` and rounding rules |
| 4 | [lecture-04](lectures/lecture-04.ipynb) | Type conversion, chaining `input()`, Boolean expressions, logical operators, string comparison, `if` statements |
| 5 | [lecture-05](lectures/lecture-05.ipynb) | Relational and logical operators, `match` statements, nested `if`, input validation (Miles Per Gallon and Invoice programs), first look at `while` |
| 6 | [lecture-06](lectures/lecture-06.ipynb) | `while` loops, `range()`, `break` and `continue`, `for` vs `while`, assignment expressions (`:=`), Test Scores program |
| 7 | [lecture-07](lectures/lecture-07.ipynb) | Defining functions, parameters and arguments, `main()`, default parameter values |
| 8 | [lecture-08](lectures/lecture-08.ipynb) | Local vs global scope, writing and importing your own module, the three `import` forms, `help()` |
| 9 | [lecture-09](lectures/lecture-09.ipynb) | Global constants, docstrings and type hints, the `random` module, Number Guessing game, Pig dice game |
| 10 | [lecture-10](lectures/lecture-10.ipynb) | Hierarchy charts; lists: creation, indexing, get/set, `append`/`insert`/`remove`, `pop`/`index`, `len`, `in`, iterating |
| 11 | [lecture-11](lectures/lecture-11.ipynb) | Mutable vs immutable types, `enumerate()` and `zip()`, processing lists in parallel, Movie List program, lists of lists |
| 12 | [lecture-12](lectures/lecture-12.ipynb) | `count`/`reverse`/`sort` vs `sorted`, case-sensitive sorting, `min`/`max`/`sum`, `random.choice`/`shuffle`, **references vs copies (assignment, shallow, deep)**, slicing, concatenation, `map`/`filter` |
| 13 | [lecture-13](lectures/lecture-13.ipynb) | `functools.reduce`, list comprehensions, functions that return tuples, introduction to file I/O |
| 14 | [lecture-14](lectures/lecture-14.ipynb) | Tuples and unpacking; files: `open`/`close`, `with`, writing, the three ways to read lines; `csv` module; `pickle` |
| 15 | [lecture-15](lectures/lecture-15.ipynb) | Movie List program with CSV persistence, `pickle`, the `math` module, `floor`/`ceil` |
| 16 | [lecture-16](lectures/lecture-16.ipynb) | F-string format specifications, rounding accurately, the `locale` module, `Decimal` and `quantize` |
| 17 | [lecture-17](lectures/lecture-17.ipynb) | `Decimal` in practice (Future Value program); strings: `ord`/`chr`, slicing, multi-line strings, `in`, `isdigit`, `startswith`, `title` |
| 18 | [lecture-18](lectures/lecture-18.ipynb) | `find`, `replace`, `removeprefix`/`removesuffix`, Create Account validator, `split`, `join`, Hangman |
| 19 | [lecture-19](lectures/lecture-19.ipynb) | Dates and times: `date`/`time`/`datetime` constructors, `strptime`, `timedelta`, Timer program |
| 20 | [lecture-20](lectures/lecture-20.ipynb) | Parsing user-entered dates, `timedelta` attributes and `total_seconds()`, Timer program completed |
| 21 | [lecture-21](lectures/lecture-21.ipynb) | Date attributes, building dates from today's date, comparing dates, days-until calculations, two-digit years |
| 22 | [lecture-22](lectures/lecture-22.ipynb) | Hotel Reservation program; dictionaries: lookup, `get`, adding, `del`/`pop`/`popitem`, `keys`/`values`/`items`, constructors, Country Code program |
| 23 | [lecture-23](lectures/lecture-23.ipynb) | The `\|=` update operator, nested dictionaries, dictionaries of lists, Book Catalog program |
| 24 | [lecture-24](lectures/lecture-24.ipynb) | Exceptions: `ValueError`, catching multiple exceptions, `try`/`except`/`else`/`finally`, `sys.exit()`, `raise` |
| 25 | [lecture-25](lectures/lecture-25.ipynb) | Moving from Colab to a local IDE; standard-library tour (`collections.Counter`, `statistics`, `json`, `pathlib`); live demos with `requests`, `matplotlib`, `qrcode`, `pyfiglet`; where to go next |

## Review notebooks

[reviews/](reviews/) holds the two study guides I wrote for students before
each exam: [midterm-review](reviews/midterm-review.ipynb) (Lectures 2–15)
and [final-review](reviews/final-review.ipynb) (Lectures 16–24). Each is a
compact re-teaching of the half-course with runnable examples. A few cells
in the midterm review raise errors on purpose and are labelled so; the
reader is asked to predict the exception before running the cell.

## What is not here

Labs, quizzes, the midterm, the final exam, and all grading material are not included. 
Exam logistics have also been removed from the review notebooks.

No publisher slides, text, or figures are included.

## Using the notebooks

```bash
git clone https://github.com/CameronLetendre/cos184-python-course-materials.git
cd cos184-python-course-materials
jupyter lab
```

Any Jupyter front end works, including VS Code and Google Colab. The notebooks
use only the standard library, except for Lecture 25, which installs a few
third-party packages inline as part of the demo.

Every file a lecture reads is in [data/](data/) and the notebooks open them
by relative path (`../data/...`), so everything runs from a fresh clone with
no setup. The two tabular datasets, `stress.csv` and `car_price.csv`, are
synthetic and generated by `data/make_synthetic.py`; the two prose texts are
public domain. The small `temperature.py` module that lectures 8 and 9 import
sits beside the notebooks in `lectures/`. The file-I/O lectures also write
scratch files next to themselves as they run; those are ignored by git.

Some cells raise errors on purpose (indexing past the end of a string,
mixing `Decimal` and `float`, a `while True` loop that never ends). They were
part of the live demonstration and are left as taught.

## License

Copyright 2026 Cameron Letendre. Licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to
reuse and adapt this material with attribution.
