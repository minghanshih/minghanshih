"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a sentence typed by the user
# 2. Process: Transform the sentence in four different ways
# 3. Out: The four transformed sentences
# 4. My four transformations, and when each is useful: 
#    strip(): remove extra spaces when cleaning data from a form
#    upper(): make a headline or a banner stand out
#    title(): format a product name or an article title 
#    replace(" ", "-"): build a URL from a title


# Your code below
# Ask the user for a sentence
sentence = input("Type a sentence: ")

# Remove extra spaces at both ends of the sentence
print(sentence.strip())

# Capital letter for all letters
print(sentence.upper())

# Capital letter at the start of each word
print(sentence.title())

# Replace spaces with dashes
print(sentence.replace(" ", "-"))

# CHECK IT YOURSELF (input:"   hello World   ")
# strip():"hello World" - expected, space removed
# upper():"   HELLO WORLD   " - expected, all letters capitalized, but the spaces at the ends are still there
# title():"   Hello World   " - expected, first letter of each word capitalized, spaces still there
# replace(" ", "-"):"---hello-World---" - not expected, the spaces at the ends also became dashes
