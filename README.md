# Data Explorer

## Install

```
pip install dx
```

## Usage

`dx` contains a simple helper called `dx`

```python
from dx import dx
```

It takes one positional argument for a Pandas `DataFrame`:

```python
dx(dataframe)
```

Which will display the dataframe in data explorer mode:

![dx in action](https://user-images.githubusercontent.com/836375/44104304-651a2560-9fa3-11e8-9852-76db43270188.png)


## FAQ

Q: What about Spark?

A: Spark support would be highly welcome! See [improved-spark-viz](https://github.com/nteract/improved-spark-viz) for the current effort. There's a format
that pandas handles for us that we could create in spark land. 


## Develop

```
git clone https://github.com/nteract/dx
cd dx
pip install -e .
```
