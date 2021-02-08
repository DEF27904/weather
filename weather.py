from pyowm import OWM

owm = OWM('0dcc3290fdc3262c8003f792fdeb3a0a')
mgr = owm.weather_manager()
gorod = input()
observation = mgr.weather_at_place(gorod)
w = observation.weather

h = w.detailed_status
u = w.wind()
i = w.humidity
x = w.temperature('celsius')
k = w.rain
e = w.clouds
print(h)
p = str(u['speed'])
print('cechas speed vetra ' + p + ' km/ch')
pp = str(i)
print('cechas vlajnast ' + pp + ' %')
ppp = str(x['temp'])
print('cechas timpiratura ' + ppp + '°С')
pppp =  str(x['feels_like'])
print('sechas oshushaetsa ' + pppp + '°С')
if str(k) == '{}':
    print('sechas dojda net')
else:
    print(k)
ppppp = str(e)
print('sechas oblachnast ' + ppppp + ' %')