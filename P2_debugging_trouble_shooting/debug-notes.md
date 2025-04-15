# 🐛 Debugging Notes – Part 2: Debugging & Troubleshooting

## Overview

This part of the Franc interview involved identifying and fixing a bug in a calculator module, as well as dealing with several setup issues related to Python environment configuration and `pyproject.toml`.

---

## ⚙️ Setup Issues

### 1. Missing `requirements.txt`
Initial installation failed with:
```
error: File not found: `requirements.txt`
```
**Fix:** Switched to using `pyproject.toml` and `uv` for dependency management.

---

### 2. `pyproject.toml` Parse Error
Original file included:
```toml
[project.dependencies]
pytest = "^7.3.1"
```
which caused:
```
TOML parse error at line 20, column 1
invalid type: map, expected a sequence
```

**Fix:** Replaced with the correct format:
```toml
dependencies = [
  "pytest>=7.3.1"
]
```
Also removed duplicate `[project]` headers.

---

### 3. `pytest` Not Found
Ran:
```bash
python3 -m pytest
```
Got:
```
No module named pytest
```
**Fix:** Activated the virtual environment:
```bash
source .venv/bin/activate
```
Then ran:
```bash
pytest
```

---

## ✅ Bug Found in `divide()` Function

### ❌ Original Buggy Code:
```python
if a < 0:
    return -(-a // b)
```
This used integer floor division (`//`) for negative inputs, leading to incorrect results for floats (e.g., `-7 / 2 == -3`, but should be `-3.5`).

### ✅ Fixed Code:
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### 🔬 Tests After Fix:
```bash
pytest
```

```
4 passed ✅
```

---

## 📦 Summary

- Resolved setup and TOML issues
- Installed dependencies using `uv`
- Identified and fixed a logic bug in the `divide()` function
- All unit tests now pass
