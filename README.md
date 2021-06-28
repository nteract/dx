# dx

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nteract/dx/main?urlpath=nteract/tree/examples)

A Pythonic Data Explorer.

## Install

For Python 3.8+:

```
pip install dx
```

## Usage

The `dx` library contains a simple helper function also called `dx`.

```python
from dx import dx
```

`dx()` takes one positional argument, a `dataframe`.

```python
dx(dataframe)
```

The `dx(dataframe)` function will display the dataframe in
[data explorer](https://github.com/nteract/data-explorer) mode:

![dx in action](https://user-images.githubusercontent.com/836375/44104304-651a2560-9fa3-11e8-9852-76db43270188.png)

Today, a Pandas `DataFrame` may be passed. In the future, other dataframe types
may be supported.

### Example

```python
import pandas as pd
from dx import dx


# Get happiness data and create a pandas dataframe
df = pd.read_csv('examples/data/2019.csv')

# Open data explorer with the happiness dataframe
dx(df)
```

## FAQ

Q: What about Spark?

A: Spark support would be highly welcome!

See [improved-spark-viz](https://github.com/nteract/improved-spark-viz) for
the current effort. There's a format that pandas handles for us that we could
create in spark land.

## Develop

```
git clone https://github.com/nteract/dx
cd dx
pip install -e .
```

We currently install jupyter and jupyter_on_nteract packages for ease of running
examples.

To run nteract on jupyter:

```
jupyter nteract
```



## Code of Conduct

We follow the nteract.io code of conduct.

## LICENSE

See [LICENSE.md](LICENSE.md).
