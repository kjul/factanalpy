### Factanal

Python wrapper replicating the known factor analysis output from the factanal R function. 
The only supported input is a pandas data frame. Formulas as input are currently 
not supported. A covariance matrix is always computed from the input data frame. 
Setting control variables for maximum likelihood estimation is currently not 
supported.


Further information on R's factanal function for factor analysis: https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/factanal

More information on the factanal output and examples: 
https://data.library.virginia.edu/getting-started-with-factor-analysis/


#### Example

```
import pandas as pd
import random
from factanal.wrapper import factanal

pdf = pd.DataFrame({"v1": [random.randint(0, 100) for _ in range (30)],
                    "v2": [random.randint(0, 100) for _ in range (30)],
                    "v3": [random.randint(0, 100) for _ in range (30)],
                    "v4": [random.randint(0, 100) for _ in range (30)],
                    "v5": [random.randint(0, 100) for _ in range (30)],
                    "v6": [random.randint(0, 100) for _ in range (30)],
                    "v7": [random.randint(0, 100) for _ in range (30)],
                    "v8": [random.randint(0, 100) for _ in range (30)]})

fa_res = factanal(pdf, factors=4, scores='regression', rotation='promax', 
                  verbose=True, return_dict=True)

pd.DataFrame(fa_res["scores"])
```


#### Installation

```pip install factanal```

#### Dependencies
The only dependency is the rpy2 library. R must be installed on your system and accessible to rpy2.

More information on rpy2: https://rpy2.github.io/doc/latest/html/index.html

Download R here: https://www.r-project.org/

#### Misc
Factanal for python is MIT licensed.



