import json
x='{"id":"14","Reg":"14.5","City":"ISB"}'
y=json.loads(x);
print(y['Reg'])