# Burglary Series (16): Nested Objects (Dicts)
# And who cursed the most in the fight between you and your spouse?
#
# Given a dict with three rounds, with nested dicts as your score per round, return who cursed the most based on the following:
#
# If you, return "ME!"
# If your spouse, return "SPOUSE!"
# If a draw, return "DRAW!"
# Examples
# determine_who_cursed_the_most({
#   "round1": { "me": 10, "spouse": 5 },
#   "round2": { "me": 5, "spouse": 10 },
#   "round3": { "me": 10, "spouse": 10 }}) ➞ "DRAW!"
#
# determine_who_cursed_the_most({
#   "round1": { "me": 40, "spouse": 5 },
#   "round2": { "me": 9, "spouse": 10 },
#   "round3": { "me": 9, "spouse": 10 }}) ➞ "ME!"
#
# determine_who_cursed_the_most({
#   "round1": { "me": 10, "spouse": 5 },
#   "round2": { "me": 9, "spouse": 44 },
#   "round3": { "me": 10, "spouse": 55 }}) ➞ "SPOUSE!"
# Notes
# N/A
def determine_who_cursed_the_most(nested_dict):
    dicti = {}
    inner= {}
    for rounds in nested_dict.keys():
        dicti[rounds] = nested_dict[rounds]
        for keyy in dicti[rounds]:
            if keyy not in inner:
                inner[keyy] = dicti[rounds][keyy]
            else:
                inner[keyy] += dicti[rounds][keyy]
    if inner["me"] == inner["spouse"]:
        return "Draw"
    return max(inner , key = inner.get)
print(determine_who_cursed_the_most({
  "round1": { "me": 40, "spouse": 5 },
  "round2": { "me": 9, "spouse": 10 },
  "round3": { "me": 9, "spouse": 10 }}))