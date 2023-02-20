
from http.client import NOT_FOUND
from xml.dom import NOT_FOUND_ERR


import pymysql
from app import app
from config import mysql
from flask import Flask, jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash





@app.post('/add')
def add_user():
    conn = None
    cursor = None
    
    try:
        
        _json = request.json
        
        _userid = _json['USER_ID']
        _employeeid = _json['EMPLOYEE_ID']
        _username = _json['USERNAME']
        _password = _json['PSWD']
        _create = _json['CREATE_DT_TMs']
        _update = _json['UPDT_DT_TMs']
        _count = _json['UPDT_CNTs']
       
        if _userid and _employeeid and _username and _password and _create and _update and _count and request.method == 'POST':

            conn = mysql.connect()
            cursor = conn.cursor()
            sql = "INSERT INTO users_dimitris_data(USER_ID, EMPLOYEE_ID, USERNAME, PSWD, CREATE_DT_TMs, UPDT_DT_TMs, UPDT_CNTs) VALUES(%s, %s, %s,%s,%s,%s,%s)"
            data = (_userid, _employeeid, _username,_password, _create, _update, _count)
            
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            
            return resp
        else:
            
            return NOT_FOUND_ERR()
        
        
    except Exception as e:
        print(e)
        resp.status_code = 500
        return resp
        
    finally:
        
        cursor.close()
        conn.close()


        


@app.route('/users', methods=['GET'])
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT USER_ID, EMPLOYEE_ID, USERNAME, PSWD, CREATE_DT_TMs, UPDT_DT_TMs, UPDT_CNTs FROM users_dimitris_data")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
        respone.status_code = 500
        return respone
    finally:
        cursor.close()
        conn.close()


@app.route('/user/<int:id>')
def user(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT USER_ID , EMPLOYEE_ID , USERNAME, PSWD,CREATE_DT_TMs,UPDT_DT_TMs,UPDT_CNTs FROM users_dimitris_data WHERE USER_ID=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp.status_code = 500
        return resp
    finally:
        cursor.close() 
        conn.close()

@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    conn = None
    cursor = None
    try:
        
        _json = request.json
        
        _userid = _json['USER_ID']
        _employeeid = _json['EMPLOYEE_ID']
        _username = _json['USERNAME']
        _password = _json['PSWD']
        _create = _json['CREATE_DT_TMs']
        _update = _json['UPDT_DT_TMs']
        _count = _json['UPDT_CNTs']
        print(id)
        print("beforeIf")		
        
        if _userid and _employeeid and _password and  _username and _create and _update and _count and request.method == 'PUT':
            print("hello")
            conn = mysql.connect()
            cursor = conn.cursor()
            sql = "UPDATE users_dimitris_data SET  EMPLOYEE_ID=%s, USERNAME=%s, PSWD=%s, CREATE_DT_TMs=%s, UPDT_DT_TMs=%s, UPDT_CNTs=%s WHERE USER_ID=%s"
            data = ( _employeeid,_username,_password,_create,_update,_count,id)
            
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            print("else")
            return NOT_FOUND()
    except Exception as e:
        print(e)
        resp.status_code = 500
        return resp
    finally:
        cursor.close() 
        conn.close()



@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users_dimitris_data WHERE USER_ID=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp.status_code = 500
        return resp
    finally:
        cursor.close() 
        conn.close()

@app.post('/addd')
def addd_user():
    conn = None
    cursor = None
    
    try:
        
        _json = request.json
        
        _userid = _json['USER_ID']
        _employeeid = _json['EMPLOYEE_ID']
        _username = _json['USERNAME']
        _password = _json['PSWD']
       # _create = _json['CREATE_DT_TMs']
       # _update = _json['UPDT_DT_TMs']
       # _count = _json['UPDT_CNTs']
       
        if _userid and _employeeid and _username and _password and request.method == 'POST':
            
            _hashed_password = generate_password_hash(_password)
            conn = mysql.connect()
            cursor = conn.cursor()
            sql = "INSERT INTO users_dimitris_data(USER_ID, EMPLOYEE_ID, USERNAME, PSWD) VALUES(%s, %s, %s,%s)"
            data = (_userid, _employeeid, _username,_hashed_password)
            
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            
            return resp
        else:
            
            return NOT_FOUND_ERR()
        
        
    except Exception as e:
        print(e)
        resp.status_code = 500
        return resp
        
    finally:
        
        cursor.close()
        conn.close()




@app.route('/upddate/<int:id>', methods=['PUT'])
def upddate_user(id):
    conn = None
    cursor = None
    try:
        
        _json = request.json
        
        _userid = _json['USER_ID']
        _employeeid = _json['EMPLOYEE_ID']
        _username = _json['USERNAME']
        _pasword = _json['PSWD']
       # _create = _json['CREATE_DT_TMs']
       # _update = _json['UPDT_DT_TMs']
       # _count = _json['UPDT_CNTs']
        print(id)
        print("beforeIf")		
        
        if _userid and _employeeid and _pasword and  _username and request.method == 'PUT':
            print("hello")
            _hashed_password = generate_password_hash(_pasword)
            conn = mysql.connect()
            cursor = conn.cursor()
            sql = "UPDATE users_dimitris_data SET  EMPLOYEE_ID=%s, USERNAME=%s, PSWD=%s WHERE USER_ID=%s"
            data = ( _employeeid,_username,_hashed_password,id)
            
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            print("else")
            return NOT_FOUND()
    except Exception as e:
        print(e)
        resp.status_code = 500
        return resp
    finally:
        cursor.close() 
        conn.close()

@app.post('/insert')
def insert():
    conn = None
    cursor = None
    
    try:
        
        _json = request.json
        
        #_employeeid = _json['EMPLOYEE_ID']
        _departmentid = _json['DEPARTMENT_ID']
        _dasIDemp = _json['EMPLOYEE_EXT_NUMBER']
        _firstname = _json['FIRST_NAME']
        _lastname = _json['LAST_NAME']
        _middlename = _json['MIDDLE_NAME']
        _fullname = _json['FULL_NAME']
        _jobtitle = _json['JOB_TITLE']
        _joblevel = _json['JOB_LEVEL']
        _email = _json['EMAIL']
        _dasIDmanager = _json['MANAGER_EXT_NUMBER']
        _hiredate = _json['HIRE_DT']
        _managerflag = _json['MANAGER_FLAG']
        #_create = _json['CREATE_DT_TMs']
        #_update = _json['UPDT_DT_TMs']
        #_count = _json['UPDT_CNTs']
        

        if  request.method == 'POST':

             
            conn = mysql.connect()
            cursor = conn.cursor()
            sql = "INSERT INTO employees_dimitris_data( DEPARTMENT_ID, EMPLOYEE_EXT_NUMBER,FIRST_NAME,LAST_NAME,MIDDLE_NAME,FULL_NAME,JOB_TITLE,JOB_LEVEL,EMAIL,MANAGER_EXT_NUMBER,HIRE_DT,MANAGER_FLAG) VALUES(%s,%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)"
            data = ( _departmentid, _dasIDemp, _firstname,_lastname,_middlename, _fullname,_jobtitle,_joblevel,_email,_dasIDmanager,_hiredate,_managerflag)
            
            cursor.execute(sql, data)
            conn.commit()
            
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            
            return resp
        else:
            
            return 
        
        
    except Exception as e:
        
        print(e)
        resp.status_code = 500
        return resp
        
    finally:
        
        cursor.close()
        conn.close()


        


@app.route('/employees', methods=['GET'])
def employees():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT  * FROM employees_dimitris_data")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
        respone.status_code = 500
        return respone
    finally:
        cursor.close()
        conn.close()


@app.route('/employee/<int:id>')
def employee(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM employees_dimitris_data WHERE EMPLOYEE_ID=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp.status_code = 500
        return resp
    finally:
        cursor.close() 
        conn.close()

@app.route('/updateemp/<int:id>', methods=['PUT'])
def update_employee(id):
    conn = None
    cursor = None
    try:
        
        _json = request.json
        
        #_employeeid = _json['EMPLOYEE_ID']
        _departmentid = _json['DEPARTMENT_ID']
        _dasIDemp = _json['EMPLOYEE_EXT_NUMBER']
        _firstname = _json['FIRST_NAME']
        _lastname = _json['LAST_NAME']
        _middlename = _json['MIDDLE_NAME']
        _fullname = _json['FULL_NAME']
        _jobtitle = _json['JOB_TITLE']
        _joblevel = _json['JOB_LEVEL']
        _email = _json['EMAIL']
        _dasIDmanager = _json['MANAGER_EXT_NUMBER']
        _hiredate = _json['HIRE_DT']
        _managerflag = _json['MANAGER_FLAG']
        #_create = _json['CREATE_DT_TMs']
        #_update = _json['UPDT_DT_TMs']
        #_count = _json['UPDT_CNTs']		
        print("hello")
        if  request.method == 'PUT':
            print("hi")
            conn = mysql.connect()
            cursor = conn.cursor()
            sql = "UPDATE employees_dimitris_data SET  DEPARTMENT_ID=%s, EMPLOYEE_EXT_NUMBER=%s, FIRST_NAME=%s,LAST_NAME=%s,MIDDLE_NAME=%s,FULL_NAME=%s,JOB_TITLE=%s,JOB_LEVEL=%s,EMAIL=%s,MANAGER_EXT_NUMBER=%s,HIRE_DT=%s,MANAGER_FLAG=%s WHERE EMPLOYEE_ID=%s"
            data = ( _departmentid, _dasIDemp, _firstname,_lastname,_middlename, _fullname,_jobtitle,_joblevel,_email,_dasIDmanager,_hiredate,_managerflag,id)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            print("ho")
            return 
    except Exception as e:
        print(e)
        resp.status_code = 500
        return resp
    finally:
        print("why")
        cursor.close() 
        conn.close()



@app.route('/deleteemp/<int:id>', methods=['DELETE'])
def delete_employee(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees_dimitris_data WHERE EMPLOYEE_ID=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp.status_code = 500
        return resp
    finally:
        cursor.close() 
        conn.close()




@app.route('/skills/<int:id>', methods=['PUT'])
def update_skill(id):
    conn = None
    cursor = None
    try:
        
        _json = request.json
        
        #_skillsId = _json['SKILLS_ID']
        #_employeeId = _json['ID']
        #_dasId = _json['DAS']
        _academy = _json['ACADEMY']
        _kube = _json['K8S']
        _network = _json['NETWORKING']
        _jira = _json['JIRA']
        
        if  request.method == 'PUT':
            
            conn = mysql.connect()
            cursor = conn.cursor()
            sql = "UPDATE skills_dimitris_data SET ACADEMY=%s, K8S=%s, NETWORKING=%s,JIRA=%s WHERE ID=%s"
            data = ( _academy, _kube, _network,_jira,id)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            
            return 
    except Exception as e:
        print(e)
        resp.status_code = 500
        return resp
    finally:
        
        cursor.close() 
        conn.close()



@app.route('/skills', methods=['GET'])
def skills():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT  * FROM skills_dimitris_data")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
        respone.status_code = 500
        return respone
    finally:
        cursor.close()
        conn.close()


@app.route('/empOfManager/<string:id>')
def empOfManager(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM employees_dimitris_data WHERE MANAGER_EXT_NUMBER=%s", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp.status_code = 500
        return resp
    finally:
        cursor.close() 
        conn.close()




@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == "__main__":
    app.run()
