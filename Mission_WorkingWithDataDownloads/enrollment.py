import pandas

data = pandas.read_csv("/home/dq/scripts/data/CRDC2013_14.csv")
data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
#print (data.columns.tolist())

print(data["total_enrollment"].sum())

races = ["HI", "AM", "AS", "HP", "BL", "WH", "TR"]

gender = ["F", "M"]

result = ''

for i in gender:
    for j in races:
        result = result + 'data["SCH_ENR_'+ j +'_' + i + '"]+'
        
#print (result)

data["all_enrollment"]=data["SCH_ENR_HI_F"]+data["SCH_ENR_AM_F"]+data["SCH_ENR_AS_F"]+data["SCH_ENR_HP_F"]+data["SCH_ENR_BL_F"]+data["SCH_ENR_WH_F"]+data["SCH_ENR_TR_F"]+data["SCH_ENR_HI_M"]+data["SCH_ENR_AM_M"]+data["SCH_ENR_AS_M"]+data["SCH_ENR_HP_M"]+data["SCH_ENR_BL_M"]+data["SCH_ENR_WH_M"]+data["SCH_ENR_TR_M"]


print(data["TOT_ENR_M"].sum() * 100.0/data["all_enrollment"].sum())
print(data["TOT_ENR_F"].sum() * 100.0/data["all_enrollment"].sum())

for i in gender:
    for j in races:
        #print (data['SCH_ENR_'+ j +'_' + i])
        print (data['SCH_ENR_'+ j +'_' + i].sum()*100.0 / data["all_enrollment"].sum())