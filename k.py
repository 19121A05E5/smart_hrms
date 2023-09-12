



from datetime import date, timedelta,datetime

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2023, 6, 1)
current_date = date.today()#2023-07-27
print(current_date)
end_date =current_date
for single_date in daterange(start_date, end_date):
    print(single_date)
  #  print(single_date.strftime("%d-%m-%Y"))

#k= datetime.now()
#print(k)
#print(k.strftime("%H-%M-%S"))