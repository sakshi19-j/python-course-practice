# Python Course Practice

Small Python exercises and projects completed while learning the basics.

## Learning log

The scripts do not include dates or day numbers, so entries are grouped by the concepts they demonstrate:

- **Inputs and strings** — collected a city and pet name to generate a band name (`project1.py`).
- **Data types and conversion** — printed strings, numbers, and booleans; converted input and counted characters (`datatype.py`).
- **Numbers and calculations** — calculated a tip and split a bill between people (`tipcalculator.py`).
- **Conditionals** — checked even and odd numbers and built a pizza-price calculator (`evenorodd.py`, `pizzacode.py`).
- **Lists and randomness** — selected a random friend from a list (`list.py`).
- **Random choices and comparisons** — created a rock-paper-scissors game against the computer (`rock_paper_Scissors.py`).
- **Nested decisions** — used branching choices to create a text adventure (`treasureisland.py`).

## Review notes

- `list.py` is a generic module name, and the script reuses `random` for a selected friend, overwriting the imported module name. A more descriptive filename and variable would avoid confusion.
- `pizzacode.py` treats any unrecognized pizza size as large; input validation would make that behavior safer.
- `tipcalculator.py` divides by the number of people, so the input should be greater than zero.
- `rock_paper_Scissors.py` currently reports scissors beating rock; that result should be a loss.

These are beginner practice programs; the review notes are suggestions, not changes made to the scripts.
