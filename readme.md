### Factanal

Python wrapper replicating the known factor analysis output from the factanal R function. 
The only supported input is a pandas data frame. Formulas as input are currently 
not supported. A covariance matrix is always computed from the input data frame. 
Setting control variables for maximum likelihood estimation is currently not 
supported.


Further information on R's factanal function for factor analysis: https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/factanal

More information on the factanal output and examples: 
https://data.library.virginia.edu/getting-started-with-factor-analysis/

#### Installation

```pip install factanal```

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

Uniquenesses: 
   v1    v2    v3    v4    v5    v6    v7    v8 
0.861 0.005 0.666 0.005 0.611 0.223 0.812 0.885 

Loadings:
   Factor1 Factor2 Factor3 Factor4
v1 -0.136                   0.326 
v2  0.983           0.169   0.104 
v3          0.128           0.575 
v4          0.999                 
v5 -0.114           0.199  -0.553 
v6 -0.204          -0.825   0.197 
v7 -0.264           0.317         
v8                  0.313   0.106 

               Factor1 Factor2 Factor3 Factor4
SS loadings      1.127   1.048   0.953   0.807
Proportion Var   0.141   0.131   0.119   0.101
Cumulative Var   0.141   0.272   0.391   0.492

Factor Correlations:
        Factor1 Factor2 Factor3 Factor4
Factor1  1.0000  0.0380 -0.0526  0.1918
Factor2  0.0380  1.0000  0.0675 -0.0599
Factor3 -0.0526  0.0675  1.0000 -0.0671
Factor4  0.1918 -0.0599 -0.0671  1.0000

Test of the hypothesis that 4 factors are sufficient.
The chi square statistic is 0.37 on 2 degrees of freedom.
The p-value is 0.833 
```

#### Dependencies
The only dependency is the rpy2 library. R must be installed on your system and accessible to rpy2.

More information on rpy2: https://rpy2.github.io/doc/latest/html/index.html

Download R here: https://www.r-project.org/

#### Misc
Factanal for python is MIT licensed.



