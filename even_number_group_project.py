#even_number_group_project.py
#Ryan L'Abbate and Antonio Singh
#Written in Atom IDE
#Covid 19 Data Visualization
#Known Bugs/Errors:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

owid = pd.read_csv("owid-covid-data.csv")

#Question 2 Test per Confirmed Case Over Time for Canada

total_canada = owid.loc[(owid['location'] == 'Canada')]
number_of_tests = total_canada['total_tests']
date = total_canada['date']
number_of_confirmed_cases = total_canada['total_cases']
tests_per_confirmed_case = number_of_tests.div(number_of_confirmed_cases)

df_confirmed_case = tests_per_confirmed_case.to_frame()
df_confirmed_case = df_confirmed_case.rename(columns = {0:'Tests Per Confirmed Case'})
df_confirmed_case['Date'] = date
df_confirmed_case['Date'] =  pd.to_datetime(df_confirmed_case['Date'], infer_datetime_format=True)

#Visualization

confirmed_case_plot = df_confirmed_case.plot(x ='Date', y='Tests Per Confirmed Case', kind = 'line', figsize=(6,6))
confirmed_case_plot.set_xlabel("Month")
confirmed_case_plot.set_ylabel("Test Per Confirmed Case")
confirmed_case_plot.set_title(" Test Per Confirmed Case Over Time for Canada")
fig_confirmed_case = confirmed_case_plot.get_figure()
fig_confirmed_case.savefig("question_2.png")

#Question 4 Rate of Recovered Cases Over Time for Canada

recoveries = pd.read_csv("time_series_covid19_recovered_global.csv")
confirmed = pd.read_csv("time_series_covid19_confirmed_global.csv")

recoveries_df = recoveries.loc[(recoveries['Country/Region'] == 'Canada')]
confirmed_df = confirmed.loc[(confirmed['Country/Region'] == 'Canada')]

cols = confirmed_df.keys()

confirmed = confirmed_df.loc[:, cols[4]:cols[-1]]
recoveries = recoveries_df.loc[:, cols[4]:cols[-1]]

dates = confirmed.keys()
dates_2 = confirmed_df.columns.tolist()
del dates_2[0:4]
recoveries_dates = pd.DataFrame(dates_2)
recoveries_dates.columns = ['Date']
recoveries_dates['Date'] =  pd.to_datetime(recoveries_dates['Date'], infer_datetime_format=True)

total_recovered = []
total_confirmed = []

for i in dates:

    recovered_sum = recoveries[i].sum()
    total_recovered.append(recovered_sum)


for i in dates:

    confirmed_sum = confirmed[i].sum()
    total_confirmed.append(confirmed_sum)

total_recovered = np.array(total_recovered).reshape(-1, 1)
total_confirmed = np.array(total_confirmed).reshape(-1, 1)
total_recovered_df = pd.DataFrame(total_recovered)
total_confirmed_df = pd.DataFrame(total_confirmed)

total_recovered_rate_df = total_recovered_df.div(total_confirmed_df)

total_recovered_rate_df.columns = ['Recovered Cases']
total_recovered_rate_df['Date'] = recoveries_dates['Date']

#Visualization

total_recovered_plot = total_recovered_rate_df.plot(x ='Date', y='Recovered Cases', kind = 'line', figsize=(8,8))
total_recovered_plot.set_xlabel("Month")
total_recovered_plot.set_ylabel("Rate of Recovered Cases")
total_recovered_plot.set_title(" Rate of Recovered Cases Over Time for Canada")
fig_recovered_case = total_recovered_plot.get_figure()
fig_recovered_case.savefig("question_4.png")

#Question 6 Mobility Vs Transmission Rate (Rt) Over Time for Country X

transmission_canada = owid.loc[(owid['location'] == 'Canada')]

transmission_rate = transmission_canada[['reproduction_rate','date']]

apple_mobility = pd.read_csv('applemobilitytrends-2020-12-10.csv', low_memory=False)

#Walking
canada_mobility_walking = apple_mobility.loc[(apple_mobility['country'] == 'Canada') & (apple_mobility['transportation_type'] == 'walking')]
cols_can_walking = canada_mobility_walking.keys()
mobility_walking = canada_mobility_walking.loc[:, cols_can_walking[6]:cols_can_walking[-1]]
dates_walking = mobility_walking.keys()
total_walking = []

for i in dates_walking:

    walking_sum = mobility_walking[i].sum()
    total_walking.append(walking_sum)

total_walking = np.array(total_walking).reshape(-1, 1)
total_walking_df = pd.DataFrame(total_walking)
total_walking_df = total_walking_df .rename(columns = {0:'Walking'})

walking_dates = canada_mobility_walking.keys()
walking_dates_2 = canada_mobility_walking.columns.tolist()
del walking_dates_2[0:6]
total_walking_dates = pd.DataFrame(walking_dates_2)
total_walking_dates.columns = ['Date']
total_walking_dates['Date'] =  pd.to_datetime(total_walking_dates['Date'], infer_datetime_format=True)

#Driving
canada_mobility_driving = apple_mobility.loc[(apple_mobility['country'] == 'Canada') & (apple_mobility['transportation_type'] == 'driving')]
cols_can_driving = canada_mobility_driving.keys()
mobility_driving = canada_mobility_driving.loc[:, cols_can_driving[6]:cols_can_driving[-1]]
dates_driving = mobility_driving.keys()
total_driving = []

for i in dates_driving:

    driving_sum = mobility_driving[i].sum()
    total_driving.append(driving_sum)

total_driving = np.array(total_driving).reshape(-1, 1)
total_driving_df = pd.DataFrame(total_driving)
total_driving_df = total_driving_df.rename(columns = {0:'Driving'})

driving_dates = canada_mobility_driving.keys()
transit_dates_2 = canada_mobility_driving.columns.tolist()
del transit_dates_2[0:6]
total_transit_dates = pd.DataFrame(transit_dates_2)
total_transit_dates.columns = ['Date']
total_transit_dates['Date'] =  pd.to_datetime(total_transit_dates['Date'], infer_datetime_format=True)

#Transit
canada_mobility_transit = apple_mobility.loc[(apple_mobility['country'] == 'Canada') & (apple_mobility['transportation_type'] == 'transit')]
cols_can_transit = canada_mobility_transit.keys()
mobility_transit = canada_mobility_transit.loc[:, cols_can_transit[6]:cols_can_transit[-1]]
dates_transit = mobility_transit.keys()
total_transit = []

for i in dates_transit:

    transit_sum = mobility_transit[i].sum()
    total_transit.append(transit_sum)

total_transit = np.array(total_transit).reshape(-1, 1)
total_transit_df = pd.DataFrame(total_transit)
total_transit_df = total_transit_df.rename(columns = {0:'Transit'})

transit_dates = canada_mobility_transit.keys()
transit_dates_2 = canada_mobility_transit.columns.tolist()
del transit_dates_2[0:6]
total_transit_dates = pd.DataFrame(transit_dates_2)
total_transit_dates.columns = ['Date']
total_transit_dates['Date'] =  pd.to_datetime(total_transit_dates['Date'], infer_datetime_format=True)

#Total
canada_mobility_total = apple_mobility.loc[(apple_mobility['country'] == 'Canada') & (apple_mobility['transportation_type'])]
cols_can_total = canada_mobility_total.keys()
mobility_total = canada_mobility_total.loc[:, cols_can_total[6]:cols_can_total[-1]]
dates_total = mobility_total.keys()
total_total = []

for i in dates_total:

    total_sum = mobility_total[i].sum()
    total_total.append(total_sum)

total_total = np.array(total_total).reshape(-1, 1)
total_total_df = pd.DataFrame(total_total)
total_total_df = total_total_df.rename(columns = {0:'Total'})

total_dates = canada_mobility_total.keys()
total_dates_2 = canada_mobility_total.columns.tolist()
del total_dates_2[0:6]
total_total_dates = pd.DataFrame(total_dates_2)
total_total_dates.columns = ['Date']
total_total_dates['Date'] =  pd.to_datetime(total_total_dates['Date'], infer_datetime_format=True)

#Transmission Rate

reproduction_rate_canada = owid.loc[(owid['location'] == 'Canada') & (owid['reproduction_rate'])]
transmission_rate_canada = reproduction_rate_canada['reproduction_rate']
transmission_rate_canada_date = reproduction_rate_canada['date']
temp = transmission_rate_canada_date.to_frame()
temp2 = transmission_rate_canada.to_frame()
temp.dropna()
temp2.dropna()
transmission_rate_df = pd.DataFrame()
transmission_rate_df['date'] = temp['date']
transmission_rate_df['reproduction_rate'] = temp2['reproduction_rate']
transmission_rate_df['date'] =  pd.to_datetime(transmission_rate_df['date'], infer_datetime_format=True)

#Visualization(s)

mobility_vs_transmission_df = pd.DataFrame()
mobility_vs_transmission_df['Walking'] = total_walking_df['Walking']
mobility_vs_transmission_df['Driving'] = total_driving_df['Driving']
mobility_vs_transmission_df['Transit'] = total_transit_df['Transit']
mobility_vs_transmission_df['Total'] = total_total_df['Total']
mobility_vs_transmission_df['Date'] = total_walking_dates['Date']
mobility_vs_transmission_df['Date'] =  pd.to_datetime(mobility_vs_transmission_df['Date'], infer_datetime_format=True)

mobility_plot = mobility_vs_transmission_df.plot(x ='Date', y=['Walking','Driving','Transit','Total'], kind='line', figsize=(8,8))
mobility_plot.set_xlabel("Month")
mobility_plot.set_ylabel("Mobility")
mobility_plot.set_title("Mobility Over Time for Canada")
mobility_plot.legend(["Walking","Driving","Transit","Total"], loc='upper left')
fig_life_mobility = mobility_plot.get_figure()
fig_life_mobility.savefig("question_6_mobility.png")

transmission_plot = transmission_rate_df.plot(x ='date', y='reproduction_rate', kind='line',logy=True, figsize=(8,8))
transmission_plot.set_xlabel("Month")
transmission_plot.set_ylabel("Transmssion Rate")
transmission_plot.set_title("Transmission Rate Over Time for Canada")
transmission_plot.legend(["Transmission Rate"], loc='upper left')
fig_transmission = transmission_plot.get_figure()
fig_transmission.savefig("question_6_transmission.png")

ax = mobility_vs_transmission_df.plot(x ='Date', y=['Walking','Driving','Transit','Total'], kind='line', logy=True,figsize=(8,8))
ax.set_title("Mobility Vs Transmission Rate (Rt) Over Time for Canada")
transmission_rate_df.plot(ax = ax, x ='date', y='reproduction_rate', kind='line', logy=True, figsize=(8,8))
ax.set_xlabel("Month")
ax.set_ylabel("Mobility / Transmssion Rate")
ax.legend(["Walking","Driving","Transit","Total", "Transmission Rate"], loc='center right')
fig_transmission_vs_mobility = ax.get_figure()
fig_transmission_vs_mobility.savefig("question_6.png")

#Question 8 HDI of All Countries Vs Their Current Transmission Rates

human_development_index_na = owid.loc[(owid['continent'] == 'North America')]
human_development_index_north_america = human_development_index_na['human_development_index']

reproduction_rate_na = owid.loc[(owid['continent'] == 'North America') & (owid['reproduction_rate'])]
reproduction_rate_north_america = reproduction_rate_na['reproduction_rate']

hdi_vs_transmission_df = pd.DataFrame()
hdi_vs_transmission_df['human_development_index'] = human_development_index_na['human_development_index']
hdi_vs_transmission_df['reproduction_rate'] = human_development_index_na['reproduction_rate']
hdi_vs_transmission_df['Date'] = human_development_index_na['date']
hdi_vs_transmission_df['Date'] =  pd.to_datetime(hdi_vs_transmission_df['Date'], infer_datetime_format=True)

#Visualization

hdi_vs_transmission_plot = hdi_vs_transmission_df.plot(x ='Date', y=['human_development_index','reproduction_rate'], style='o', logy=True, figsize=(8,8))
hdi_vs_transmission_plot.set_xlabel("Month")
hdi_vs_transmission_plot.set_ylabel("HDI / Transmission Rate")
hdi_vs_transmission_plot.set_title("HDI of All Countries (North America) Vs Their Current Transmission Rates")
hdi_vs_transmission_plot.legend(["HDI","Transmission Rate"])
fig_hdi_vs_transmission = hdi_vs_transmission_plot.get_figure()
fig_hdi_vs_transmission.savefig("question_8.png")

hdi_vs_transmission_plot = hdi_vs_transmission_df.plot(x ='human_development_index', y=['reproduction_rate'], style='o', figsize=(8,8))
hdi_vs_transmission_plot.set_xlabel("HDI")
hdi_vs_transmission_plot.set_ylabel("Transmission Rate")
hdi_vs_transmission_plot.set_title("HDI of All Countries (North America) Vs Their Current Transmission Rates")
hdi_vs_transmission_plot.legend(["Transmission Rate"])
fig_hdi_vs_transmission = hdi_vs_transmission_plot.get_figure()
fig_hdi_vs_transmission.savefig("question_8_alternate.png")

#Question 10 Life Expectancy Vs Current Death Rate of All Countries (North America)

canada_death_life = owid.loc[(owid['continent'] == 'North America')]
life_expectancy = canada_death_life['life_expectancy']
confirmed_death = canada_death_life['total_deaths']
confirmed_cases = canada_death_life['total_cases']
death_date = canada_death_life['date']
current_death_rate = confirmed_death.div(confirmed_cases)

life_expectancy_vs_death_rate_df = pd.DataFrame()
life_expectancy_vs_death_rate_df['life_expectancy'] = life_expectancy
life_expectancy_vs_death_rate_df['current_death_rate'] = current_death_rate
life_expectancy_vs_death_rate_df['Date'] = death_date
life_expectancy_vs_death_rate_df['Date'] =  pd.to_datetime(life_expectancy_vs_death_rate_df['Date'], infer_datetime_format=True)

#Visualization

life_expectancy_vs_death_rate_plot = life_expectancy_vs_death_rate_df.plot(x ='Date', y=['life_expectancy','current_death_rate'], kind='line', logy=True, figsize=(8,8))
life_expectancy_vs_death_rate_plot.set_xlabel("Month")
life_expectancy_vs_death_rate_plot.set_ylabel("Life Expectancy / Death Rate ")
life_expectancy_vs_death_rate_plot.set_title("Life Expectancy Vs Current Death Rate of All Countries (North America)")
life_expectancy_vs_death_rate_plot.legend(["Life Expectancy","Current Death Rate"], loc='center left')
fig_life_expectancy_vs_death_rate = life_expectancy_vs_death_rate_plot.get_figure()
fig_life_expectancy_vs_death_rate.savefig("question_10.png")

life_expectancy_vs_death_rate_plot = life_expectancy_vs_death_rate_df.plot(x ='life_expectancy', y=['current_death_rate'], style='o', logy=True, figsize=(8,8))
life_expectancy_vs_death_rate_plot.set_xlabel("Life Expectancy")
life_expectancy_vs_death_rate_plot.set_ylabel("Current Death Rate ")
life_expectancy_vs_death_rate_plot.set_title("Life Expectancy Vs Current Death Rate of All Countries (North America)")
#life_expectancy_vs_death_rate_plot.legend(["Life Expectancy","Current Death Rate"], loc='center left')
fig_life_expectancy_vs_death_rate = life_expectancy_vs_death_rate_plot.get_figure()
fig_life_expectancy_vs_death_rate.savefig("question_10_alternate.png")
