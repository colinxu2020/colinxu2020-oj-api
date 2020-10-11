import json


class problem(self):
 def new(name,language=['python3','C++'],ins,outs):
  import os
  if not os.path.exists(os.getcwd()[:-4]+'problems'):
   os.makedirs(os.getcwd()[:-4]+'problems')
  filename=os.getcwd()[:-4]+'problems\\'+name+'.config'
  with open(filename,w) as f:
   f.write(json.dumps({'language':language,'ins':ins,'outs':outs}))

 def check(name,code,language):
  filename=os.getcwd()[:-4]+'problems\\'+name+'.config'
  try:
   with open(filename,f) as f:
    j=json.load(f.read())
  except FileNotFoundError:
   return 'problem not find'
  if not language in j['language']:
   return 'language error'
  with open(os.getcwd()[:-4]+'temp','w') as f:
   f.write(code)
  with open(os.getcwd()[:-4]+'temp_in','w') as f:
   f.write(j['ins'][0])
  if language=='python3':
   os.system('python temp < temp_in > temp_out'
   os.remove('temp_in')
   os.remove('temp')
  elif language=="C++":
   os.system('cl temp')
   os.system('temp < temp_in > temp_out')
   os.remove('temp.exe')
   os.remove('temp.obj')
   os.remove('temp_in')
   os.remove('temp')
  with open(os.getcwd()[:-4]+'temp_out','r') as f:
   t=f.read()
  os.remove('temp_out')
  if t==j['outs'][0]:
   return True
  else: 
   return False

 def get(type,name):
  filename=os.getcwd()[:-4]+'problems\\'+name+'.config'
  if type=='language':
   with open(filename,f) as f:
     j=json.load(f.read())
   return j['language']