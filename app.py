from flask import Flask, render_template, request
from get_event import event
from bot import login
from datetime import datetime
import csv

app = Flask(__name__)



accounts_file = 'accounts_details.csv'

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/w')
def working():
    return "Working"

@app.route('/attendace')
def attendace():
    accounts = list()
    # with open(accounts_file, 'r') as file:
    file = open(accounts_file, 'r')
    csvreader = csv.reader(file)
    for row in csvreader:
        # print(row)
        accounts.append(row)


    total_accounts = int(csvreader.line_num)
    print(total_accounts)

    # email = 'emi123noel@gmail.com'
    # password = 'Zoho123!'
    # event_text, all_day = event()

    res = event()

    print('ressssssssss: ', res)
    if res =="No Event":
        return res

    event_text, all_day = res[0], res[1]
    print('text:',event_text, 'allday:', all_day)

    dt = datetime.now()
    day = dt.isoweekday()
    print('Weekday is:', day)

    # attendance
    # 1 for monday 7 for sunday
    print(accounts)
    for account in accounts:
        print(account)
        email = account[0]
        password = account[1]
        if day < 6:
            print('weekday')
            if 'holiday' not in event_text and 'leave' not in event_text:
                result = login(email, password)
                print(result)
                # return result
        else:
            print('weekend') 
            if 'True' in all_day:
                result = login(email, password)
                print(result)
                # return result
        print("Attendace Marked For the account: ", email)
    
    return 'Done'

@app.route("/add_account", methods=['POST'])
def add_account():

    gmail = request.form['gmail']
    password = request.form['password']




    new_data = [gmail, password]
    
    csvfile = open(accounts_file, 'a')
    csvwriter = csv.writer(csvfile, lineterminator='\n')
    csvwriter.writerow(new_data)
    csvfile.close()
    return "Account is Added successfully!"


if __name__ == '__main__':
    app.run(debug=True)
