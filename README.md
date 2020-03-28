<p align="center">
  <a href="https://github.com/skmatz/optan">
    <img src="./assets/images/banner.png" width="500" alt="banner" />
  </a>
</p>

<p align="center">Researcher Friendly Argument Parser for Python</p>

<p align="center">
  <a href="./LICENSE">
    <img
      src="https://img.shields.io/github/license/skmatz/optan"
      alt="license"
    />
  </a>
  <a href="https://github.com/skmatz/optan/releases/latest">
    <img
      src="https://img.shields.io/github/v/release/skmatz/optan"
      alt="release"
    />
  </a>
</p>

## Install

```sh
pip install git+https://github.com/skmatz/optan.git
```

## Example

Basic usage is the same as `argparse.ArgumentParser`.

```python
from optan import Optan

optan = Optan()

optan.add_argument("--aaa")
optan.add_argument("--bbb", type=int)
optan.add_argument("--ccc", action="store_true")

args = optan.parse_args()

optan.add_param("acc", 0.7)
optan.add_params({"tp": 3, "fp": 1, "tn": 4, "fn": 2})

optan.write("optan.csv")
```

You run `python example.py --aaa abc --bbb 123 --ccc` and get:

```csv
#,datetime,aaa,bbb,ccc,acc,tp,fp,tn,fn
1,20200101000000,abc,123,True,0.7,3,1,4,2
```
