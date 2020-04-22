import pandas as pd
from rpy2.robjects.conversion import localconverter
from rpy2.robjects import default_converter
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri


def factanalpy(x, factors, score="none", rotation="varimax", verbose=True, return_dict=False):
    """
    Factor analysis based on factanal R package replicating the known output.
    
    Args:
        X (pandas data frame): Data frame containing the data set to be analyzed.
        score (str): R package fractanal score parameter.
        rotation (str): R package fractanal rotation parameter.
        verbose (boolean): If set to True, factanal stlye output is printed.
        return_dict (boolean): If set to True, dictionary containing the factanal output is returned.
        
    Returns:
        dict: dictionary containing the factanal output is returned.
    """
    with localconverter(default_converter + pandas2ri.converter) as cv:
        r_data_set = pandas2ri.py2ri(x)
    factanal = robjects.r['factanal']
    fit = factanal(r_data_set, factors=factors, score=score, rotation=rotation)
    fit_python_dict = {name: list(fit[index]) for name, index in zip(fit.names, range(0, len(fit)))}
    
    if verbose:
        _print_factanal_output(fit=fit_python_dict, features=list(x.columns), factors=factors)
    if return_dict:
        return fit_python_dict


def _print_factanal_output(fit, features, factors):
    """
    Replicates the known factanal R package output.
    
    Args:
        fit (rpy2.robjects.vectors.ListVector): ListVector
        features (list): feature names as strings in a list
        factors (int): number of factors
        
    Returns:
        -
    """
    loadings = fit["loadings"].copy()
    uniquenessess = fit["uniquenesses"].copy()
    dof = int(fit["dof"][0])
    pval = fit["criteria"][0]
    
    factor_names = [f"Factor{number}" for number in range(1, factors+1)]
    
    uniquenessess_dict = {}
    for i in features:
        uniquenessess_dict[i] = [uniquenessess.pop(0)]
    uniquenessess_df = pd.DataFrame(uniquenessess_dict, index=["uniqueness"])
    
    loadings_dict = {factor_name: [] for factor_name in factor_names}
    
    for i in range(factors):
        for _ in range(len(features)):
            loadings_dict["Factor"+str(i+1)] = loadings_dict["Factor"+str(i+1)] + [loadings.pop(0)]
    loadings_dict["feature"] = features
    
    loading_metrics_df = pd.DataFrame(loadings_dict)
    loading_metrics_df = loading_metrics_df.drop("feature", axis=1)
    loadings_sq_df = loading_metrics_df ** 2
    loadings_sq_sum = dict(loadings_sq_df.sum())
    for i in loadings_sq_sum:
        loadings_sq_sum[i] = [loadings_sq_sum[i]] 
    loading_metrics_df = pd.DataFrame(loadings_sq_sum, index=["SS loadings"])
    proportion_var_df = loading_metrics_df / len(features)
    proportion_var_df = proportion_var_df.rename({"SS loadings": "Proportion Var"})
    loading_metrics_df = loading_metrics_df.append(proportion_var_df)
    proportion_var = list(loading_metrics_df.loc["Proportion Var",:])
    cum_var = []
    cum_var.append(proportion_var.pop(0))
    while len(proportion_var) != 0:
        cum_var.append(cum_var[-1] + proportion_var.pop(0))
    loading_metrics_df = loading_metrics_df.append(pd.DataFrame({j: cum_var[i] for i, j in zip(range(len(factor_names)), factor_names)}, index=["Cumulative Var"]))
    
    print("Call:")
    print(f"factanal(x, factors = {factors})")
    print()
    print("Uniquenesses:")
    print(round(uniquenessess_df, 3).to_string(index=False))
    print()
    print("Loadings:")
    print(round(pd.DataFrame(loadings_dict).set_index('feature'), 3))
    print()
    print(round(loading_metrics_df, 3))
    print()
    print(f"THIS PART IS WIP: The degrees of freedom for the model is {dof} and the fit was {round(pval, 4)}")
