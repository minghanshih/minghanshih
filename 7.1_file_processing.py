# What is wrong with names.txt (found by reading it, not by guessing):
# - There are empty lines (line 3 and line 9).
# - Some lines start with spaces ("  alan TURING", "  linus torvalds").
# - The capitals are a mess: "ada LOVELACE", "grace hopper", "GUIDO van rossum".
# - One person has a last name with 2 words: "van rossum".
# - The names are not in any order.

# 1. In: names.txt, 10 lines, first name then last name
# 2. Process, problem by problem:
#    Empty lines: I skip them.
#    Spaces at the start: strip() removes them.
#    Mixed capitals: title() writes every name like "Ada Lovelace".
#    Two-word last name: I take everything after the first word as the last name.
#    No order: I sort with the last name.
# 3. Out: names_sorted.txt, one clean name per line, sorted by last name.
#    names.txt is only read, never changed.
# 4. How I decide which word is the last name:
#    The first word is always the first name, so the last name is everything after it.
#    If I only took the last word, Guido van Rossum would be sorted at "Rossum" and
#    "van" would be lost.

# Your code below
# Read all the lines, "r" by default, so the original file is not changed
with open("names.txt", encoding="utf-8") as f:
    lines = f.readlines()

# Clean each line: remove spaces, skip empty lines, fix the capitals
names = []
for line in lines:
    clean = line.strip()
    if clean == "":
        continue
    clean = clean.title()
    names.append(clean)


# Give back the last name: every word after the first one
def last_name(full_name):
    words = full_name.split()
    return " ".join(words[1:])


# Sort the list using the last name
names = sorted(names, key=last_name)

# Write the clean list in a new file
with open("names_sorted.txt", "w", encoding="utf-8") as f:
    for name in names:
        f.write(name + "\n")

print("Lines in names.txt:", len(lines))
print("Names saved in names_sorted.txt:", len(names))

# CHECK IT YOURSELF
# names.txt has 10 lines, names_sorted.txt has 8. The 2 missing lines are the empty ones.
# First name in the sorted list: Margaret Hamilton (H). Last one: Guido Van Rossum (V).
# I checked by hand: H, Ho, J, Li, Lo, Tor, Tu, V. Correct.
# title() writes "Van Rossum" with a capital V, the real name is "van Rossum".
# I accept this small mistake.