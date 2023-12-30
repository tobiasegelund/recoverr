# recoverr

To handle recoverable errors in Python, take advantage of a wrapper that stores the outcome of functions to better control the flow of outputs.

The library is heavily inspired by the Result enum from Rust. Its name is a contraction of'recover' and 'error'.

It's important to highlight that the library is completely self-contained, devoid of any dependencies, ensuring its status as a pristine Python module.

## Install

```bash
pip install recoverr
```

## Usage

```python
from recoverr import Ok, Err

res1 = Ok(2) # Result<2, None>
```
