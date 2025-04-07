#strftime:This method is called and takes one parameter,format , to specify the format of reutuned string.
#%b ->Month name ,Short Version. ex:Dec
#%B ->Month name,Full version. Ex: December
#%m ->Month as number .ex:01-12     12
#%y ->year short version,without century.  ex:18
#%Y ->year,full Version. Ex:2018
#%H ->Hour.Ex:00-23
#%I ->Hour.Ex:00-12
#%p ->AM/pm
#%M ->Minutes. ex:00-59 
#%s ->Second
#%d-> day

##pg

import datetime as dt

n=dt.datetime.now()
# print(n)
# E=n.strftime("%H")
# print("Hour:",E)

# a=n.strftime('%M')
# print("Minutes:",a)

# st=n.strftime("%S")
# print("Second:",st)

# print(n.strftime('%b'))
# print(n.strftime('%B'))

# print(n.strftime('%y'))
# print(n.strftime('%Y'))

# print(n.strftime('%m'))

# print(n.strftime('%I'))   #12 hours format ->hour
# print(n.strftime('%p'))

# print(n.strftime("DATE:"+"%d"+":"+"%m"+":"+"%y"))
# print(n.strftime("TIME:"+"%I"+":"+"%M"+":"+"%S "+'%p'))  #Full Time Format

