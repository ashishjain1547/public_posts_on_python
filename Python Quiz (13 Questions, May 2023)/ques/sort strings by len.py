"""Both list.sort and sorted take two optional, keyword-only arguments: key and reverse.

reverse

If True, the items are returned in descending order, i.e. by reversing the comparison
of the items. The default is False.

...

key

A one-argument function that will be applied to each item to produce its sorting
key. For example, when sorting a list of strings, key=str.lower can be used to
perform a case-insensitive sort, and key=len will sort the strings by character
length. The default is the identity function, i.e. the items themselves are compared."""


l = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
l.sort(key = len)
print(l)
