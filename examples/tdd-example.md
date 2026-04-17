# TDD Example

## Scenario

Nanobot needs to implement a `retry` function that retries a failed operation up to 3 times.

## How Nanobot Should Respond (with TDD skill active)

---

**Let's build this test-first.**

**Step 1: Write the failing test**

```python
def test_retries_failed_operations_3_times():
    """Should retry up to 3 times before giving up."""
    attempts = 0
    
    def failing_operation():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ConnectionError("Network error")
        return "success"
    
    result = retry(failing_operation, max_retries=3)
    
    assert result == "success"
    assert attempts == 3
```

**Step 2: Run to verify it fails**
```
$ pytest test_retry.py -v
E: NameError: name 'retry' is not defined
```

**Step 3: Write minimal implementation**

```python
def retry(fn, max_retries=3):
    last_error = None
    for i in range(max_retries):
        try:
            return fn()
        except Exception as e:
            last_error = e
    raise last_error
```

**Step 4: Run to verify it passes**
```
$ pytest test_retry.py -v
✓ test_retries_failed_operations_3_times PASSED
```

**Step 5: Refactor** (if needed)

---

This is the red-green-refactor cycle. Want me to continue with edge case tests?