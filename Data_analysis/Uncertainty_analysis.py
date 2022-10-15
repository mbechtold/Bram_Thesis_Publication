# Import packages
from thesis_pub_tools import *
from scipy import optimize
from scipy import stats
import sklearn.preprocessing
import sklearn.linear_model as lm
import statsmodels.api as sm
import datetime
from patsy import dmatrices
import matplotlib.colors as clr
from matplotlib.pyplot import cm

# ----------------------------------------------------------------------------------------------------------------------
# Settings
# ----------------------------------------------------------------------------------------------------------------------
# Main settings
peat_min = 0.50
area = 'Obi_River'
SIF_PAR = True
Time_2021 = True
SP_res = 0.2
p = 0.05
# ----------------------------
corr = '_c30_pt' + str(round(peat_min * 100)) + '_SPres' + str(round(SP_res*10)) + '_pValue' + str(int(round(p*100)))

# ----------------------------------------------------------------------------------------------------------------------
# Import data
# ----------------------------------------------------------------------------------------------------------------------
if area == 'Alaska':
    lat_lim = [61, 65]
    lon_lim = [-161, -142]
    int_lon = 5
    int_lat = 1
    figsize = (6, 2)
    title = 'Alaska'
    res = 'l'
elif area == 'Boreal_Plains':
    lat_lim = [57, 60]
    lon_lim = [-125, -112]
    int_lon = 5
    int_lat = 1
    figsize = (6, 2)
    title = 'Boreal Plains'
    res = 'l'
elif area == 'Hudson_Bay':
    lat_lim = [51, 55]
    lon_lim = [-97, -80]
    int_lon = 5
    int_lat = 1
    figsize = (6, 2)
    title = 'Hudson Bay'
    res = 'l'
elif area == 'Obi_River':
    lat_lim = [58, 62]
    lon_lim = [67, 78]
    int_lon = 2
    int_lat = 1
    figsize = (6, 3)
    title = 'Obi River'
    res = 'l'
elif area == 'NH':
    # lat_lim = [51, 53]
    # lon_lim = [-86, -84]
    lat_lim = [63, 64]
    lon_lim = [-117, -115]
    int_lon = 20
    int_lat = 5
    figsize = (10, 1.65)
    title = ''
    res = 'c'
if SIF_PAR:
    SIF_variable = 'sif_norm'
    corr = corr + '_SIFnorm'
else:
    SIF_variable = 'sif_dc'
    corr = corr + '_SIF'
if Time_2021 and SP_res == 0.05:
    lon, lat, time = data_analysis_dimension(SIF2021_file5, lat_lim=lat_lim, lon_lim=lon_lim)
    SIFnorm = data_analysis_variable(SIF2021_file5, SIF_variable, peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    WTD = data_analysis_variable(WTD2021_file5, 'WTD', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    OW = data_analysis_variable(OW2021_file5, 'OW', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    i_unit = ' (m$^{-3}$sr$^{-1}\mu$m$^{-1}$)'
    corr = corr + '_2021'
    nYears = 4
elif Time_2021 and SP_res == 0.2:
    lon, lat, time = data_analysis_dimension(SIF2021_file2, lat_lim=lat_lim, lon_lim=lon_lim)
    SIFnorm = data_analysis_variable(SIF2021_file2, SIF_variable, peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    WTD = data_analysis_variable(WTD2021_file2, 'WTD', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    WTD_10y = data_analysis_variable(WTD10y_file2, 'WTD', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    OW = data_analysis_variable(OW2021_file2, 'OW', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res,
                                Time_2021=Time_2021)
    i_unit = ' (m$^{-3}$sr$^{-1}\mu$m$^{-1}$)'
    corr = corr + '_2021'
    nYears = 4
elif not Time_2021 and SP_res == 0.05:
    lon, lat, time = data_analysis_dimension(SIF_file5, lat_lim=lat_lim, lon_lim=lon_lim)
    SIFnorm = data_analysis_variable(SIF_file5, SIF_variable, peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    WTD = data_analysis_variable(WTD_file5, 'WTD', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    PAR = data_analysis_variable(PAR_file5, 'PAR_avg', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    # OW = data_analysis_variable(OW2021_file5, 'OW', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res,
    #                            Time_2021=Time_2021)
    nYears = 3
else:
    lon, lat, time = data_analysis_dimension(SIF_file2, lat_lim=lat_lim, lon_lim=lon_lim)
    SIFnorm = data_analysis_variable(SIF_file2, SIF_variable, peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    WTD = data_analysis_variable(WTD_file2, 'WTD', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    PAR = data_analysis_variable(PAR_file2, 'PAR_avg', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    WTD_10y = data_analysis_variable(WTD10y_file2, 'WTD', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res, Time_2021=Time_2021)
    # OW = data_analysis_variable(OW2021_file5, 'OW', peat_min=peat_min, lat_lim=lat_lim, lon_lim=lon_lim, SP_res=SP_res,
    #                            Time_2021=Time_2021)
    nYears = 3

SIF_sAnom, WTD_sAnom = short_anom(lat, lon, time, SIFnorm, WTD)
SIF_lAnom, WTD_lAnom = long_anom(lat, lon, time, SIFnorm, WTD)
# SIF_seas = seasonality(lat, lon, time, SIFnorm)
# WTD_seas = seasonality(lat, lon, time, WTD)
# SIF_clim = lt_climatology(lat, lon, time, SIFnorm)
# WTD_clim = lt_climatology(lat, lon, time, WTD)


def func(WTDanom, WTD, a, b):
    return a * WTDanom + b * WTDanom * WTD


"""
WTD_opt = np.zeros((len(lat), len(lon)))
for ilat in range(len(lat)):
    for ilon in range(len(lon)):
        SIF_sAnom_pix = SIF_sAnom[ilat, ilon, :]
        WTD_sAnom_pix = WTD_sAnom[ilat, ilon, :]
        WTD_pix = WTD[ilat, ilon, :]
        WTD_opt[ilat, ilon] = cal_WaterStressModel(SIF_sAnom_pix, WTD_sAnom_pix, WTD_pix, p, time)[1]
"""

# Bootstrap analysis
WTDopt_mean = np.zeros((len(lat), len(lon)))
WTD_CI_5 = np.zeros((len(lat), len(lon)))
WTD_CI_95 = np.zeros((len(lat), len(lon)))
for ilat in range(len(lat)):
    print(str(ilat))
    for ilon in range(len(lon)):
        if not np.isnan(WTD).all() and not np.isnan(SIF_sAnom).all() and not np.isnan(WTD_sAnom).all():
            WTDopt_mean_pix, WTD_CI_5_pix, WTD_CI_95_pix = Bootstrap_uncertainty(SIF_sAnom[ilat, ilon, :], WTD_sAnom[ilat, ilon, :], WTD[ilat, ilon, :], 10, p, time)
            WTDopt_mean[ilat, ilon] = WTDopt_mean_pix
            WTD_CI_5[ilat, ilon] = WTD_CI_5_pix
            WTD_CI_95[ilat, ilon] = WTD_CI_95_pix
        else:
            WTDopt_mean[ilat, ilon] = np.nan
            WTD_CI_5[ilat, ilon] = np.nan
            WTD_CI_95[ilat, ilon] = np.nan

WTD_CI_5_mean = np.nanmean(WTD_CI_5)
WTD_CI_95_mean = np.nanmean(WTD_CI_95)
