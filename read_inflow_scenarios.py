import  pandas as pd
##read data from regulated inflow
# Resolution is Mm3/week
def read_inflow_scenarios():
    data = pd.read_csv('data/regulated_inflow.csv', sep=';', index_col=[0])
    data = pd.DataFrame(data)
    ## unregulate

    udata = pd.read_csv('data/unregulated_inflow.csv', sep=';', index_col=[0])
    udata = pd.DataFrame(udata)

    ## data slice
    ## regulated
    inflow = {}
    inflow['regulated'] = {}
    for year in range(51):
        inflow['regulated'][year] = {}
        for i in range(49901, 49913):
            data_1 = data[str(i)].iloc[year * 52:(year) * 52+52]## each time read 52 digit
            inflow['regulated'][year][str(i)] = data_1.reset_index(drop=True)
    ## unregulated
    inflow['unregulated'] = {}
    for year in range(51):
        inflow['unregulated'][year] = {}
        for i in range(49901, 49913):
            data_2 = udata[str(i)].iloc[year * 52:(year) * 52+52]## each time read 52 digit
            inflow['unregulated'][year][str(i)] = data_2.reset_index(drop=True)

    return inflow
