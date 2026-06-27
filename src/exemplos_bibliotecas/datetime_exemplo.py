from datetime import datetime 
data = datetime.now()
print("horas", data.hour,":",data.minute,":",data.second)
print("data", data.day,"/", data.month,"/",data.year) 
if data.hour >= 6 and data.hour <= 18:
    print("bom dia")
else:
    print("boa noite")