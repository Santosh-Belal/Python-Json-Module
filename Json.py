import json

data ='{"var1":"Santosh,Belal","var2":15}'

print(data)

pars=json.loads(data)

print(pars['var1'])

print(type(pars))

data2={

"cars":{"BMW","Ferrari"},

"friends":("Hari","Santosh"),

"numbers":[1,2,3,4,4,4]

}

print(data2['cars'])

print(data2["friends"])

print(data2['numbers'][0])

data3 ='{"var3:"Apple","var4":15}'

print(data3)

jscomb=json.dumps(data3)#

print(jscomb)
