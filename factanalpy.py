import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri


def factanalpy(x, factors, score="none", rotation="varimax", verbose=True, return_dict=False):
    """
    Python wrapper replicating the known factor analysis output from factanal R package .
    
    Args:
        x (pandas data frame): Data frame containing the data set to be analyzed.
        score (str): R package fractanal score parameter.
        rotation (str): R package fractanal rotation parameter.
        verbose (boolean): If set to True, factanal stlye output is printed.
        return_dict (boolean): If set to True, dictionary containing the factanal output is returned.
        
    Returns:
        dict: dictionary containing the factanal output is returned.
    """
    pandas2ri.activate()
    factanal = robjects.r['factanal']
    fit = factanal(x, factors=factors, score=score, rotation=rotation)
    fit_python_dict = {name: list(fit[index]) for name, index in zip(fit.names, range(0, len(fit)))}
    if verbose:
        print("Uniquenesses:", str(fit[-1]).split("Uniquenesses:")[1])
    if return_dict:
        return fit_python_dict
