import mysql.connector as connection

mydb=  connection.connect(host ="localhost", user = "root", passwd  = "Shankar22@")

cursor = mydb.cursor()

#cursor.execute("insert into darshan.ineuron values(65,'Akshada', 'akshada@gmail.com', 20000 )")
mydb.commit()

#cursor.execute("select * from darshan.ineuron")
cursor.execute("select * from darshan.ineuron")
l=[]
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l[0]))

(57,"blue-collar","married","primary","no",52,"yes","no","unknown",5,"may",38,1,-1,0,"unknown","no"),(
60,"retired","married","primary","no",60,"yes","no","unknown",5,"may",219,1,-1,0,"unknown","no"),(
33,"services","married","secondary","no",0,"yes","no","unknown",5,"may",54,1,-1,0,"unknown","no"),(
28,"blue-collar","married","secondary","no",723,"yes","yes","unknown",5,"may",262,1,-1,0,"unknown","no"),(
56,"management","married","tertiary","no",779,"yes","no","unknown",5,"may",164,1,-1,0,"unknown","no"),(
32,"blue-collar","single","primary","no",23,"yes","yes","unknown",5,"may",160,1,-1,0,"unknown","no"),(
25,"services","married","secondary","no",50,"yes","no","unknown",5,"may",342,1,-1,0,"unknown","no"),(
40,"retired","married","primary","no",0,"yes","yes","unknown",5,"may",181,1,-1,0,"unknown","no"),(
44,"admin.","married","secondary","no",-372,"yes","no","unknown",5,"may",172,1,-1,0,"unknown","no")(
39,"management","single","tertiary","no",255,"yes","no","unknown",5,"may",296,1,-1,0,"unknown","no"),(
52,"entrepreneur","married","secondary","no",113,"yes","yes","unknown",5,"may",127,1,-1,0,"unknown","no"),(
46,"management","single","secondary","no",-246,"yes","no","unknown",5,"may",255,2,-1,0,"unknown","no"),(
36,"technician","single","secondary","no",265,"yes","yes","unknown",5,"may",348,1,-1,0,"unknown","no"),(
57,"technician","married","secondary","no",839,"no","yes","unknown",5,"may",225,1,-1,0,"unknown","no"),(
49,"management","married","tertiary","no",378,"yes","no","unknown",5,"may",230,1,-1,0,"unknown","no"),(
60,"admin.","married","secondary","no",39,"yes","yes","unknown",5,"may",208,1,-1,0,"unknown","no"),(
59,"blue-collar","married","secondary","no",0,"yes","no","unknown",5,"may",226,1,-1,0,"unknown","no"),(
51,"management","married","tertiary","no",10635,"yes","no","unknown",5,"may",336,1,-1,0,"unknown","no"),(
57,"technician","divorced","secondary","no",63,"yes","no","unknown",5,"may",242,1,-1,0,"unknown","no"),(
25,"blue-collar","married","secondary","no",-7,"yes","no","unknown",5,"may",365,1,-1,0,"unknown","no"),(
53,"technician","married","secondary","no",-3,"no","no","unknown",5,"may",1666,1,-1,0,"unknown","no"),(
36,"admin.","divorced","secondary","no",506,"yes","no","unknown",5,"may",577,1,-1,0,"unknown","no"),(
37,"admin.","single","secondary","no",0,"yes","no","unknown",5,"may",137,1,-1,0,"unknown","no"),(
44,"services","divorced","secondary","no",2586,"yes","no","unknown",5,"may",160,1,-1,0,"unknown","no"),(
50,"management","married","secondary","no",49,"yes","no","unknown",5,"may",180,2,-1,0,"unknown","no"),(
60,"blue-collar","married","unknown","no",104,"yes","no","unknown",5,"may",22,1,-1,0,"unknown","no"),(
54,"retired","married","secondary","no",529,"yes","no","unknown",5,"may",1492,1,-1,0,"unknown","no"),(
58,"retired","married","unknown","no",96,"yes","no","unknown",5,"may",616,1,-1,0,"unknown","no"),(
36,"admin.","single","primary","no",-171,"yes","no","unknown",5,"may",242,1,-1,0,"unknown","no"),(
58,"self-employed","married","tertiary","no",-364,"yes","no","unknown",5,"may",355,1,-1,0,"unknown","no"),
(44,"technician","married","secondary","no",0,"yes","no","unknown",5,"may",225,2,-1,0,"unknown","no"),
(55,"technician","divorced","secondary","no",0,"no","no","unknown",5,"may",160,1,-1,0,"unknown","no"),
(29,"management","single","tertiary","no",0,"yes","no","unknown",5,"may",363,1,-1,0,"unknown","no"),
(46,"services","married","primary","no",179,"yes","no","unknown",5,"may",1778,1,-1,0,"unknown","no"
),(32,"admin.","married","tertiary","no",0,"yes","no","unknown",5,"may",138,1,-1,0,"unknown","no"
),(53,"technician","divorced","secondary","no",989,"yes","no","unknown",5,"may",812,1,-1,0,"unknown","no"
),(57,"blue-collar","married","primary","no",249,"yes","no","unknown",5,"may",164,1,-1,0,"unknown","no"
),(33,"services","married","secondary","no",790,"yes","no","unknown",5,"may",391,1,-1,0,"unknown","no"
),(49,"blue-collar","married","unknown","no",154,"yes","no","unknown",5,"may",357,1,-1,0,"unknown","no"
),(51,"management","married","tertiary","no",6530,"yes","no","unknown",5,"may",91,1,-1,0,"unknown","no"
),(60,"retired","married","tertiary","no",100,"no","no","unknown",5,"may",528,1,-1,0,"unknown","no"
),(59,"management","divorced","tertiary","no",59,"yes","no","unknown",5,"may",273,1,-1,0,"unknown","no"
),(35,"blue-collar","single","secondary","no",12223,"yes","yes","unknown",5,"may",177,1,-1,0,"unknown","no"
),(57,"blue-collar","married","secondary","no",5935,"yes","yes","unknown",5,"may",258,1,-1,0,"unknown","no"
),(31,"services","married","secondary","no",25,"yes","yes","unknown",5,"may",172,1,-1,0,"unknown","no"
),(54,"management","married","secondary","no",282,"yes","yes","unknown",5,"may",154,1,-1,0,"unknown","no"
),(55,"blue-collar","married","primary","no",23,"yes","no","unknown",5,"may",291,1,-1,0,"unknown","no"
),(43,"technician","married","secondary","no",1937,"yes","no","unknown",5,"may",181,1,-1,0,"unknown","no"
),(53,"technician","married","secondary","no",384,"yes","no","unknown",5,"may",176,1,-1,0,"unknown","no"
),(44,"blue-collar","married","secondary","no",582,"no","yes","unknown",5,"may",211,1,-1,0,"unknown","no"
),(55,"services","divorced","secondary","no",91,"no","no","unknown",5,"may",349,1,-1,0,"unknown","no"
)