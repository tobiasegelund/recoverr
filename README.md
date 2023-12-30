# recoverr

To handle recoverable errors in Python. Take advantage of a wrapper to store the outcome of functions to better control the flow of outputs.

The library is heavily inspired by the Result enum from Rust. The name of the library is a contraction of'recover' and 'error'.

## Install

```bash
pip install recoverr
```

## Usage

```python
from recoverr import Ok, Err

res1 = Ok(2) # Result<2, None>
```
