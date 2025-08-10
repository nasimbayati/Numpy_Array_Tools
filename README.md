# NumPy Array Tools

A Python utility showcasing two powerful NumPy features:
1. **Array Intersection** – Finds the unique, sorted intersection of two arrays.
2. **Broadcasting Addition** – Adds two arrays following NumPy broadcasting rules.

---

## Features
- Accepts arrays inline or from `.npy` files.
- Works with numbers, strings, or mixed data types.
- Demonstrates broadcasting rules for automatic shape alignment.

---

## Installation
```bash
pip install numpy
```

## Usage

## Run Demo Mode

```bash
python numpy_array_tools.py
```

**Intersection Example (inline input)**
```bash
python numpy_array_tools.py intersect \
    --a "[['joe','Joe','harry'],['frank','alice','jim'],['Will','sam','tom']]" \
    --b "[['joe','Joe','heather'],['frank','alice','frank'],['Will','bill','martha']]"

```

## Broadcasting Addition Example (inline input)

```bash
python numpy_array_tools.py add \
    --a "[[33,59,24],[16,12,18]]" \
    --b "[13,16,47]"
```

## Using .npy Files
```bash
# Save arrays
python -c "import numpy as np; np.save('arrA.npy', np.array([[1,2],[3,4]])); np.save('arrB.npy', np.array([10,20]))"

# Use with script
python numpy_array_tools.py add --a arrA.npy --b arrB.npy
```

## Broadcasting Rules
Two shapes are **broadcast-compatible** if:

* Each dimension matches **or**

* One of them is 1


Example:
```bash
(2, 3) + (3,) ✅ works
(2, 3) + (2, 1) ✅ works
(2, 3) + (2, 2) ❌ fails
```

## Output Examples

## Intersection
```bash
['Joe' 'Will' 'alice' 'frank' 'joe']
```

## Broadcasting Addition

```bash
[[46 75 71]
 [29 28 65]]

 ```
