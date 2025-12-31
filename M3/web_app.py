from flask import Flask, request, jsonify,render_template,redirect
import sqlite3
from datetime import datetime
from flask import Flask ,render_template,request,jsonify,session
from flask import Flask, url_for, request
from Chatbot_Process import chat_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Helper function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('./chatbot.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    if 'user_id' in session:
        # conn = get_db_connection()
        # cursor = conn.cursor()
        # cursor.execute('SELECT username FROM users WHERE id = ?', (session['user_id'],))
        # user = cursor.fetchone()
        # print(user)
        # username = user['username']
        # return render_template('home.html',username=username)
        return redirect(url_for('chatbot'))
    
    return render_template('cht.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.json
        username = data['username']
        # username = request.form['username']
        email = data['email']
        password = data['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        ''', (username, email, password))
        conn.commit()
        conn.close()

        # return jsonify({'message': 'User added successfully.'}), 201
        # return jsonify({
        #     'message': 'Data received successfully.',
        # }), 200
        return jsonify({'status': 'success'})
    except:
        return jsonify({'status': 'failed'})

def validate(username,password):
     
    con=get_db_connection()
    completion = False
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()
        for row in rows:
            dbuser = row[1]
            # print(dbuser)
            dbpass = row[3]
            # print(dbpass)
            if dbuser == username:
                completion = (dbpass == password)
                print(completion,username)
                
    return completion,username
@app.route('/login', methods=['GET', 'POST'])
def login():

    data = request.json
    username = data['username']
    password = data['password']

    completion,username = validate(username,password)
    print(completion,username)
    if completion == False:
        error = 'invalid Credentials. please try again.'
        print(error)
    else:
        # session['username'] = request.form['username']
        # return render_template('home.html')
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        print(user)
        session['user_id'] = user['id']
        print(session['user_id'])
        print("login success")

        return jsonify({'status': 'success','username':username})
        # return render_template('index.html', username=username)
    # return render_template('index.html', error=error)
    return jsonify({'status': 'failed'})



@app.route('/add_question', methods=['POST'])
def add_question():
    data = request.json

    question = str(data['question'])
    print("question___________",question)
    # answer = data.get('answer', '')
    datetime_now = str(datetime.now().isoformat())

    conn = get_db_connection()
    cursor = conn.cursor()


    # cursor.execute(f'SELECT id FROM users WHERE username = {username}')
    # cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
    # user = cursor.fetchone()
    # print(user)
    # user_id = user['id']
    user_id=session['user_id']
    print("session________id",session['user_id'])


    answer=chat_response(question)
    
    # print("user___________id",user_id)
    cursor.execute('''
        INSERT INTO questions (user_id, datetime, question,answer)
        VALUES (?, ?, ?, ?)
    ''', (user_id, datetime_now, question,answer))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Question added successfully.','answer':answer}), 201




@app.route('/get_users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()

    return jsonify([dict(user) for user in users])

@app.route('/chatbot', methods=['GET'])
def chatbot():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM users WHERE id = ?', (session['user_id'],))
    user = cursor.fetchone()
    cursor.execute('SELECT question, answer FROM questions WHERE user_id = ? ORDER BY id DESC LIMIT 10', (session['user_id'],))
    questionswithanswers = cursor.fetchall()
    # print(user)
    l=[dict(question) for question in questionswithanswers]
    que=[]
    ans=[]
    for i in l[::-1]:
        # print(i['question'])
        que.append(i['question'])
        print(i['answer'])
        ans.append(i['answer'])

    username = user['username']
    cursor.execute('SELECT datetime	 FROM questions WHERE user_id = ? ORDER BY id ', (session['user_id'],))
    date_time = cursor.fetchall()

    l_date=[dict(date) for date in date_time]
    date_t=[]
    for i in l_date[::-1]:
        if i['datetime'][:10] not in date_t:
            print(i['datetime'][:10])
            date_t.append(i['datetime'][:10])
    print(date_t)
    return render_template('home.html',username=username,date_t=date_t)


@app.route('/get_questions/<int:user_id>', methods=['GET'])
def get_questions(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM questions WHERE user_id = ?', (user_id,))
    questions = cursor.fetchall()
    conn.close()

    return jsonify([dict(question) for question in questions])

@app.route('/view_table/<table_name>', methods=['GET'])
def view_table(table_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Get table schema
        cursor.execute(f"PRAGMA table_info({table_name})")
        schema = cursor.fetchall()

        # Get table data
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()

        conn.close()

        return jsonify({
            'schema': [dict(row) for row in schema],
            'data': [dict(row) for row in data]
        })
    except sqlite3.OperationalError:
        conn.close()
        return jsonify({'error': 'Table not found.'}), 404

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))
    # print("session_______id",session['user_id'])
    # return render_template('cht.html')

# @app.route('/get_date')
# def get_date():
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     cursor.execute('SELECT datetime	 FROM questions WHERE user_id = ? ORDER BY id ', (session['user_id'],))
#     date_time = cursor.fetchall()

#     l_date=[dict(date) for date in date_time]
#     date_t=[]
#     for i in l_date:
#         if i['datetime'][:10] not in date_t:
#             print(i['datetime'][:10])
#             date_t.append(i['datetime'][:10])
#     print(date_t)
#     return redirect(url_for('chatbot'))

@app.route('/show_history',  methods=['POST'])
def show_history():
    data = request.json

    dt = str(data['date'])
    # dt="2024-08-12"
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM questions WHERE user_id = ? ORDER BY id ', (session['user_id'],))
    all_data = cursor.fetchall()

    l_date=[dict(data) for data in all_data]

    qn=[]
    an=[]
    for i in l_date:
        if i['datetime'][:10] == dt:
            # print(i['datetime'][:10])
            qn.append(i['question'])
            an.append(i['answer'])
    # print(qn,an)
    return jsonify({'status': 'success', 'question':qn ,'answer':an})
    # return jsonify({'status': 'success','username':username})



if __name__ == '__main__':
    app.run(debug=True)
