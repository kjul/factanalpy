import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri


def factanal(x, factors, scores="none", rotation="varimax", verbose=True, return_dict=False):
    """
    Python wrapper replicating the known factor analysis output from factanal R function. The only supported input for x
    is a pandas data frame. Formulas in x are currently not supported. covmat is always computed from x. Setting control
    variables for maximum likelihood estimation is currently not supported.
    Further information: https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/factanal

    Args:
        x (DataFrame): Data frame containing the data set to be analyzed.
        factors (int): R package factanal factors parameter.
        scores (str): R package factanal score parameter.
        rotation (str): R package factanal rotation parameter.
        verbose (boolean): If set to True, factanal stlye output is printed.
        return_dict (boolean): If set to True, dictionary containing the factanal output is returned.
        
    Returns:
        dict: if return_dict is set to True a dictionary containing the factanal output is returned.
    """
    pandas2ri.activate()
    fit = robjects.r['factanal'](x, factors=factors, scores=scores, rotation=rotation)
    if verbose:
        print("Uniquenesses:", str(fit[-1]).split("Uniquenesses:")[1])
    if return_dict:
        return {name: list(fit[index]) for name, index in zip(fit.names, range(len(fit)))}
