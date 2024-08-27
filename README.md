## Description

This is a minimal proof-of-concept exploring how import hooks might be used to execute custom logic upon import and to see whether it is feasible to disallow certain callers from importing successfully.

## Usage

```bash
# this should import fine
python -m src.module_a

# this should throw an ImportError
python -m src.module_c
```

## Additional reading

*   [firewalling your code](https://lackofimagination.org/2024/08/firewalling-your-code/)
*   [in-depth learning of the python import mechanism](https://www.sobyte.net/post/2021-10/python-import/)
