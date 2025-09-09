# 🧮 Broken Calculator - Nova CI-Rescue Demo

> **⚠️ This repository contains intentionally broken code for demonstration purposes**

## What is this?

This is a real Python calculator module with 10 common functions - except they're all broken. It's what you might find in a legacy codebase, a junior developer's first attempt, or after a bad merge. Perfect for demonstrating how Nova CI-Rescue can automatically fix failing tests in production code.

## The Problem

You just inherited this calculator module. The previous developer left, and now you have 10 failing tests:

```bash
$ pytest test_calculator.py -v
================================= test session starts ==================================
platform darwin -- Python 3.11.5, pytest-7.4.2, pluggy-1.3.0
collected 10 items

test_calculator.py::test_addition FAILED                                         [ 10%]
test_calculator.py::test_subtraction FAILED                                      [ 20%]
test_calculator.py::test_multiplication FAILED                                   [ 30%]
test_calculator.py::test_division FAILED                                         [ 40%]
test_calculator.py::test_power FAILED                                            [ 50%]
test_calculator.py::test_modulo FAILED                                           [ 60%]
test_calculator.py::test_absolute FAILED                                         [ 70%]
test_calculator.py::test_square_root FAILED                                      [ 80%]
test_calculator.py::test_factorial FAILED                                        [ 90%]
test_calculator.py::test_max_of_two FAILED                                       [100%]

================================= 10 failed in 0.08s ===================================
```

### Here's what's broken:

- **Addition** is off by 1 (classic off-by-one error)
- **Subtraction** has the operands reversed
- **Multiplication** is doing addition instead
- **Division** is doing multiplication (copy-paste error?)
- **Power** function just multiplies (forgot to implement properly)
- **Modulo** returns the wrong value entirely
- **Absolute** value always returns negative (ironic, right?)
- **Square root** doesn't compute anything
- **Factorial** is completely unimplemented
- **Max** returns the minimum (someone was confused)

## The Traditional Fix

Normally, you'd spend the next hour:
1. Reading through each test failure
2. Debugging each function one by one
3. Running tests repeatedly
4. Possibly introducing new bugs while fixing others

## The Nova Way

```bash
# 1. Clone this mess
git clone https://github.com/seabass011/calculator-broken-demo.git
cd calculator-broken-demo

# 2. See the damage
pytest test_calculator.py -v

# 3. Install Nova CI-Rescue (one-time setup)
pip install nova-ci-rescue \
  --index-url https://dl.cloudsmith.io/9rqxsQdhFkYzaXqm/nova/nova-ci-rescue/python/simple/ \
  --extra-index-url https://pypi.org/simple/

# 4. Set your API key
export OPENAI_API_KEY='sk-...'  # Get one at platform.openai.com

# 5. Let Nova fix it
nova fix
```

## What Actually Happens

When you run `nova fix`, here's the actual output:

```
🔍 Nova CI-Rescue v0.2.3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Analyzing test failures...
Found 10 failing tests in test_calculator.py

🧠 Understanding failures:
  ✗ test_addition: Expected 5, got 6
  ✗ test_subtraction: Expected 7, got -7  
  ✗ test_multiplication: Expected 12, got 7
  ✗ test_division: Expected 5, got 20
  ✗ test_power: Expected 8, got 6
  ✗ test_modulo: Expected 1, got 3
  ✗ test_absolute: Expected 5, got -5
  ✗ test_square_root: Expected 3, got 9
  ✗ test_factorial: Expected 24, got 4
  ✗ test_max_of_two: Expected 5, got 3

🔧 Generating fixes...
  → Fixed add(): Removed extra +1
  → Fixed subtract(): Corrected operand order (a-b)
  → Fixed multiply(): Changed + to *
  → Fixed divide(): Changed * to /
  → Fixed power(): Implemented a**b
  → Fixed modulo(): Implemented a%b
  → Fixed absolute(): Removed negative sign
  → Fixed square_root(): Added sqrt calculation
  → Fixed factorial(): Implemented factorial logic
  → Fixed max_of_two(): Changed min() to max()

✅ Running tests...
All tests passing!

💾 Changes saved to calculator.py
⏱️  Total time: 12.3 seconds
```

## Verify It Worked

```bash
$ pytest test_calculator.py -v
================================= test session starts ==================================
platform darwin -- Python 3.11.5, pytest-7.4.2, pluggy-1.3.0
collected 10 items

test_calculator.py::test_addition PASSED                                         [ 10%]
test_calculator.py::test_subtraction PASSED                                      [ 20%]
test_calculator.py::test_multiplication PASSED                                   [ 30%]
test_calculator.py::test_division PASSED                                         [ 40%]
test_calculator.py::test_power PASSED                                            [ 50%]
test_calculator.py::test_modulo PASSED                                           [ 60%]
test_calculator.py::test_absolute PASSED                                         [ 70%]
test_calculator.py::test_square_root PASSED                                      [ 80%]
test_calculator.py::test_factorial PASSED                                        [ 90%]
test_calculator.py::test_max_of_two PASSED                                       [100%]

================================= 10 passed in 0.05s ===================================
```

## Real Example: What Got Fixed

Here's an actual before/after from the subtract function:

```python
# BEFORE (broken)
def subtract(a, b):
    """Subtract b from a.""" 
    # BUG: Subtracting in wrong order
    return b - a

# AFTER (fixed by Nova)
def subtract(a, b):
    """Subtract b from a.""" 
    return a - b
```

## Why This Matters

This isn't a toy example. These are real bugs that appear in production code:
- **Off-by-one errors** (our add function)
- **Copy-paste mistakes** (divide doing multiplication)
- **Incomplete implementations** (factorial)
- **Logic inversions** (max returning min)

In a real codebase with hundreds of files and thousands of tests, finding and fixing these takes hours. Nova does it in seconds.

## Try Breaking It Yourself

Want to see Nova handle your own bugs? 

1. Modify any function in `calculator.py`
2. Run `pytest` to confirm it's broken
3. Run `nova fix`
4. Watch it get fixed

## The Math

**Your team's reality:**
- Average PR has 2-3 test failures
- Each takes ~15 minutes to diagnose and fix
- You ship 20 PRs/day across your team
- That's **10 hours/day** fixing tests

**With Nova:**
- Same failures fixed in ~30 seconds each
- That's **20 minutes/day** total
- **You just got 9.5 hours back**

At $150/hour for a senior engineer, that's **$1,425/day** or **$356,250/year** saved.

## Get Started

Ready to stop fixing tests manually?

1. **Install Nova**: Use the commands above
2. **Run on your code**: `nova fix` in any project
3. **Save hours**: Let Nova handle the tedious fixes

---

*This demo is maintained by the Nova team. Questions? Reach out at support@nova-ci.com*