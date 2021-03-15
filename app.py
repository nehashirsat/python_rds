from flask import Flask,render_template,request,redirect,url_for
import socket
import platform
import mysql.connector

app = Flask(__name__)


#getting the details
@app.route('/machineinfo')

def machineinfo():
    #get machine details
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    os_name = platform.system()



    return render_template("machineinfo.html", host_name=host_name, host_ip=host_ip, os_name=os_name)




@app.route('/getflowers')

def flowers():
    #get machine details
  
    conn=mysql.connector.connect(host="devopsdb.clbdj44v7c4x.us-east-1.rds.amazonaws.com",user="admin",passwd="nehashirsat#",database="flowersdb");
    curs=conn.cursor();
    query="select * from flowers_metadata_tbl";
    curs.execute(query);
    data=curs.fetchall();
    print("Data Received")
    print(data)
    len1=len(data)

    return render_template("linuxos.html", len1=len1, data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
