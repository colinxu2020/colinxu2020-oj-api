import rsa
global encodekey
encodekey=rsa.key.PublicKey(22637172592906910124283816971297164433174566474447569061242059342011239698838862384076175351303896836428428778110793244850373588524960953285505306309626530006462685550945681087638958136549877244023341002226859907912671315254608594412870547722245702678624200541649653959222299723593867933296080564190810207332521504903021821126034463857821982587422991166978146902762969220820330093659014869170351884893561884106805061716445924923005893530318370101503554965582481119659686905175940110341313776122972144758929702776627795328752750269339613011300572549115829953241013010985421106882260815699061704657986775203134832208293,65537)

class problem(self):
  from functools import lru_cache
  import json
  import os
  global filename
  filename=os.getcwd()[:-4]+'problems'

  def new(name,language=['python3','C++'],ins,outs):
    if not os.path.exists(filename):
    os.makedirs(filename+'\\problems')
    with open(filename+"\\problems\\"+name+'.json',w) as f:
     f.write(json.dumps({'language':language,'ins':ins,'outs':outs}))

  @lru_cache(maxsize=1024)
  def check(name,code,language):
    try:
      with open(filename+"\\problems\\"+name+'.json',f) as f:
        j=json.load(f.read())
    except FileNotFoundError:
      return 'problem not find'
    if not language in j['language']:
      return 'language error'
    with open(filename+'\\temp','w') as f:
      f.write(code)
    with open(filename+'\\temp_in','w') as f:
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
    with open(filename+'\\temp_out','r') as f:
      t=f.read()
    os.remove('temp_out')
    if t==j['outs'][0]:
      return True
    else: 
      return False

  def get(type,name):
    if type=='language':
      with open(filename+"\\problems\\"+name+'.json',f) as f:
        j=json.load(f.read())
    return j['language']


class user:
  import sqlite3
  global conn,cu
  conn=sqlite3.connect('D:\user.db')
  cu=conn.cursor()
  cu.execute('CREATE TABLE IF NOT EXISTS USER(ID INT,NAME TEXT,PASSWD TEXT);')

  def passworld_check(passworld):
    import re
    if len(passoworld)<7:
      return False
    if re.findall("\D",passworld)==[]:
  	  return False
    return True
  def passworld_encode(passworld):
    import bcrypt
    import secrets
    import string
    password = encode(passworld)
    y=''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(len(passworld)))
    passworldhasy=''.join([passworld[i]+y[i] for i in range(len(passworld))])
    return bcrypt.hashpw(passworldhasy,bcrypt.gensalt())

  def add(uuid,name,passworld,checker=passworld_check,encoder=passworld_encode):
    if not checker(passworld):
      return {'msg':'passworldunsafe'}
    cursor = cu.execute("SELECT name from USER")
    for t in cursor:
      if t[0]==name:
      	return {'msg':'usernamerepeated'}
    cu.execute("INSERT INTO USER (ID,NAME,PASSWD) VALUES ("+str(uuid)+",'' "+name+"','' "+encoder(passworld)+"' )")
    conn.commit()
    return {'msg':'success','uuid':random.random()}

  def check(name,passwd):
  	import time
  	import rsa
  	cursor = cu.execute("SELECT name,passworld from USER")
    if t=[t[0]==name and t[1]==passwd for t in cursor]:
    	lemon_pub,lemon_priv = rsa.newkeys(2048)[0],encodekey
    	cookie=time.time()+rsa.encrypt(passwd,lemon_pub)+name
    	return {'msg':'success'}
    else:
    	return {'msg':'username does not exist or password does not match the username'}
