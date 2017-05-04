from twilio.rest import Client
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'some_secret'



@app.route("/")
def index():

    	return render_template("webflow.html")


@app.route("/send", methods = ['POST', 'GET'])
def send ():
    
    if request.method == 'POST':
        text_msg = request.form['message'].lower().strip()
        recipient = str(request.form['number'].strip())


    # Your Account SID from twilio.com/console
    account_sid = "AC33c81cb71e51ac79c1bc76f65b27bf7b"
    # Your Auth Token from twilio.com/console
    auth_token  = "7c375233938f4e58b9332a3969f0ba29"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to= recipient,
        from_="+442033224759",
        body=text_msg)

 
    return ('Your Message has been sent to {}'.format(recipient))




@app.route("/recieve", methods = ['POST', 'GET'])
def respond():
    resp = MessagingResponse()
    time_stamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    resp.message('I can see you {}'.format(time_stamp))

    message = request.form.get("Body") #this gets the message from the POST request
    sender = request.form.get("From")
    text_file = open("Output.txt", "a")
    text_file.write("\n{} -- {} || {}".format(time_stamp, message, sender))
    text_file.close()

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

        