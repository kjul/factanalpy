### Factanalpy

Python wrapper replicating the known factor analysis output from factanal R function. 
The only supported input is a pandas data frame. Formulas as input are currently 
not supported. A covariance matrix is always computed from the input data frame. 
Setting control variables for maximum likelihood estimation is currently not 
supported.


Further information on R's factanal function for factor analysis: https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/factanal

More information on the factanal output and examples: 
https://data.library.virginia.edu/getting-started-with-factor-analysis/


#### Installation

```pip install factanal```

#### Dependencies
The only dependency is the rpy2 library. 

```pip install rpy2```

In addition to that, R must be installed on your system and accessible to rpy2.

More information on rpy2: https://rpy2.github.io/doc/latest/html/index.html

Download R here: https://www.r-project.org/

#### Misc
Factanal for python is MIT licensed.


