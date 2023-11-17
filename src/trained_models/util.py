import numpy as np


def hello(args):
    pass


def detect_outliers_zscores(column):
    thres = 3
    median = np.median(column)
    std = np.std(column)
    for i in column:
        z_score = (i-median)/std
        if (np.abs(z_score) > thres):
            self.outliers.append(i)
    return self.outliers


def detect_outliers_iqr(self, data):
    data = sorted(data)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)

    IQR = q3-q1
    lwr_bound = q1-(1.5*IQR)
    upr_bound = q3+(1.5*IQR)

    for i in data:
        if (i < lwr_bound or i > upr_bound):
            self.outliers.append(i)
    return self.outliers


def quantile_based_flooring_and_capping(column):
    """
    In this technique, the outlier is capped at a certain value above 
    the 90th percentile value or floored at a factor below the 10th 
    percentile value. Python code to delete the outlier and copy 
    the rest of the elements to another array
    """

    tenth_percentile = np.percentile(column, 10)
    ninetieth_percentile = np.percentile(column, 90)

    data = np.where(column < tenth_percentile, tenth_percentile, column)
    data = np.where(column > ninetieth_percentile,
                    ninetieth_percentile, column)
    return data


def median_imputation_outliers(column, outliers):
    median = np.median(column)
    for i in outliers:
        result = np.where(column == i, 14, column)
    return result


def detect_outliers_zcore(data):
    outliers = []
    thres = 3
    mean = np.mean(data)
    std = np.std(data)
    for i in data:
        z_score = (i-mean)/std
        if (np.abs(z_score) > thres):
            outliers.append(i)
    return outliers
