# Broken Calculator - Nova CI-Rescue Demo

🚨 **This calculator is intentionally broken!** 🚨

Every function in this calculator has a bug. This repository is designed to demonstrate Nova CI-Rescue's ability to automatically fix multiple failing tests.

## The Challenge

This calculator has **10 functions** and **every single one has a bug**:

- `add()` - adds an extra 1 to results
- `subtract()` - subtracts in wrong order
- `multiply()` - adds instead of multiplying
- `divide()` - multiplies instead of dividing
- `power()` - multiplies instead of exponentiation
- `modulo()` - returns divisor instead of remainder
- `absolute()` - always returns negative values
- `square_root()` - just returns the input number
- `factorial()` - just returns the input number
- `max_of_two()` - returns minimum instead of maximum

## See the Failures

Run the tests to see all the failures:

```bash
git clone https://github.com/nova/calculator-broken-demo.git
cd calculator-broken-demo
pytest test_calculator.py -v
```

You'll see **multiple test failures** across all functions.

## Watch Nova Fix Them All

Install Nova CI-Rescue and watch it fix every bug automatically:

```bash
# Install Nova CI-Rescue
pip install nova-ci-rescue --index-url https://dl.cloudsmith.io/9rqxsQdhFkYzaXqm/nova/nova-ci-rescue/python/simple/ --extra-index-url https://pypi.org/simple/

# Set your OpenAI API key
export OPENAI_API_KEY='your-key-here'

# Watch the magic happen
nova fix
```

Nova will:

1. 🔍 Analyze all failing tests
2. 🧠 Understand what each test expects vs what it gets
3. 🔧 Generate fixes for every bug
4. ✅ Verify all tests pass

## Expected Results

After Nova runs, all tests should pass and every function should work correctly!

---

_This demo repository showcases Nova CI-Rescue's ability to handle complex, multi-function bug fixes automatically._
