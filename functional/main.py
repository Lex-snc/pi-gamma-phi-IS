from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQLdb
from functools import wraps
from twilio.rest import Client
from flask import make_response
import os
from datetime import datetime



app = Flask(__name__)

#account_sid = 'ACe544c3592df3dbc09ff5d2474f224721'

#auth_token = '7c37ee3c85f1f39f6a72c14ec5c95236'
#client = Client(account_sid, auth_token)



app.secret_key = 'security'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sampledata'


def connection():
    try:
        conn = MySQLdb.connect(
            host = "localhost",
            user = "root",           
            password = "",
            db = "sampledata"
            )
        return conn        
    
    except Exception as e:
        return str(e)









@app.route('/')

def login():
    session['admin_logged_in'] = False
    return render_template('login.html')

@app.route('/logout')

def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/adlogin_process', methods=['POST'])
def adlogin_process():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM adlogin WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:  # Check if user is not None
            session['admin_logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))  # Redirect to login if the method is not POST



@app.route('/update_process_chapter', methods=['GET', 'POST'])
def update_process_chapter():
    if request.method == 'POST':
        to_number = request.form['to']
        body_message = request.form['body']
        
        message = client.messages.create( # type: ignore
            from_='+13257503204',
            body=body_message,
            to=to_number
        )
        
        return redirect(url_for('chapterlist', success=True, message_sid=message.sid))

    return render_template('chapterlist', success=False)



@app.route('/dashboard')

def dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    conn = connection()
    cur = conn.cursor()

    # Counting the total number of rows in the 'reports' table
    cur.execute("SELECT COUNT(*) FROM reports")
    rep = cur.fetchone()[0] or 0

    # Counting the total number of rows in the 'chapter' table
    cur.execute("SELECT COUNT(*) FROM chapter")
    chap = cur.fetchone()[0] or 0

    # Counting the total number of rows in the 'officials' table
    cur.execute("SELECT COUNT(*) FROM officials")
    off = cur.fetchone()[0] or 0

    cur.close()
    conn.close()
    
    if 'username' in session:
        username = session['username']
        return render_template('dash1.html', rep=rep, chap=chap, off=off, username = username)
    else:
        return redirect(url_for('login'))

@app.route('/report')
 
def report():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))

@app.route('/report_process', methods=['GET', 'POST'])
def report_process():
    if request.method == "POST":
        report_id = request.form['report_id']
        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        datejoin = request.form['datejoin']
        status = request.form['status']
        chapter = request.form['chapter']
        conn = connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO reports VALUES('{}' , '{}' , '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(report_id, fname, lname, gender, email, phone, datejoin, status, chapter))
        conn.commit()
    return redirect(url_for('memberlist'))


@app.route('/memberlist')

def memberlist():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    Connect = connection()
    cur = Connect.cursor()
    cur.execute("SELECT * FROM reports")
    row = cur.fetchall()	
    return render_template('member.html',  row= row)


@app.route('/delete_member/<string:report_id>/')
def delete_member(report_id):
	conn = connection()
	cur = conn.cursor()
	cur.execute("DELETE FROM reports WHERE report_id = '{}'".format(report_id))
	conn.commit()
	return redirect(url_for('memberlist'))

@app.route('/update_member/<string:report_id>/') 
def update_member(report_id):
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT *FROM reports WHERE report_id = '{}'".format(report_id))
    row = cur.fetchone()
    return render_template('updatemember.html',row = row)


@app.route('/update_process_member', methods = ['GET','POST']) 
def update_process_member():
    if request.method == "POST":
        report_id = request.form['report_id']
        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        datejoin = request.form['datejoin']
        status = request.form['status']
        chapter = request.form['chapter']
        
        conn = connection()
        cur = conn.cursor()
        cur.execute("UPDATE reports SET fname = '{}', lname = '{}', gender = '{}', email = '{}', phone = '{}', datejoin = '{}', status = '{}', chapter = '{}'  WHERE report_id = '{}'".format(fname, lname, gender, email, phone, datejoin, status,chapter, report_id))
        conn.commit()
        return redirect(url_for('memberlist'))
    
    
@app.route('/adminlist')

def adminlist():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    Connect = connection()
    cur = Connect.cursor()
    cur.execute("SELECT * FROM adlogin")
    admin = cur.fetchall()	
    return render_template('adminlist.html',  admin = admin)


@app.route('/admin_process', methods=['GET', 'POST'])
def admin_process():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    if request.method == "POST":
        admin_id = request.form['admin_id']
        username = request.form['username']
        password = request.form['password']
        conn = connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO adlogin VALUES('{}' , '{}' , '{}')".format(admin_id, username, password))
        conn.commit()
    return redirect(url_for('adminlist'))

@app.route('/addmin') 

def addmin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    
    return render_template('addmin.html')
    


@app.route('/delete_admin/<string:admin_id>/')
def delete_admin(admin_id):
	conn = connection()
	cur = conn.cursor()
	cur.execute("DELETE FROM adlogin WHERE admin_id = '{}'".format(admin_id))
	conn.commit()
	return redirect(url_for('adminlist'))

@app.route('/update_admin/<string:admin_id>/') 
def update_admin(admin_id):
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT *FROM adlogin WHERE admin_id = '{}'".format(admin_id))
    admin = cur.fetchone()
    return render_template('updateadmin.html',admin = admin)


@app.route('/update_process_admin', methods = ['GET','POST']) 
def update_process_admin():
    if request.method == "POST":
        admin_id = request.form['admin_id']
        username = request.form['username']
        password = request.form['password']
        
        conn = connection()
        cur = conn.cursor()
        cur.execute("UPDATE adlogin SET username = '{}', password = '{}' WHERE admin_id = '{}'".format(username, password, admin_id))
        conn.commit()
        return redirect(url_for('adminlist'))
    


@app.route('/officiallist')

def officiallist():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    Connect = connection()
    cur = Connect.cursor()
    cur.execute("SELECT * FROM officials")
    off = cur.fetchall()	
    return render_template('officiallist.html',  off = off)

@app.route('/archive')

def archive():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    Connect = connection()
    cur = Connect.cursor()
    cur.execute('SELECT * FROM archive')
    arc = cur.fetchall()
    return render_template('archive.html', arc = arc)


@app.route('/delete_official/<string:official_id>/')
def delete_official(official_id):
    Connect = connection()
    cur = Connect.cursor()
    cur.execute('SELECT * FROM officials WHERE official_id = %s', (official_id,))
    deleted_off = cur.fetchone()
    
    cur.execute('DELETE FROM officials WHERE official_id = %s', (official_id,))
    Connect.commit()
    cur.execute('INSERT INTO archive (fname, lname, position, age, chaptersurvived, datesurvived) VALUES (%s, %s, %s, %s, %s, %s)',
                (deleted_off[1], deleted_off[2], deleted_off[3], deleted_off[4], deleted_off[5], deleted_off[6]))
    Connect.commit()

    return redirect(url_for('officiallist'))

@app.route('/delete_arc/<string:arc_id>/')
def delete_arc(arc_id):
	conn = connection()
	cur = conn.cursor()
	cur.execute("DELETE FROM archive WHERE arc_id = '{}'".format(arc_id))
	conn.commit()
	return redirect(url_for('archive'))

@app.route('/official_process', methods=['GET', 'POST'])
def official_process():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    if request.method == "POST":
        official_id = request.form['official_id']
        fname = request.form['fname']
        lname = request.form['lname']
        position = request.form['position']
        age = request.form['age']
        chaptersurvived = request.form['chaptersurvived']
        datesurvived = request.form['datesurvived']
        
        conn = connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO officials VALUES('{}' , '{}' , '{}', '{}', '{}', '{}', '{}')".format(official_id, fname, lname, position, age, chaptersurvived, datesurvived))
        conn.commit()
    return redirect(url_for('officiallist'))

@app.route('/addofficial') 

def addofficial():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
   



@app.route('/chapterlist')

def chapterlist():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    Connect = connection()
    cur = Connect.cursor()
    cur.execute("SELECT * FROM chapter")
    chap = cur.fetchall()	
    return render_template('chapterlist.html',  chap = chap)


@app.route('/addchapter') 
 
def addchapter():
    return render_template('addchapter.html')


@app.route('/chapter_process', methods=['GET', 'POST'])
def chapter_process():
    if request.method == "POST":
        chapter_id = request.form['chapter_id']
        chapter = request.form['chapter']
        pres = request.form['pres']
        
        place = request.form['place']
        datecreated = request.form['datecreated']

        conn = connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO chapter VALUES('{}' , '{}' , '{}', '{}', '{}')".format(chapter_id, chapter,pres, place, datecreated))
        conn.commit()
    return redirect(url_for('chapterlist'))


@app.route('/delete_chapter/<string:archap_id>/')
def delete_chapter(archap_id):
	conn = connection()
	cur = conn.cursor()
	cur.execute("DELETE FROM arc_chapter WHERE archap_id = '{}'".format(archap_id))
	conn.commit()
	return redirect(url_for('chaparc'))

@app.route('/delete_chap/<string:chapter_id>/')
def delete_chap(chapter_id):
    Connect = connection()
    cur = Connect.cursor()
    cur.execute('SELECT * FROM chapter WHERE chapter_id = %s', (chapter_id,))
    deleted_off = cur.fetchone()
    
    cur.execute('DELETE FROM chapter WHERE chapter_id = %s', (chapter_id,))
    Connect.commit()
    cur.execute('INSERT INTO arc_chapter (chapname, chappres,  chapplace, chapdate) VALUES (%s, %s, %s, %s)',
                (deleted_off[1], deleted_off[2], deleted_off[3], deleted_off[4]))
    Connect.commit()

    return redirect(url_for('chapterlist'))

@app.route('/chaparc')

def chaparc():
	Connect = connection()
	cur = Connect.cursor()
	cur.execute("SELECT * FROM arc_chapter")
	chap1 = cur.fetchall()	
	return render_template('chaparc.html',  chap1 = chap1)

@app.route('/restore_chap/<string:archap_id>/')
def restore_chap(archap_id):
    Connect = connection()
    cur = Connect.cursor()
    cur.execute('SELECT * FROM arc_chapter WHERE archap_id = %s', (archap_id,))
    restore_off = cur.fetchone()
    
    cur.execute('DELETE FROM arc_chapter WHERE archap_id = %s', (archap_id,))
    Connect.commit()
    
    
    cur.execute('INSERT INTO chapter (chapter, pres, place, datecreated) VALUES (%s, %s, %s, %s)',
                (restore_off[1], restore_off[2], restore_off[3], restore_off[4]))
    Connect.commit()
    
    return redirect(url_for('chapterlist'))


############################SMS#######################################



if __name__ == '__main__':
    app.run(debug=True)