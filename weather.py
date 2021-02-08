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
print('now speed wind ' + p + ' km/ch')
pp = str(i)
print('now humidity ' + pp + ' %')
ppp = str(x['temp'])
print('now temperature ' + ppp + '°С')
pppp =  str(x['feels_like'])
print('temperature feels like ' + pppp + '°С')
if str(k) == '{}':
    print('now not rain')
else:
    print(k)
ppppp = str(e)
print('now clouds ' + ppppp + ' %')