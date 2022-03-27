import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate 100 wind power scenarios

def get_inflow():
    filename = 'dataset/storeskar inflow.xlsx'
    historical_inflow_data = pd.read_excel(filename, skiprows=2)
    historical_inflow_data.time = pd.to_datetime(historical_inflow_data.time)
    historical_inflow_data.set_index("time", inplace=True)


    nb_days = 5
    inflow_scenarios = {}
    for day in range(1, 1+nb_days):
        one_day_wind = historical_inflow_data[(historical_inflow_data.index.month==1) & (historical_inflow__data.index.day==day)]['national']*max_wind
        for year in range(40):
            inflow_scenarios[year+1+(day-1)*40] = one_day_wind[24*year:24*(year+1)].reset_index(drop=True)

    return inflow_scenarios

    #for scen in range(1, 120, 1):
    #    wind_scenarios[scen].plot(figsize = (20,5), color = "red", label = scen)
    #plt.title("Scenarios", size = 24)
    #plt.show()


# rng = np.random.default_rng()
# values = rng.standard_normal(10)
# more_values = rng.normal(10)

# Normal distribution
# Max wind power production is 160 MW
# sc = 50
# np.random.seed(100)
# val = np.random.normal(loc=0, scale=sc, size=24)
# print(val)