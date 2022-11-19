def ANOVA(df,cat,con):
    from statsmodels.formula.api import ols
    from statsmodels.stats.anova import anova_lm
    rel = con + " ~ " + cat
    model = ols(rel,df).fit()
    Q = anova_lm(model)
    pval = round(Q.iloc[0,4],4)
    return pval

def chisquare(df,cat1,cat2):
    import pandas as pd
    from scipy.stats import chi2_contingency
    a,b,c,d=chi2_contingency(pd.crosstab(df[cat1],df[cat2]))
    return b

def OUTLIERS(df):
    cat = []
    con = []
    for i in df.columns:
        if(df[i].dtypes == "object"):
            cat.append(i)
        else:
            con.append(i)
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    ss = StandardScaler()
    X1 = pd.DataFrame(ss.fit_transform(df[con]),columns=con)

    OL = []
    for i in X1.columns:
        OL.extend(list(X1[(X1[i]>3)|(X1[i]<-3)].index)) 
    from numpy import unique
    outliers = unique(OL)    
    return outliers
