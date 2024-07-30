# Tidy Title and Author Strings
# You have a list of strings, each consisting of a book title and an author's name.
#
# To illustrate:
#
# [
#   ["   Death of a Salesman - Arthur Miller    "],
#   ["   Macbeth - William Shakespeare    "],
#   ["    A Separate Peace - John Knowles     "],
#   [" Lord of the Flies - William Golding"],
#   ["A Tale of Two Cities - Charles Dickens"]
# ]
# Create a function that takes a list like the one above and transforms it into the same format as the one below:
#
# [
#   ["Death of a Salesman", "Arthur Miller"],
#   ["Macbeth", "William Shakespeare"],
#   ["A Separate Peace", "John Knowles"],
#   ["Lord of the Flies", "William Golding"],
#   ["A Tale of Two Cities", "Charles Dickens"]
# ]
# Examples
# tidy_books([
#   ["     The Catcher in the Rye - J. D. Salinger    "],
#   ["    Brave New World - Aldous Huxley   "],
#   ["    Of Mice and Men - John Steinbeck    "]
# ]) ➞ [
#   ["The Catcher in the Rye", "J. D. Salinger"],
#   ["Brave New World", "Aldous Huley"],
#   ["Of Mice and Men", "John Steinbeck"]
# ]
# Notes
# Some of these entries have excess white space. Remove this white space in your final output.

def tidy_title(lis_string):
    splitter = []
    for ith in lis_string:
        for jth in ith:
            split_in = jth.split("-")
            final_splitter = [j.strip() for j in split_in]
            splitter.append(final_splitter)


    return splitter
print(tidy_title([
  ["   Death of a Salesman - Arthur Miller    "],
  ["   Macbeth - William Shakespeare    "],
  ["    A Separate Peace - John Knowles     "],
  [" Lord of the Flies - William Golding"],
  ["A Tale of Two Cities - Charles Dickens"]
]))

#another way from Chat GPT
def tidy_books(books):
    result = []
    for book in books:
        # Strip leading and trailing whitespace and then split by " - "
        title, author = book[0].strip().split(' - ')

        # Append the cleaned up title and author as a list to the result
        result.append([title, author])
    return result

# Test case
print(tidy_books([
    ["     The Catcher in the Rye - J. D. Salinger    "],
    ["    Brave New World - Aldous Huxley   "],
    ["    Of Mice and Men - John Steinbeck    "]
]))  # ➞ [["The Catcher in the Rye", "J. D. Salinger"], ["Brave New World", "Aldous Huxley"], ["Of Mice and Men", "John Steinbeck"]]
