# =============================================================
#  PYTHON DICTIONARIES - from absolute basics to advanced
# =============================================================
# A dictionary (dict) stores data as KEY : VALUE pairs.
# Think of a real dictionary: the word is the key, the meaning is the value.
# Dictionaries are:
#   - Mutable   : you can add, change and remove items
#   - Ordered   : items keep insertion order (Python 3.7+)
#   - Keyed     : you look values up by key, not by position (index)
#   - Unique    : each key can appear only once (a repeated key overwrites)


# -------------------------------------------------------------
# 1. CREATING DICTIONARIES
# -------------------------------------------------------------
student = {"name": "Arpan", "age": 23, "city": "Kolkata"}
print(student)                  # {'name': 'Arpan', 'age': 23, 'city': 'Kolkata'}
print(type(student))            # <class 'dict'>

empty1 = {}                     # empty dictionary (most common way)
empty2 = dict()                 # same thing, using the constructor
print(empty1, empty2)

# dict() with keyword arguments (keys must be simple names, become strings)
person = dict(name="Dutta", age=30)
print(person)

# dict() from a list of (key, value) pairs
pairs = [("a", 1), ("b", 2), ("c", 3)]
print(dict(pairs))              # {'a': 1, 'b': 2, 'c': 3}

# dict.fromkeys(keys, default_value): many keys, same starting value
print(dict.fromkeys(["x", "y", "z"], 0))   # {'x': 0, 'y': 0, 'z': 0}

# zip() two lists together into a dictionary
keys = ["math", "science", "english"]
marks = [90, 85, 88]
print(dict(zip(keys, marks)))   # {'math': 90, 'science': 85, 'english': 88}


# -------------------------------------------------------------
# 2. ACCESSING VALUES
# -------------------------------------------------------------
print(student["name"])          # Arpan  (square brackets with the key)

# print(student["phone"])       # KeyError! the key does not exist

# .get() is safer: returns None (or a default you choose) instead of crashing
print(student.get("phone"))             # None
print(student.get("phone", "N/A"))      # N/A
print(student.get("age", 0))            # 23 (key exists, so default is ignored)


# -------------------------------------------------------------
# 3. ADDING AND UPDATING ITEMS
# -------------------------------------------------------------
student["email"] = "arpan@example.com"   # new key -> added
student["age"] = 24                      # existing key -> value updated
print(student)

# .update() changes/adds several items at once
student.update({"age": 25, "country": "India"})
print(student)

# .setdefault(key, default): returns value if key exists,
# otherwise inserts the key with the default and returns it
student.setdefault("grade", "A")
student.setdefault("name", "Someone Else")   # ignored, name already exists
print(student)


# -------------------------------------------------------------
# 4. REMOVING ITEMS
# -------------------------------------------------------------
data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

print(data.pop("a"))            # removes 'a' and RETURNS its value -> 1
print(data.pop("zzz", "none"))  # with a default, no KeyError -> 'none'
print(data.popitem())           # removes & returns the LAST pair -> ('e', 5)
del data["b"]                   # removes key 'b' (KeyError if missing)
print(data)                     # {'c': 3, 'd': 4}
data.clear()                    # removes everything
print(data)                     # {}
# del data                      # would delete the whole variable itself


# -------------------------------------------------------------
# 5. KEYS, VALUES AND ITEMS
# -------------------------------------------------------------
info = {"name": "Arpan", "age": 23, "city": "Kolkata"}

print(info.keys())      # dict_keys(['name', 'age', 'city'])
print(info.values())    # dict_values(['Arpan', 23, 'Kolkata'])
print(info.items())     # dict_items([('name', 'Arpan'), ('age', 23), ('city', 'Kolkata')])

print(list(info.keys()))        # convert the view to a normal list

# These are LIVE views: they reflect later changes to the dictionary
k = info.keys()
info["job"] = "Developer"
print(k)                        # now includes 'job' too


# -------------------------------------------------------------
# 6. CHECKING MEMBERSHIP & SIZE
# -------------------------------------------------------------
print("name" in info)           # True  (checks KEYS)
print("Arpan" in info)          # False (values are not checked)
print("Arpan" in info.values()) # True
print("zip" not in info)        # True
print(len(info))                # number of key-value pairs -> 4


# -------------------------------------------------------------
# 7. LOOPING THROUGH A DICTIONARY
# -------------------------------------------------------------
scores = {"math": 90, "science": 85, "english": 88}

for key in scores:                      # default: loops over keys
    print(key)

for value in scores.values():           # loop over values
    print(value)

for key, value in scores.items():       # loop over both (most useful)
    print(f"{key} -> {value}")

# enumerate gives a counter too
for i, (subject, mark) in enumerate(scores.items(), start=1):
    print(i, subject, mark)

# NEVER add/remove keys while looping over the same dict (RuntimeError).
# Loop over a copy instead:
for key in list(scores.keys()):
    if scores[key] < 86:
        del scores[key]
print(scores)                           # {'math': 90, 'english': 88}


# -------------------------------------------------------------
# 8. RULES FOR KEYS AND VALUES
# -------------------------------------------------------------
# Keys must be IMMUTABLE (hashable): str, int, float, bool, tuple (of immutables)
# Values can be ANYTHING: numbers, strings, lists, other dicts, functions...
mixed = {
    1: "int key",
    "two": "str key",
    3.5: "float key",
    (4, 5): "tuple key",
    "list_value": [1, 2, 3],
    "dict_value": {"inner": True},
}
print(mixed[(4, 5)])            # tuple key

# mixed[[1, 2]] = "x"           # TypeError: lists are unhashable (mutable)

# Duplicate keys: the last one wins
dup = {"a": 1, "a": 2}
print(dup)                      # {'a': 2}

# Keys are case-sensitive
print({"Name": 1, "name": 2})   # two different keys


# -------------------------------------------------------------
# 9. COPYING DICTIONARIES
# -------------------------------------------------------------
original = {"a": 1, "b": [10, 20]}

alias = original                # NOT a copy, same object!
alias["a"] = 99
print(original)                 # {'a': 99, ...} changed too

shallow = original.copy()       # new dict, but nested objects are shared
shallow["a"] = 1
shallow["b"].append(30)         # affects original too (shared list)
print(original)                 # {'a': 99, 'b': [10, 20, 30]}

import copy
deep = copy.deepcopy(original)  # fully independent copy
deep["b"].append(40)
print(original["b"], deep["b"]) # [10, 20, 30] [10, 20, 30, 40]


# -------------------------------------------------------------
# 10. MERGING DICTIONARIES
# -------------------------------------------------------------
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

merged = {**d1, **d2}           # unpacking (works in all Python 3.5+)
print(merged)                   # {'a': 1, 'b': 20, 'c': 3}  (later wins)

merged2 = d1 | d2               # union operator (Python 3.9+)
print(merged2)

d1 |= d2                        # in-place merge (like update)
print(d1)


# -------------------------------------------------------------
# 11. NESTED DICTIONARIES
# -------------------------------------------------------------
company = {
    "emp1": {"name": "Asha", "skills": ["python", "sql"]},
    "emp2": {"name": "Ravi", "skills": ["java"]},
}
print(company["emp1"]["name"])          # Asha
print(company["emp1"]["skills"][0])     # python

company["emp3"] = {"name": "Meera", "skills": []}   # add a nested dict
company["emp2"]["skills"].append("go")              # modify inside

# Safe deep access with chained .get()
print(company.get("emp9", {}).get("name", "unknown"))   # unknown

for emp_id, details in company.items():
    print(emp_id, details["name"], len(details["skills"]))


# -------------------------------------------------------------
# 12. DICTIONARY COMPREHENSIONS
# -------------------------------------------------------------
# Syntax: {key_expr: value_expr for item in iterable if condition}
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)                  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_squares = {n: n ** 2 for n in range(1, 11) if n % 2 == 0}
print(even_squares)

# Swap keys and values (values must be unique & hashable)
prices = {"apple": 50, "banana": 20}
print({v: k for k, v in prices.items()})    # {50: 'apple', 20: 'banana'}

# Transform / filter an existing dictionary
discounted = {k: v * 0.9 for k, v in prices.items()}
expensive = {k: v for k, v in prices.items() if v > 30}
print(discounted, expensive)


# -------------------------------------------------------------
# 13. SORTING DICTIONARIES
# -------------------------------------------------------------
marks = {"Ravi": 72, "Asha": 95, "Meera": 88}

print(sorted(marks))                            # sorted keys (a list)
print(dict(sorted(marks.items())))              # sorted by key
print(dict(sorted(marks.items(), key=lambda kv: kv[1])))                # by value, ascending
print(dict(sorted(marks.items(), key=lambda kv: kv[1], reverse=True)))  # descending

print(max(marks, key=marks.get))                # key with highest value -> Asha
print(min(marks, key=marks.get))                # key with lowest value  -> Ravi
print(sum(marks.values()) / len(marks))         # average mark


# -------------------------------------------------------------
# 14. COMMON PATTERNS (counting & grouping)
# -------------------------------------------------------------
# Count how often each character appears
text = "mississippi"
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
print(count)                    # {'m': 1, 'i': 4, 's': 4, 'p': 2}

# Group words by their first letter
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
groups = {}
for w in words:
    groups.setdefault(w[0], []).append(w)
print(groups)   # {'a': ['apple', 'avocado'], 'b': [...], 'c': ['cherry']}


# -------------------------------------------------------------
# 15. ADVANCED: collections MODULE HELPERS
# -------------------------------------------------------------
from collections import defaultdict, Counter, OrderedDict

# defaultdict: missing keys get an automatic default value
dd = defaultdict(list)
for w in words:
    dd[w[0]].append(w)          # no need to check if key exists
print(dict(dd))

dd_int = defaultdict(int)       # missing key -> 0
for ch in "banana":
    dd_int[ch] += 1
print(dict(dd_int))

# Counter: a dictionary specialised for counting
c = Counter("mississippi")
print(c)                        # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(c.most_common(2))         # [('i', 4), ('s', 4)]

# OrderedDict: remembers order and has move_to_end (rarely needed now,
# since normal dicts are already ordered)
od = OrderedDict(a=1, b=2, c=3)
od.move_to_end("a")
print(od)                       # b, c, a


# -------------------------------------------------------------
# 16. ADVANCED: MORE POWER TOOLS
# -------------------------------------------------------------
# Dictionary of functions (a simple "switch" / dispatch table)
def add(a, b): return a + b
def sub(a, b): return a - b

operations = {"+": add, "-": sub, "*": lambda a, b: a * b}
print(operations["+"](6, 3))    # 9
print(operations["*"](6, 3))    # 18

# Unpack a dict into function keyword arguments with **
def greet(name, city):
    return f"Hello {name} from {city}"

print(greet(**{"name": "Arpan", "city": "Kolkata"}))

# Accept any keyword arguments as a dict with **kwargs
def show(**kwargs):
    for k, v in kwargs.items():
        print(k, "=", v)

show(a=1, b=2)

# Dictionaries are the basis of JSON
import json
as_text = json.dumps(student, indent=2)     # dict -> JSON string
print(as_text)
print(json.loads(as_text) == student)       # JSON string -> dict -> True

# Read-only view of a dictionary
from types import MappingProxyType
ro = MappingProxyType({"pi": 3.14})
print(ro["pi"])
# ro["pi"] = 3                  # TypeError: read-only


# -------------------------------------------------------------
# QUICK CHEAT SHEET
# -------------------------------------------------------------
# d = {}                  create             d[k]            get (KeyError if missing)
# d.get(k, default)       safe get           d[k] = v        add / update
# d.update(other)         merge in           d.setdefault()  get or insert
# d.pop(k)                remove & return    del d[k]        remove
# d.popitem()             remove last        d.clear()       empty it
# d.keys() / values() / items()              k in d          membership
# len(d)                  size               d.copy()        shallow copy
# {k: v for ...}          comprehension      d1 | d2         merge (3.9+)
