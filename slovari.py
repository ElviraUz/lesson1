weather = {
    "city": "Москва",
    "temperature": 20
}
print(weather ["city"])

weather["temperature"]=15
print(weather)
print(weather.get("country"))
weather.get("country","Россия")
print(weather)
weather["date"]="27.05.2019"
print(weather)
print(len(weather))