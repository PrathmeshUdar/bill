# LOG

## Day 1 (Mon 23 Nov): Think first, save your work

### Hypotheses
- `cd Desktop` said "The system cannot find the path specified". I think I was not in my home folder, so there was no Desktop folder there.
- `python bill.py` said it could not open the file. I think Notepad never saved `bill.py`, because `dir` showed 0 files.
- `split_bill(100, 0)` should crash with `ZeroDivisionError`, so I need a check for zero people.

### What got me stuck
- Not knowing where to type commands (the Command Prompt window).
- The `bill` folder was empty, because Notepad did not save my file.
- Getting "A subdirectory or file bill already exists" after running `mkdir bill` twice.

### What I learned
- Git stores snapshots, so a deleted file comes back with `git restore`.
- Working tree = my files now. Staging area = changes I picked with `git add`. Commit = the saved snapshot.
- A traceback is read from the bottom: the last line is the error, the line above is where it happened.
- A venv gives each project its own packages.
- Edge cases like zero people, negative numbers and rounding (10.00 / 3 leaves a penny) must be thought about before coding.
