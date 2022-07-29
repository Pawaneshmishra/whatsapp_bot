from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from dateutil.parser import parse
from gsheet_func import *


app = Flask(__name__)
count=0
@app.route('/sms', methods=['POST'])


def reply():

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    message=response.message()
    responded=False
    words=incoming_msg.split('@')

    if 'hello' or 'hi' or 'Hi' or 'Hello' in incoming_msg:
        reply = "Hello! \nDo you want to set a remainder? "
        message.body(reply)
        responded=True
    
    if len(words) == 1 and 'yes' or 'Yes' in incoming_msg:
        remainder_string = "Please provide the date and time in the following format. \n"
        "*Date @* _type the date_"
        message.body(remainder_string)
        responded=True

    if len(words) == 1 and 'no' or 'No' in incoming_msg:
        reply = "Thank you for using the remainder service. \n"
        message.body(reply)
        responded=True

    elif len(words) != 1:
        input_type = words[0].strip().lower()
        input_string = words[1].strip()
        if input_type == 'date':
            reply = "Please enter the remaining message in the following format. \n" 
            "*Remainder @* _type the message_"
            set_remainder_date(input_string)
            message.body(reply)
            responded=True

        if input_type == 'remainder':
            reply="Your remainder has been set. \n"
            set_remainder_body(input_string)
            message.body(reply)
            responded=True

    if not responded:
        message.body('Incorrect format. Please enter the following format. \n')

    return str(response)


def set_remainder_date(msg):
    p = parse(msg)
    date = p.strftime('%d%m%Y')
    save_remainder_date(date)
    return 0


def set_remainder_body(msg):
    save_remainder_body(msg)
    return 0    
    

if __name__ == '__main__':
    app.run(debug=True)