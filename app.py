from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    user_id TEXT PRIMARY KEY, 
                    year INTEGER, 
                    semester INTEGER, 
                    password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS faculty (
                    faculty_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    faculty_name TEXT UNIQUE)''')
    c.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    subject_name TEXT, 
                    year INTEGER, 
                    semester INTEGER, 
                    faculty_name TEXT DEFAULT 'None',
              UNIQUE(subject_name,year,semester))''')
    # c.execute('''CREATE TABLE IF NOT EXISTS feedback (
    #                 user_id TEXT, 
    #                 year INTEGER, 
    #                 semester INTEGER, 
    #                 subject_name TEXT, 
    #                 faculty_name TEXT, 
    #                 question1 INTEGER, 
    #                 question2 INTEGER, 
    #                 question3 INTEGER, 
    #                 question4 INTEGER, 
    #                 question5 INTEGER, 
    #                 question6 INTEGER, 
    #                 question7 INTEGER, 
    #                 question8 INTEGER, 
    #                 question9 INTEGER, 
    #                 question10 INTEGER, 
    #                 suggestions TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS feedback (
                    user_id TEXT, 
                    year INTEGER, 
                    semester INTEGER, 
                    subject_name TEXT, 
                    faculty_name TEXT, 
                    question1 INTEGER, 
                    question2 INTEGER, 
                    question3 INTEGER, 
                    question4 INTEGER, 
                    question5 INTEGER, 
                    question6 INTEGER, 
                    question7 INTEGER, 
                    question8 INTEGER, 
                    question9 INTEGER, 
                    question10 INTEGER, 
                    suggestions TEXT)''')
    
    # c.execute('''CREATE TABLE IF NOT EXISTS feedback (
    #                 user_id TEXT, 
    #                 year INTEGER, 
    #                 semester INTEGER, 
    #                 subject_name TEXT, 
    #                 faculty_name TEXT, 
    #                 feedback_date DATE DEFAULT (CURRENT_DATE),
    #                 question1 INTEGER, 
    #                 question2 INTEGER, 
    #                 question3 INTEGER, 
    #                 question4 INTEGER, 
    #                 question5 INTEGER, 
    #                 question6 INTEGER, 
    #                 question7 INTEGER, 
    #                 question8 INTEGER, 
    #                 question9 INTEGER, 
    #                 question10 INTEGER, 
    #                 suggestions TEXT)''')



    # Sample data for students
    # students_data = [
    #     ('22X41A1201',3,1, generate_password_hash('22X41A1201')),
    #     ('22X41A1202',3,1, generate_password_hash('22X41A1202')),
    #     ('22X41A1203',3,1, generate_password_hash('22X41A1203')),
    #     ('22X41A1204',3,1, generate_password_hash('22X41A1204')),
    #     ('22X41A1205',3,1, generate_password_hash('22X41A1205')),
    #     ('22X41A1206',3,1, generate_password_hash("22X41A1206")),
    #     ('22X41A1207',3,1, generate_password_hash('22X41A1207')),
    #     ('22X41A1208',3,1, generate_password_hash('22X41A1208')),
    #     ('22X41A1209',3,1, generate_password_hash('22X41A1209')),
    #     ('22X41A1210',3,1, generate_password_hash('22X41A1210')),
    #     ('22X41A1211',3,1, generate_password_hash('22X41A1211')),
    #     ('22X41A1212',3,1, generate_password_hash('22X41A1212')),
    #     ('22X41A1213',3,1, generate_password_hash('22X41A1213')),
    #     ('22X41A1214',3,1, generate_password_hash('22X41A1214')),
    #     ('22X41A1215',3,1, generate_password_hash('22X41A1215')),
    #     ('22X41A1216',3,1, generate_password_hash('22X41A1216')),        
    #     ('22X41A1217',3,1, generate_password_hash('22X41A1217')),
    #     ('22X41A1218',3,1, generate_password_hash('22X41A1218')),
    #     ('22X41A1219',3,1, generate_password_hash('22X41A1219')),
    #     ('22X41A1220',3,1, generate_password_hash('22X41A1220')),
    #     ('22X41A1221',3,1, generate_password_hash('22X41A1221')),
    #     ('22X41A1222',3,1, generate_password_hash('22X41A1222')),
    #     ('22X41A1223',3,1, generate_password_hash('22X41A1223')),
    #     ('22X41A1224',3,1, generate_password_hash('22X41A1224' )),
    #     ('22X41A1225',3,1, generate_password_hash('22X41A1225' )),
    #     ('22X41A1226',3,1, generate_password_hash('22X41A1226' )),
    #     ('22X41A1227',3,1, generate_password_hash('22X41A1227' )),
    #     ('22X41A1228',3,1, generate_password_hash('22X41A1228' )),
    #     ('22X41A1229',3,1, generate_password_hash('22X41A1229' )),
    #     ('22X41A1230',3,1, generate_password_hash('22X41A1230' )),
    #     ('22X41A1231',3,1, generate_password_hash('22X41A1231' )),
    #     ('22X41A1232',3,1, generate_password_hash('22X41A1232' )),
    #     ('22X41A1233',3,1, generate_password_hash('22X41A1233' )),
    #     ('22X41A1234',3,1, generate_password_hash('22X41A1234' )),
    #     ('22X41A1235',3,1, generate_password_hash('22X41A1235' )),
    #     ('22X41A1236',3,1, generate_password_hash('22X41A1236' )),
    #     ('22X41A1237',3,1, generate_password_hash('22X41A1237' )),
    #     ('22X41A1238',3,1, generate_password_hash('22X41A1238' )),
    #     ('22X41A1239',3,1, generate_password_hash('22X41A1239' )),
    #     ('22X41A1240',3,1, generate_password_hash('22X41A1240' )),
    #     ('22X41A1241',3,1, generate_password_hash('22X41A1241' )),
    #     ('22X41A1242',3,1, generate_password_hash('22X41A1242' )),
    #     ('22X41A1243',3,1, generate_password_hash('22X41A1243' )),
    #     ('22X41A1244',3,1, generate_password_hash('22X41A1244' )),
    #     ('22X41A1245',3,1, generate_password_hash('22X41A1245' )),
    #     ('22X41A1246',3,1, generate_password_hash('22X41A1246' )),
    #     ('22X41A1247',3,1, generate_password_hash('22X41A1247' )),
    #     ('22X41A1248',3,1, generate_password_hash('22X41A1248' )),
    #     ('22X41A1249',3,1, generate_password_hash('22X41A1249' )),
    #     ('22X41A1250',3,1, generate_password_hash('22X41A1250' )),
    #     ('22X41A1251',3,1, generate_password_hash('22X41A1251' )),
    #     ('22X41A1252',3,1, generate_password_hash('22X41A1252' )),
    #     ('22X41A1253',3,1, generate_password_hash('22X41A1253' )),
    #     ('22X41A1254',3,1, generate_password_hash('22X41A1254' )),
    #     ('22X41A1255',3,1, generate_password_hash('22X41A1255' )),
    #     ('22X41A1256',3,1, generate_password_hash('22X41A1256' )),
    #     ('22X41A1257',3,1, generate_password_hash('22X41A1257' )),
    #     ('22X41A1258',3,1, generate_password_hash('22X41A1258' )),
    #     ('22X41A1259',3,1, generate_password_hash('22X41A1259' )),
    #     ('23X45A1201',3,1, generate_password_hash('22X41A1201' )),
    #     ('23X45A1202',3,1, generate_password_hash('22X41A1202' )),
    #     ('23X45A1203',3,1, generate_password_hash('22X41A1203' )),
    #     ('23X45A1204',3,1, generate_password_hash('22X41A1204' )),
    #     ('23X45A1205',3,1, generate_password_hash('22X41A1205' )),
    #     ('23X45A1206',3,1, generate_password_hash('22X41A1206' )),
    #     ('23X45A1207',3,1, generate_password_hash('22X41A1207' )),
    #     ('23X45A1208',3,1, generate_password_hash('22X41A1208' )),
    #     ('23X45A1209',3,1, generate_password_hash('22X41A1209' )),
    #     ('23X45A1210',3,1, generate_password_hash('22X41A1210' )),
    #     ('23X45A1211',3,1, generate_password_hash('22X41A1211' )),
    #     ('23X45A1212',3,1, generate_password_hash('22X41A1212' )),
    #     ('23X45A1213',3,1, generate_password_hash('22X41A1213' )),
    #     ('21X41A1201',4,1, generate_password_hash('21X41A1201' )),
    #     ('21X41A1202',4,1, generate_password_hash('21X41A1202' )),
    #     ('21X41A1203',4,1, generate_password_hash('21X41A1203' )),
    #     ('21X41A1204',4,1, generate_password_hash('21X41A1204' )),
    #     ('21X41A1205',4,1, generate_password_hash('21X41A1205' )),
    #     ('21X41A1206',4,1, generate_password_hash('21X41A1206' )),
    #     ('21X41A1207',4,1, generate_password_hash('21X41A1207' )),
    #     ('21X41A1208',4,1, generate_password_hash('21X41A1208' )),
    #     ('21X41A1209',4,1, generate_password_hash('21X41A1209' )),
    #     ('21X41A1210',4,1, generate_password_hash('21X41A1210' )),
    #     ('21X41A1211',4,1, generate_password_hash('21X41A1211' )),
    #     ('21X41A1212',4,1, generate_password_hash('21X41A1212' )),
    #     ('21X41A1213',4,1, generate_password_hash('21X41A1213' )),
    #     ('21X41A1214',4,1, generate_password_hash('21X41A1214' )),
    #     ('21X41A1215',4,1, generate_password_hash('21X41A1215' )),
    #     ('21X41A1216',4,1, generate_password_hash('21X41A1216' )),
    #     ('21X41A1217',4,1, generate_password_hash('21X41A1217' )),
    #     ('21X41A1218',4,1, generate_password_hash('21X41A1218' )),
    #     ('21X41A1219',4,1, generate_password_hash('21X41A1219' )),
    #     ('21X41A1220',4,1, generate_password_hash('21X41A1220'  )),
    #     ('21X41A1221',4,1, generate_password_hash('21X41A1221' )),
    #     ('21X41A1222',4,1, generate_password_hash('21X41A1222' )),
    #     ('21X41A1223',4,1, generate_password_hash('21X41A1223' )),
    #     ('21X41A1224',4,1, generate_password_hash('21X41A1224' )),
    #     ('21X41A1225',4,1, generate_password_hash('21X41A1225' )),
    #     ('21X41A1226',4,1, generate_password_hash('21X41A1226' )),
    #     ('21X41A1227',4,1, generate_password_hash('21X41A1227' )),
    #     ('21X41A1228',4,1, generate_password_hash('21X41A1228' )),
    #     ('21X41A1229',4,1, generate_password_hash('21X41A1229' )),
    #     ('21X41A1230',4,1, generate_password_hash('21X41A1230' )),
    #     ('21X41A1231',4,1, generate_password_hash('21X41A1231' )),
    #     ('21X41A1232',4,1, generate_password_hash('21X41A1232' )),
    #     ('21X41A1233',4,1, generate_password_hash('21X41A1233' )),
    #     ('21X41A1234',4,1, generate_password_hash('21X41A1234' )),
    #     ('21X41A1235',4,1, generate_password_hash('21X41A1235' )),
    #     ('21X41A1236',4,1, generate_password_hash('21X41A1236' )),
    #     ('21X41A1237',4,1, generate_password_hash('21X41A1237' )),
    #     ('21X41A1238',4,1, generate_password_hash('21X41A1238' )),
    #     ('21X41A1239',4,1, generate_password_hash('21X41A1239' )),
    #     ('21X41A1240',4,1, generate_password_hash('21X41A1240' )),
    #     ('21X41A1241',4,1, generate_password_hash('21X41A1241' )),
    #     ('21X41A1242',4,1, generate_password_hash('21X41A1242' )),
    #     ('21X41A1243',4,1, generate_password_hash('21X41A1243' )),
    #     ('21X41A1244',4,1, generate_password_hash('21X41A1244' )),
    #     ('21X41A1245',4,1, generate_password_hash('21X41A1245' )),
    #     ('21X41A1246',4,1, generate_password_hash('21X41A1246' )),
    #     ('21X41A1247',4,1, generate_password_hash('21X41A1247' )),
    #     ('21X41A1248',4,1, generate_password_hash('21X41A1248' )),
    #     ('21X41A1249',4,1, generate_password_hash('21X41A1249' )),
    #     ('21X41A1250',4,1, generate_password_hash('21X41A1250' )),
    #     ('21X41A1251',4,1, generate_password_hash('21X41A1251' )),
    #     ('21X41A1252',4,1, generate_password_hash('21X41A1252' )),
    #     ('21X41A1253',4,1, generate_password_hash('21X41A1253' )),
    #     ('21X41A1254',4,1, generate_password_hash('21X41A1254' )),
    #     ('21X41A1255',4,1, generate_password_hash('21X41A1255' )),
    #     ('21X41A1256',4,1, generate_password_hash('21X41A1256' )),
    #     ('21X41A1257',4,1, generate_password_hash('21X41A1257' )),
    #     ('21X41A1258',4,1, generate_password_hash('21X41A1258' )),
    #     ('21X41A1259',4,1, generate_password_hash('21X41A1259' )),
    #     ('21X41A1260',4,1, generate_password_hash('21X41A1260' )),
    #     ('21X41A1261',4,1, generate_password_hash('21X41A1261' )),
    #     ('21X41A1262',4,1, generate_password_hash('21X41A1262' )),
    #     ('21X41A1263',4,1, generate_password_hash('21X41A1263' )),
    #     ('21X41A1264',4,1, generate_password_hash('21X41A1264' )),
    #     ('21X41A1265',4,1, generate_password_hash('21X41A1265' )),
    #     ('21X41A1266',4,1, generate_password_hash('21X41A1266' )),
    #     ('21X41A1267',4,1, generate_password_hash('21X41A1267' )),
    #     ('21X41A1268',4,1, generate_password_hash('21X41A1268' ))
    # ]
 
    students_data = [
        ('23X41A1201',2,2, generate_password_hash('23X41A1201')),
        ('23X41A1202',2,2, generate_password_hash('23X41A1202')),
        ('23X41A1203',2,2, generate_password_hash('23X41A1203')),
        ('23X41A1204',2,2, generate_password_hash('23X41A1204')),
        ('23X41A1205',2,2, generate_password_hash('23X41A1205')),
        ('23X41A1206',2,2, generate_password_hash("23X41A1206")),
        ('23X41A1207',2,2, generate_password_hash('23X41A1207')),
        ('23X41A1208',2,2, generate_password_hash('23X41A1208')),
        ('23X41A1209',2,2, generate_password_hash('23X41A1209')),
        ('23X41A1210',2,2, generate_password_hash('23X41A1210')),
        ('23X41A1211',2,2, generate_password_hash('23X41A1211')),
        ('23X41A1212',2,2, generate_password_hash('23X41A1212')),
        ('23X41A1213',2,2, generate_password_hash('23X41A1213')),
        ('23X41A1214',2,2, generate_password_hash('23X41A1214')),
        ('23X41A1215',2,2, generate_password_hash('23X41A1215')),
        ('23X41A1216',2,2, generate_password_hash('23X41A1216')),        
        ('23X41A1217',2,2, generate_password_hash('23X41A1217')),
        ('23X41A1218',2,2, generate_password_hash('23X41A1218')),
        ('23X41A1219',2,2, generate_password_hash('23X41A1219')),
        ('23X41A1220',2,2, generate_password_hash('23X41A1220')),
        ('23X41A1221',2,2, generate_password_hash('23X41A1221')),
        ('23X41A1222',2,2, generate_password_hash('23X41A1222')),
        ('23X41A1223',2,2, generate_password_hash('23X41A1223')),
        ('23X41A1224',2,2, generate_password_hash('23X41A1224' )),
        ('23X41A1225',2,2, generate_password_hash('23X41A1225' )),
        ('23X41A1226',2,2, generate_password_hash('23X41A1226' )),
        ('23X41A1227',2,2, generate_password_hash('23X41A1227' )),
        ('23X41A1228',2,2, generate_password_hash('23X41A1228' )),
        ('23X41A1229',2,2, generate_password_hash('23X41A1229' )),
        ('23X41A1230',2,2, generate_password_hash('23X41A1230' )),
        ('23X41A1231',2,2, generate_password_hash('23X41A1231' )),
        ('23X41A1232',2,2, generate_password_hash('23X41A1232' )),
        ('23X41A1233',2,2, generate_password_hash('23X41A1233' )),
        ('23X41A1234',2,2, generate_password_hash('23X41A1234' )),
        ('23X41A1235',2,2, generate_password_hash('23X41A1235' )),
        ('23X41A1236',2,2, generate_password_hash('23X41A1236' )),
        ('23X41A1237',2,2, generate_password_hash('23X41A1237' )),
        ('23X41A1238',2,2, generate_password_hash('23X41A1238' )),
        ('23X41A1239',2,2, generate_password_hash('23X41A1239' )),
        ('23X41A1240',2,2, generate_password_hash('23X41A1240' )),
        ('23X41A1241',2,2, generate_password_hash('23X41A1241' )),
        ('23X41A1242',2,2, generate_password_hash('23X41A1242' )),
        ('23X41A1243',2,2, generate_password_hash('23X41A1243' )),
        ('23X41A1244',2,2, generate_password_hash('23X41A1244' )),
        ('23X41A1245',2,2, generate_password_hash('23X41A1245' )),
        ('23X41A1246',2,2, generate_password_hash('23X41A1246' )),
        ('23X41A1247',2,2, generate_password_hash('23X41A1247' )),
        ('23X41A1248',2,2, generate_password_hash('23X41A1248' )),
        ('23X41A1249',2,2, generate_password_hash('23X41A1249' )),
        ('23X41A1250',2,2, generate_password_hash('23X41A1250' )),
        ('23X41A1251',2,2, generate_password_hash('23X41A1251' )),
        ('23X41A1252',2,2, generate_password_hash('23X41A1252' )),
        ('23X41A1253',2,2, generate_password_hash('23X41A1253' )),
        ('23X41A1254',2,2, generate_password_hash('23X41A1254' )),
        ('23X41A1255',2,2, generate_password_hash('23X41A1255' )),
        ('23X41A1256',2,2, generate_password_hash('23X41A1256' )),
        ('23X41A1257',2,2, generate_password_hash('23X41A1257' )),
        ('23X41A1258',2,2, generate_password_hash('23X41A1258' )),
        ('23X41A1259',2,2, generate_password_hash('23X41A1259' )),
        ('23X45A1260',2,2, generate_password_hash('23X41A1260' )),
        ('23X45A1261',2,2, generate_password_hash('23X41A1261' )),
        ('23X45A1262',2,2, generate_password_hash('23X41A1262' )),
        ('23X45A1263',2,2, generate_password_hash('23X41A1263' )),
        ('23X45A1264',2,2, generate_password_hash('23X41A1264' )),
        ('23X45A1265',2,2, generate_password_hash('23X41A1265' )),
        ('23X45A1266',2,2, generate_password_hash('23X41A1266' )),
        ('24X45A1201',2,2, generate_password_hash('24X41A1201' )),
        ('24X45A1202',2,2, generate_password_hash('24X41A1202' )),
        ('24X45A1203',2,2, generate_password_hash('24X41A1203' )),       
        ('24X45A1204',2,2, generate_password_hash('24X41A1204' )),
        ('24X45A1205',2,2, generate_password_hash('24X41A1205' )),
        ('24X45A1206',2,2, generate_password_hash('24X41A1206' )),
        

        ('22X41A1201',3,2, generate_password_hash('22X41A1201')),
        ('22X41A1202',3,2, generate_password_hash('22X41A1202')),
        ('22X41A1203',3,2, generate_password_hash('22X41A1203')),
        ('22X41A1204',3,2, generate_password_hash('22X41A1204')),
        ('22X41A1205',3,2, generate_password_hash('22X41A1205')),
        ('22X41A1206',3,2, generate_password_hash("22X41A1206")),
        ('22X41A1207',3,2, generate_password_hash('22X41A1207')),
        ('22X41A1208',3,2, generate_password_hash('22X41A1208')),
        ('22X41A1209',3,2, generate_password_hash('22X41A1209')),
        ('22X41A1210',3,2, generate_password_hash('22X41A1210')),
        ('22X41A1211',3,2, generate_password_hash('22X41A1211')),
        ('22X41A1212',3,2, generate_password_hash('22X41A1212')),
        ('22X41A1213',3,2, generate_password_hash('22X41A1213')),
        ('22X41A1214',3,2, generate_password_hash('22X41A1214')),
        ('22X41A1215',3,2, generate_password_hash('22X41A1215')),
        ('22X41A1216',3,2, generate_password_hash('22X41A1216')),        
        ('22X41A1217',3,2, generate_password_hash('22X41A1217')),
        ('22X41A1218',3,2, generate_password_hash('22X41A1218')),
        ('22X41A1219',3,2, generate_password_hash('22X41A1219')),
        ('22X41A1220',3,2, generate_password_hash('22X41A1220')),
        ('22X41A1221',3,2, generate_password_hash('22X41A1221')),
        ('22X41A1222',3,2, generate_password_hash('22X41A1222')),
        ('22X41A1223',3,2, generate_password_hash('22X41A1223')),
        ('22X41A1224',3,2, generate_password_hash('22X41A1224' )),
        ('22X41A1225',3,2, generate_password_hash('22X41A1225' )),
        ('22X41A1226',3,2, generate_password_hash('22X41A1226' )),
        ('22X41A1227',3,2, generate_password_hash('22X41A1227' )),
        ('22X41A1228',3,2, generate_password_hash('22X41A1228' )),
        ('22X41A1229',3,2, generate_password_hash('22X41A1229' )),
        ('22X41A1230',3,2, generate_password_hash('22X41A1230' )),
        ('22X41A1231',3,2, generate_password_hash('22X41A1231' )),
        ('22X41A1232',3,2, generate_password_hash('22X41A1232' )),
        ('22X41A1233',3,2, generate_password_hash('22X41A1233' )),
        ('22X41A1234',3,2, generate_password_hash('22X41A1234' )),
        ('22X41A1235',3,2, generate_password_hash('22X41A1235' )),
        ('22X41A1236',3,2, generate_password_hash('22X41A1236' )),
        ('22X41A1237',3,2, generate_password_hash('22X41A1237' )),
        ('22X41A1238',3,2, generate_password_hash('22X41A1238' )),
        ('22X41A1239',3,2, generate_password_hash('22X41A1239' )),
        ('22X41A1240',3,2, generate_password_hash('22X41A1240' )),
        ('22X41A1241',3,2, generate_password_hash('22X41A1241' )),
        ('22X41A1242',3,2, generate_password_hash('22X41A1242' )),
        ('22X41A1243',3,2, generate_password_hash('22X41A1243' )),
        ('22X41A1244',3,2, generate_password_hash('22X41A1244' )),
        ('22X41A1245',3,2, generate_password_hash('22X41A1245' )),
        ('22X41A1246',3,2, generate_password_hash('22X41A1246' )),
        ('22X41A1247',3,2, generate_password_hash('22X41A1247' )),
        ('22X41A1248',3,2, generate_password_hash('22X41A1248' )),
        ('22X41A1249',3,2, generate_password_hash('22X41A1249' )),
        ('22X41A1250',3,2, generate_password_hash('22X41A1250' )),
        ('22X41A1251',3,2, generate_password_hash('22X41A1251' )),
        ('22X41A1252',3,2, generate_password_hash('22X41A1252' )),
        ('22X41A1253',3,2, generate_password_hash('22X41A1253' )),
        ('22X41A1254',3,2, generate_password_hash('22X41A1254' )),
        ('22X41A1255',3,2, generate_password_hash('22X41A1255' )),
        ('22X41A1256',3,2, generate_password_hash('22X41A1256' )),
        ('22X41A1257',3,2, generate_password_hash('22X41A1257' )),
        ('22X41A1258',3,2, generate_password_hash('22X41A1258' )),
        ('22X41A1259',3,2, generate_password_hash('22X41A1259' )),
        ('23X45A1201',3,2, generate_password_hash('23X45A1201' )),
        ('23X45A1202',3,2, generate_password_hash('23X45A1202' )),
        ('23X45A1203',3,2, generate_password_hash('23X45A1203' )),
        ('23X45A1204',3,2, generate_password_hash('23X45A1204' )),
        ('23X45A1205',3,2, generate_password_hash('23X45A1205' )),
        ('23X45A1206',3,2, generate_password_hash('23X45A1206' )),
        ('23X45A1207',3,2, generate_password_hash('23X45A1207' )),
        ('23X45A1208',3,2, generate_password_hash('23X45A1208' )),
        ('23X45A1209',3,2, generate_password_hash('23X45A1209' )),
        ('23X45A1210',3,2, generate_password_hash('23X45A1210' )),
        ('23X45A1211',3,2, generate_password_hash('23X45A1211' )),
        ('23X45A1212',3,2, generate_password_hash('23X45A1212' )),
        ('23X45A1213',3,2, generate_password_hash('23X45A1213' )),
        ('21X41A1201',4,2, generate_password_hash('21X41A1201' )),
        ('21X41A1202',4,2, generate_password_hash('21X41A1202' )),
        ('21X41A1203',4,2, generate_password_hash('21X41A1203' )),
        ('21X41A1204',4,2, generate_password_hash('21X41A1204' )),
        ('21X41A1205',4,2, generate_password_hash('21X41A1205' )),
        ('21X41A1206',4,2, generate_password_hash('21X41A1206' )),
        ('21X41A1207',4,2, generate_password_hash('21X41A1207' )),
        ('21X41A1208',4,2, generate_password_hash('21X41A1208' )),
        ('21X41A1209',4,2, generate_password_hash('21X41A1209' )),
        ('21X41A1210',4,2, generate_password_hash('21X41A1210' )),
        ('21X41A1211',4,2, generate_password_hash('21X41A1211' )),
        ('21X41A1212',4,2, generate_password_hash('21X41A1212' )),
        ('21X41A1213',4,2, generate_password_hash('21X41A1213' )),
        ('21X41A1214',4,2, generate_password_hash('21X41A1214' )),
        ('21X41A1215',4,2, generate_password_hash('21X41A1215' )),
        ('21X41A1216',4,2, generate_password_hash('21X41A1216' )),
        ('21X41A1217',4,2, generate_password_hash('21X41A1217' )),
        ('21X41A1218',4,2, generate_password_hash('21X41A1218' )),
        ('21X41A1219',4,2, generate_password_hash('21X41A1219' )),
        ('21X41A1220',4,2, generate_password_hash('21X41A1220' )),
        ('21X41A1221',4,2, generate_password_hash('21X41A1221' )),
        ('21X41A1222',4,2, generate_password_hash('21X41A1222' )),
        ('21X41A1223',4,2, generate_password_hash('21X41A1223' )),
        ('21X41A1224',4,2, generate_password_hash('21X41A1224' )),
        ('21X41A1225',4,2, generate_password_hash('21X41A1225' )),
        ('21X41A1226',4,2, generate_password_hash('21X41A1226' )),
        ('21X41A1227',4,2, generate_password_hash('21X41A1227' )),
        ('21X41A1228',4,2, generate_password_hash('21X41A1228' )),
        ('21X41A1229',4,2, generate_password_hash('21X41A1229' )),
        ('21X41A1230',4,2, generate_password_hash('21X41A1230' )),
        ('21X41A1231',4,2, generate_password_hash('21X41A1231' )),
        ('21X41A1232',4,2, generate_password_hash('21X41A1232' )),
        ('21X41A1233',4,2, generate_password_hash('21X41A1233' )),
        ('21X41A1234',4,2, generate_password_hash('21X41A1234' )),
        ('21X41A1235',4,2, generate_password_hash('21X41A1235' )),
        ('21X41A1236',4,2, generate_password_hash('21X41A1236' )),
        ('21X41A1237',4,2, generate_password_hash('21X41A1237' )),
        ('21X41A1238',4,2, generate_password_hash('21X41A1238' )),
        ('21X41A1239',4,2, generate_password_hash('21X41A1239' )),
        ('21X41A1240',4,2, generate_password_hash('21X41A1240' )),
        ('21X41A1241',4,2, generate_password_hash('21X41A1241' )),
        ('21X41A1242',4,2, generate_password_hash('21X41A1242' )),
        ('21X41A1243',4,2, generate_password_hash('21X41A1243' )),
        ('21X41A1244',4,2, generate_password_hash('21X41A1244' )),
        ('21X41A1245',4,2, generate_password_hash('21X41A1245' )),
        ('21X41A1246',4,2, generate_password_hash('21X41A1246' )),
        ('21X41A1247',4,2, generate_password_hash('21X41A1247' )),
        ('21X41A1248',4,2, generate_password_hash('21X41A1248' )),
        ('21X41A1249',4,2, generate_password_hash('21X41A1249' )),
        ('21X41A1250',4,2, generate_password_hash('21X41A1250' )),
        ('21X41A1251',4,2, generate_password_hash('21X41A1251' )),
        ('21X41A1252',4,2, generate_password_hash('21X41A1252' )),
        ('21X41A1253',4,2, generate_password_hash('21X41A1253' )),
        ('21X41A1254',4,2, generate_password_hash('21X41A1254' )),
        ('21X41A1255',4,2, generate_password_hash('21X41A1255' )),
        ('21X41A1256',4,2, generate_password_hash('21X41A1256' )),
        ('21X41A1257',4,2, generate_password_hash('21X41A1257' )),
        ('21X41A1258',4,2, generate_password_hash('21X41A1258' )),
        ('21X41A1259',4,2, generate_password_hash('21X41A1259' )),
        ('21X41A1260',4,2, generate_password_hash('21X41A1260' )),
        ('21X41A1261',4,2, generate_password_hash('21X41A1261' )),
        ('21X41A1262',4,2, generate_password_hash('21X41A1262' )),
        ('21X41A1263',4,2, generate_password_hash('21X41A1263' )),
        ('21X41A1264',4,2, generate_password_hash('21X41A1264' )),
        ('22X45A1201',4,2, generate_password_hash('22X45A1201' )),
        ('22X45A1202',4,2, generate_password_hash('22X45A1202' )),
        ('22X45A1203',4,2, generate_password_hash('22X45A1203' )),
        ('22X45A1204',4,2, generate_password_hash('22X45A1204' )),
        ('22X45A1205',4,2, generate_password_hash('22X45A1205' )),
        ('22X45A1206',4,2, generate_password_hash('22X45A1206' ))
    ]
    
    for student in students_data:
        c.execute("INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?)", student)
    
    # Sample data for faculty
    faculty_data = [
        'Amritha Mishra', 'P.Sai Charitha', 'G.D.K.Kishore', 'G.Sri Lakshmi', 'Neelima priyanka','Y.Maneesha'
    ]
    
    # for faculty in faculty_data:
        # c.execute("INSERT OR IGNORE INTO faculty (faculty_name) VALUES (?)", (faculty,))

    for faculty in faculty_data:
        c.execute("INSERT OR IGNORE INTO faculty (faculty_name) VALUES (?)", (faculty,))

    
    # Sample data for subjects
    # subjects_data = [
    #     ('Communicative English' , 1 , 1, 'None'),
    #     ('M1',1,1,'None'),
    #     ('Applied Physics',1,1,'None'),
    #     ('C Programming',1,1,'None'),
    #     ('M2',1,2,'None'),
    #     ('Applied Chemistry',1,2,'None'),
    #     ('Computer Organisation',1,2,'None'),
    #     ('Python Programming',1,2,'None'),
    #     ('Data Structures',1,2,'None'),
    #     ('M3', 2, 1, 'None'),
    #     ('DMG', 2, 1, 'None'),
    #     ('OOPS through C++',2, 1, "None"),
    #     ('OS', 2, 1, "None"),
    #     ('DBMS',2,1, "None"),
    #     ('S R', 2,2, "None"),
    #     ('ATCD',2,2, "None"),
    #     ('JAVA',2,2, 'None'),
    #     ('PSE', 2, 2, 'None'),
    #     ('MEFA', 2, 2, 'None'),
    #     ('SET', 3 , 1 , "None"),
    #     ('DAA', 3, 1, 'None'),
    #     ('DMT', 3, 1, 'None'),
    #     ('AUP', 3, 1, 'None'),
    #     ('CN', 3, 1, 'None'),
    #     ('ML', 3, 2, 'None'),
    #     ('CNS', 3, 2, 'None'),
    #     ('MEAN', 3, 2, 'None'),
    #     ('Big Data', 3, 2, 'None'),
    #     ('Cloud Computing', 4 , 1 , "None"),
    #     ('Deep Learning', 4,1,'None'),
    #     ("M-Com", 4, 1,'None'),
    #     ('Human Values', 4 , 1 , 'None')
    # ]
    
    
    subjects_data = [
        ('Communicative English' , 1 , 1, 'None'),
        ('M1',1,1,'None'),
        ('Applied Physics',1,1,'None'),
        ('C Programming',1,1,'None'),
        ('M2',1,2,'None'),
        ('Applied Chemistry',1,2,'None'),
        ('Computer Organisation',1,2,'None'),
        ('Python Programming',1,2,'None'),
        ('Data Structures',1,2,'None'),
        ('Universal Human Values', 2, 1, 'None'),
        ('DMG', 2, 1, 'None'),
        ('Digital Logic and Computer Organization',2, 1, "None"),
        ('Advanced Data Structures and Algorithms', 2, 1, "None"),
        ('Object Oriented Through JAVA',2,1, "None"),
        ('Environmental Values',2,1, "None"),
        ('Statistics with R', 2,2, "None"),
        ('ATCD',2,2, "None"),
        ('JAVA',2,2, 'None'),
        ('PSE', 2, 2, 'None'),
        ('MEFA', 2, 2, 'None'),
        ('SET', 3 , 1 , "None"),
        ('DAA', 3, 1, 'None'),
        ('DMT', 3, 1, 'None'),
        ('AUP', 3, 1, 'None'),
        ('CN', 3, 1, 'None'),
        ('ML', 3, 2, 'None'),
        ('CNS', 3, 2, 'None'),
        ('Design Patterns', 3, 2, 'None'),
        ('Disaster Management', 3, 2, 'None'),
        ('Big Data Analytics', 3, 2, 'None'),
        ('Cloud Computing', 4 , 1 , "None"),
        ('Advanced Database', 4 , 1 , "None"),
        ('Deep Learning', 4,1,'None'),
        ("M-Com", 4, 1,'None'),
        ('Human Values', 4 , 1 , 'None')
    ]
    # for subject in subjects_data:
    #     c.execute("INSERT OR IGNORE INTO subjects VALUES (?, ?, ?, ?)", subject)
    
    # Faculty insertion with unique constraint


# Subjects insertion with unique constraint
    for subject in subjects_data:
        c.execute("INSERT OR IGNORE INTO subjects VALUES (?, ?, ?, ?)", subject)



    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         user_id = request.form['user_id']
#         password = request.form['password']
#         conn = sqlite3.connect('database.db')
#         c = conn.cursor()
#         c.execute("SELECT * FROM students WHERE user_id=? AND password=?", (user_id, password))
#         student = c.fetchone()
#         conn.close()
#         if student:
#             session['user_id'] = user_id
#             session['year'] = student[1]
#             session['semester'] = student[2]
#             return redirect(url_for('feedback'))
#     return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM students WHERE user_id=?", (user_id,))
        student = c.fetchone()
        conn.close()
        
        if student and check_password_hash(student[3], password):  # Compare hashed password
            session['user_id'] = user_id
            session['year'] = student[1]
            session['semester'] = student[2]
            return redirect(url_for('feedback'))
        else:
            return render_template('login.html', error="Invalid user ID or password")
    return render_template('login.html')



@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            user_id = session['user_id']
            year = request.form['year']
            semester = request.form['semester']
            subject_name = request.form['subject_name']
            faculty_name = request.form['faculty_name']
            question1 = request.form['question1']
            question2 = request.form['question2']
            question3 = request.form['question3']
            question4 = request.form['question4']
            question5 = request.form['question5']
            question6 = request.form['question6']
            question7 = request.form['question7']
            question8 = request.form['question8']
            question9 = request.form['question9']
            question10 = request.form['question10']
            suggestions = request.form['suggestions']
            
            print("Received feedback form submission")
            print(f"user_id: {user_id}, year: {year}, semester: {semester}, subject_name: {subject_name}, faculty_name: {faculty_name}")
            
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            
            # Update faculty name in subjects table
            c.execute('''UPDATE subjects SET faculty_name = ? 
                         WHERE subject_name = ? AND year = ? AND semester = ?''', 
                         (faculty_name, subject_name, year, semester))
            
            print("Faculty name updated in subjects table")
            
            # Insert feedback into feedback table
            c.execute('''INSERT INTO feedback (user_id, year, semester, subject_name, faculty_name, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, suggestions)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)''', 
                         (user_id, year, semester, subject_name, faculty_name, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, suggestions))
            
            print("Feedback inserted into feedback table")
                         
            conn.commit()
            conn.close()
            
            print("Feedback submitted successfully")
            
            return redirect(url_for('thank_you'))
        except Exception as e:
            print("Error submitting feedback:", e)
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT faculty_name FROM faculty")
    faculty = c.fetchall()
    conn.close()
    
    return render_template('feedback.html', faculty=faculty)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('year', None)
    session.pop('semester', None)
    return redirect(url_for('login'))

@app.route('/get_subjects/<int:year>/<int:semester>')
def get_subjects(year, semester):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT subject_name FROM subjects WHERE year=? AND semester=?", (year, semester))
    subjects = c.fetchall()
    conn.close()
    return jsonify(subjects)

if __name__ == '__main__':
    app.run(debug=True)
