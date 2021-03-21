import json

x='{"id":"14","Reg":"14.5","City":"ISB"}'
y=json.load(x);
print (y['id'])