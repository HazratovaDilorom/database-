import sqlite3


a=sqlite3.connect('ocupations.db')
b=a.cursor()

b.execute('''
CREATE TABLE IF NOT EXISTS doctor(
    name TEXT
    surname TEXT
    years INTEGER
)''')  



b.execute('''
CREATE TABLE IF NOT EXISTS teacher(
    name TEXT
    surname TEXT
    years INTEGER
)''')
 

b.execute('''
CREATE TABLE IF NOT EXISTS student(
    name TEXT
    surname TEXT
    drection TEXT
)''')


b.execute('''
CREATE TABLE IF NOT EXISTS enginer(
    name TEXT
    surname  TEXT
    experience TEXT  
)''')


b.execute('''
CREATE TABLE IF NOT EXISTS designer(
    name TEXT
    surname TEXT
    projects INTEGER
)''')

c=sqlite3.connect('technology.db')
d=c.cursor()

d.execute('''
CREATE TABLE IF NOT EXISTS kompyuter(
    color TEXT
    cost INTEGER
)''')


d.execute('''
CREATE TABLE IF NOT EXISTS televizor(
    color TEXT
    cost INTEGER
)''') 


d.execute('''
CREATE TABLE IF NOT EXISTS kondidsaner(
    color TEXT
    cost INTEGER
)''')



d.execute('''
CREATE TABLE IF NOT EXISTS telefon(
  color TEXT
  cost  INTEGER        
)''')

