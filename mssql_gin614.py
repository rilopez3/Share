import pymssql
def query(q):
  connect_data = {
      'server': 'SQL5097.site4now.net',
      'user': 'db_9df238_gin614_admin',
      'pass': 'engin614',
      'db': 'db_9df238_gin614' 
  }
  conn = pymssql.connect(
    server = connect_data['server'],
    database = connect_data['db'],
    user =  connect_data['user'], 
    password =  connect_data['pass']
  )
  cursor = conn.cursor()
  data = []
  try:
    cursor.execute(q)
    data = [ tuple(i[0] for i in cursor.description) ]
    results = cursor.fetchall()
    data += results
  except:
    print("An exception occurred")
    print(sys.exc_info()[1] )
  cursor.close()
  return data
def consultar(q):
  for i in query(q):
    for j in i:
      print(j,end='\t')
    print()
def dataf(q):
  data = query(q)
  df = pd.DataFrame(data[1:], columns=data[0])
  return df