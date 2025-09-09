# 🧮 Broken Calculator - Nova CI-Rescue Demo

<div align="center">
  <img src="https://img.shields.io/badge/bugs-10-red?style=for-the-badge" alt="10 Bugs">
  <img src="https://img.shields.io/badge/tests-failing-red?style=for-the-badge" alt="Failing Tests">
  <img src="https://img.shields.io/badge/nova-fixable-green?style=for-the-badge" alt="Nova Fixable">
</div>

<div align="center">
  <h3>🚨 This calculator is intentionally broken! 🚨</h3>
  <p><i>Perfect for demonstrating Nova CI-Rescue's auto-fix capabilities</i></p>
</div>

---

## 🎯 The Challenge

This repository contains a Python calculator with **10 functions**, and **every single one has a bug**. It's designed to showcase Nova CI-Rescue's ability to automatically detect, understand, and fix multiple failing tests across an entire codebase.

### 🐛 The Bugs

| Function | Expected Behavior | Actual Behavior (Bug) | Example |
|----------|------------------|----------------------|---------|
| `add()` | Adds two numbers | Adds extra 1 to result | `add(2, 3)` returns `6` instead of `5` |
| `subtract()` | Subtracts b from a | Subtracts in wrong order | `subtract(10, 3)` returns `-7` instead of `7` |
| `multiply()` | Multiplies two numbers | Adds instead | `multiply(3, 4)` returns `7` instead of `12` |
| `divide()` | Divides a by b | Multiplies instead | `divide(10, 2)` returns `20` instead of `5` |
| `power()` | Raises a to power b | Just multiplies | `power(2, 3)` returns `6` instead of `8` |
| `modulo()` | Returns remainder | Returns divisor | `modulo(10, 3)` returns `3` instead of `1` |
| `absolute()` | Returns absolute value | Always negative | `absolute(5)` returns `-5` instead of `5` |
| `square_root()` | Returns square root | Returns input | `square_root(9)` returns `9` instead of `3` |
| `factorial()` | Calculates factorial | Returns input | `factorial(4)` returns `4` instead of `24` |
| `max_of_two()` | Returns maximum | Returns minimum | `max_of_two(5, 3)` returns `3` instead of `5` |

## 🚀 Quick Start Demo

### 1️⃣ Clone and See the Failures

```bash
# Clone this broken calculator
git clone https://github.com/seabass011/calculator-broken-demo.git
cd calculator-broken-demo

# Install pytest if needed
pip install pytest

# Run tests - watch them all fail! 
pytest test_calculator.py -v
```

You'll see output like:
```
FAILED test_calculator.py::test_addition - assert 6 == 5
FAILED test_calculator.py::test_subtraction - assert -7 == 7
FAILED test_calculator.py::test_multiplication - assert 7 == 12
... and more failures
```

### 2️⃣ Install Nova CI-Rescue

```bash
# Install from Cloudsmith private registry
pip install nova-ci-rescue \
  --index-url https://dl.cloudsmith.io/9rqxsQdhFkYzaXqm/nova/nova-ci-rescue/python/simple/ \
  --extra-index-url https://pypi.org/simple/

# Set your OpenAI API key
export OPENAI_API_KEY='your-api-key-here'
```

### 3️⃣ Watch the Magic ✨

```bash
# Let Nova fix everything automatically
nova fix
```

Nova will:
- 🔍 **Analyze** all failing tests
- 🧠 **Understand** what each test expects vs what it gets  
- 🔧 **Generate** minimal fixes for every bug
- ✅ **Verify** all tests pass

### 4️⃣ Verify Success

```bash
# All tests should now pass!
pytest test_calculator.py -v
```

## 📊 What Nova Does

Nova creates minimal, targeted fixes. For example:

```python
# Before (buggy):
def add(a, b):
    return a + b + 1  # Bug: adds extra 1

# After (fixed by Nova):
def add(a, b):
    return a + b      # Fixed: correct addition
```

## 🎥 Demo Script

For a presentation-ready demo, you can use this flow:

```bash
# Show the broken state
echo "📍 Current state: 10 broken functions"
pytest test_calculator.py -q

# Run Nova
echo "🤖 Running Nova CI-Rescue..."
nova fix

# Show the fixed state
echo "✅ After Nova: All tests passing!"
pytest test_calculator.py -q
```

## 🤔 Why This Matters

- **Real-world scenario**: Bugs across multiple functions
- **Complex fixes**: Not just simple typos, but logic errors
- **Automatic resolution**: No manual intervention needed
- **Time saved**: Minutes instead of hours of debugging

## 📈 ROI Calculator

If your team encounters:
- 10 failing tests per day
- 15 minutes to fix each manually
- 250 working days per year

**That's 625 hours/year saved with Nova CI-Rescue!**

## 🔗 Learn More

- **Nova CI-Rescue**: [GitHub Repository](https://github.com/joinnova-ci/nova-ci-rescue)
- **Documentation**: Coming soon
- **Support**: support@nova-ci.com

---

<div align="center">
  <p><b>Built with ❤️ to showcase Nova CI-Rescue</b></p>
  <p><i>Software fixing software - automatically</i></p>
</div>