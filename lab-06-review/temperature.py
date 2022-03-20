temperatureInCelsius = input("Please enter a temperature in Cesius");
temperatureInCelsius = float(temperatureInCelsius);
print(type(temperatureInCelsius));

temperatureinFahereinheit = temperatureInCelsius * 1.8 + 32;
# using round method to limit decimal places
temperatureinFahereinheit = round(temperatureinFahereinheit, 2);
print(str(temperatureInCelsius)+ " degree celsius is "+str(temperatureinFahereinheit)+ " degrees Fahrenheit")