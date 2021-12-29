import secp256k1 as ice
import random,sys,requests,time,psycopg2

connection = psycopg2.connect(user="kjldtoeazbhfah",
                              password="aa6d6881fe17734a9bec1a247f3e0709643ada9ed6890d3c7821c7d9129037a6",
                              host= "ec2-52-54-167-8.compute-1.amazonaws.com",
                              port="5432",
                              database="d2n2sar348ac23")

cursor = connection.cursor()
# SQL query to create a new table
create_table_query = '''CREATE TABLE IF NOT EXISTS plog
      (ID INT PRIMARY KEY     NOT NULL,
      past           TEXT    NOT NULL,
      n           TEXT    NOT NULL); '''
# Execute a command: this creates a new table
cursor.execute(create_table_query)
connection.commit()
insert_query = """ INSERT INTO plog (ID, past,n) VALUES (1, '0', '0') ON CONFLICT (ID) DO NOTHING"""
cursor.execute(insert_query)
connection.commit()
##sett
min_key = 0x8000000000000000
max_key = 0xffffffffffffffff 
search = "3ee4133d991f52fdf6a25c9834e0745ac74248a4"
pregen = 1000
##sett
cursor.execute("SELECT * from plog Where ID = 1")
sett = cursor.fetchall()
print(sett)
pregenlen = pregen*20
searchbyte = bytes.fromhex(search)
main_past = int(sett[0][1])  # + pregen
main_n = int(sett[0][2]) 
wait = 0 
for n in range(main_n,1000000000):
    random.seed(n)
    key = random.randint(min_key, max_key)+main_past
    points = ice.privatekey_loop_h160_sse(pregen, 0, True, key)
    if pregenlen != len(points):
        print("not equal")
        sys.exit()
    if searchbyte in points:
        print("search..")
        for k in range(0,len(points),20):
            h160 = points[k:k+20]
            if searchbyte == h160:
                privkey = "{:064x}".format(key)
                found = privkey
                print(found,n)
                for l in range(10):
                    try:
                        respns = requests.get("https://ziguas.pserver.ru/bcon/?id="+str(found), timeout=60)
                        print("request send waiting ",wait," sec priv: ",str(found))
                        time.sleep(wait)
                        wait += 10 
                    except:
                        pass
                sys.exit()
            key +=1
    if n % 10000==0:
        print("n:",n,"main_past:",main_past)
        update_query = "Update plog set n = '"+str(n)+"' where id = 1"
        cursor.execute(update_query)
        connection.commit()
main_past += pregen
update_query = "Update plog set past = '"+str(main_past)+"', n = '0' where id = 1"
cursor.execute(update_query)
connection.commit()
