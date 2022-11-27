# Import packages
from thesis_pub_tools import *
import datetime

# ----------------------------------------------------------------------------------------------------------------------
# Settings
# ----------------------------------------------------------------------------------------------------------------------
# Main settings
peat_min = 0.50
area = 'NH'
SIF_PAR = True
Time_2021 = True
SP_res = 0.2
p = 1
output_file = '/data/leuven/336/vsc33653/OUTPUT_pub/uncertainty_WTDopt.txt'
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
    lat_lim = []
    lon_lim = []
    int_lon = 20
    int_lat = 5
    figsize = (10, 1.65)
    title = ''
    res = 'c'
elif area == 'test':
    lat_lim = [51, 53]
    lon_lim = [-86, -84]
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

# stats.bootstrap((SIF_sAnom[0, 0, :], WTD_sAnom[0, 0, :], WTD[0, 0, :], time,), cal_WaterStressModel)

# Bootstrap analysis
nRuns = 100
WTDopt_s_mean = np.zeros((len(lat), len(lon)))
WTDopt_s_CI5 = np.zeros((len(lat), len(lon)))
WTDopt_s_CI95 = np.zeros((len(lat), len(lon)))
for ilat in range(len(lat)):
    print('Short term bootstrap analysis: ' + str(round((ilat / len(lat)) * 100, 2)) + '%')
    for ilon in range(len(lon)):
        if not np.isnan(WTD).all() and not np.isnan(SIF_sAnom).all() and not np.isnan(WTD_sAnom).all():
            random_data = np.zeros((len(time), 3, nRuns))
            time_rand = np.random.choice(SIF_sAnom.shape[0], (SIF_sAnom.size, nRuns), replace=True)
            random_data[:, 0, :] = SIF_sAnom[time_rand]
            random_data[:, 1, :] = WTD_sAnom[time_rand]
            random_data[:, 2, :] = WTD[time_rand]
            WTDopt_pixel = np.zeros((nRuns))
            for i in range(0, nRuns):
                WTDopt_pixel[i] = cal_WaterStressModel(random_data[:, 0, i], random_data[:, 1, i], random_data[:, 2, i], 1, time)[1]
                WTDopt_s_mean[ilat, ilon] = np.nanmean(WTDopt_pixel)
                WTDopt_s_CI5[ilat, ilon] = np.nanquantile(WTDopt_pixel, 0.05)
                WTDopt_s_CI95[ilat, ilon] = np.nanquantile(WTDopt_pixel, 0.95)
        else:
            WTDopt_s_mean[ilat, ilon] = np.nan
            WTDopt_s_CI5[ilat, ilon] = np.nan
            WTDopt_s_CI95[ilat, ilon] = np.nan

WTD_CI_5_mean_s = np.nanmean(WTDopt_s_CI5)
WTD_CI_95_mean_s = np.nanmean(WTDopt_s_CI95)
WTDopt_mean_s = np.nanmean(WTDopt_s_mean)

with open(output_file, 'a') as f:
    f.write('--------------------------------------------------------------------------------------\n')
    f.write('Uncertainty WTDopt                  Date:'+str(datetime.datetime.today())+'\n')
    f.write('--------------------------------------------------------------------------------------\n')
    f.write('Settings:\n')
    f.write('   peat mask: ' + str(peat_min) + '\n')
    f.write('   area: '+str(area)+'\n')
    f.write('   p: '+str(p)+'\n')
    f.write('   Normalized by PAR?: '+str(SIF_PAR)+'\n')
    f.write('   2021 included?: '+str(Time_2021)+'\n')
    f.write('   Spatial resolution: '+str(SP_res)+'\n')
    f.write('Short term analysis:\n')
    f.write('   Upper limit: '+str(WTD_CI_95_mean_s)+'\n')
    f.write('   WTDopt: ' + str(WTDopt_mean_s) + '\n')
    f.write('   Lower limit: ' + str(WTD_CI_5_mean_s) + '\n\n')
    f.write('-------------------------------------------------------------\n')
    f.write('------------------------------------------------------------------------------------\n\n')
