celsius_temperature = 31

if celsius_temperature > 30:
    print("Starting sprinklers")
    print("Starting pump")
else:
    print("Waiting...")
    print("End")

weather_condition = "ideal conditions" if 20 < celsius_temperature < 28 else "NOT"
print(weather_condition)

interior_temperature = 18
while interior_temperature < 24:
    print("Heating...")
    interior_temperature += 2

result = 1 / 3
value = 0.33
if abs(result - value) < 0.01:
    print("Works")

x = [s.upper() for s in "abcd"]
print(x)
