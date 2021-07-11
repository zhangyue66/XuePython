locations = {'North America': {'USA': ['Mountain View']}}

locations['Asia'] = {'India':['Bangalore']}

USC_list = locations['North America']
USC_list['USA'].append('Atlanta')

locations['Africa'] = {'Egypt':['Cairo']}

AsiaC_list = locations["Asia"]

AsiaC_list['China'] = ['Shanghai']
locations['Asia']['China'] .append('Shenzhen')
#print (locations)
#print(US_list)
#print(locations.keys())
'''
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
'''

print(1)
y = USC_list['USA']
y = sorted(y)
print(y[0])
print(y[1])
#print(sorted(USC_list['USA']))

print(2)
x=AsiaC_list['India']
x= sorted(x)
for i in x:
    print (i + ' - India')
z = AsiaC_list['China']
z = sorted(z)
for i in z:
    print(i + ' - China')
