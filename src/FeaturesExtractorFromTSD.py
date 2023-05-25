import numpy as np
from scipy import stats
from scipy.signal import find_peaks
from scipy.fft import fft

def create_feature_dict_from_tsd(time_series):
    # idea fir feature mapping is taken
    # from table 2 from https://link.springer.com/article/10.1007/s12559-020-09768-8
    time_series = np.array(time_series)
    mean  = np.mean(time_series)
    var = np.var(time_series)
    # Compute the median absolute deviation of the data along the given axis.
    mad = stats.median_abs_deviation(time_series)
    ma = max(time_series)
    mi = min(time_series)
    #defined as the sum of absolute values of the three axis averaged over a window
    sma =  np.sum(abs(time_series))/len(time_series)
    #Energy of a signal in every axis is computed by taking the mean of sum of squares of the values in a window in that particular axis.
    energy = np.sum(time_series**2)/len(time_series)
    iqr = np.percentile(time_series, 75) - np.percentile(time_series, 25)
    entropy = stats.entropy(time_series)
    correlation = np.corrcoef(time_series)
    kurtosis = stats.kurtosis(time_series)
    skewness = stats.skew(time_series)

    # analyse the time_series data in frequency domain. Idea from https://datascience.stackexchange.com/questions/20339/frequency-for-a-time-series
    fft_time_series = fft(time_series)
    maxFreqCompInd = np.argmax(np.abs(fft_time_series))
    maxFreqComp = fft_time_series[maxFreqCompInd]
    meanFreq = np.mean(fft_time_series)
    skewnessFreq = stats.skew(fft_time_series)
    kurtosisFreq = stats.kurtosis(fft_time_series)
    # Calculate the amplitude spectrum
    ampSprec = np.abs(fft_time_series)
    # Calculate the phase angle
    angle = np.angle(fft_time_series)
    median = np.median(time_series)
    peak_count = len(find_peaks(time_series)[0])

    return {"mean": mean,
            "var": var,
            "mad":mad,
            "max":ma,
            "min":mi,
            "sma":sma,
            "energy":energy,
            "iqr":iqr,
            "entropy":entropy,
            "correlation":correlation,
            "kurtosis":kurtosis,
            "skewness":skewness,
            "maxFreqCompInd":maxFreqCompInd,
            "maxFreqComp":maxFreqComp,
            "meanFreq":meanFreq,
            "skewnessFreq":skewnessFreq,
            "kurtosisFreq":kurtosisFreq,
            #"ampSprec":ampSprec, # TODO: the both values are array of values
            #"angle":angle,
            "median":median,
            "peak_count":peak_count,
    }