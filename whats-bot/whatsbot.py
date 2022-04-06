from flask import Flask
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse
  
  
app = Flask(__name__)
  
@app.route("/", methods=["POST"])
  
# Logic for bot
def whatsappbot():
  
    # user input
    user_msg = request.values.get('Body', '').lower()
  
    # creating object of MessagingResponse
    response = MessagingResponse()
  
    # User search
    q = user_msg + "geeksforgeeks.org"
  
    # list
    result = []
  
    # searching urls
    for i in search(q, tld='co.in', num=6, stop=6, pause=2):
        result.append(i)
  
    # show output
    msg = response.message(f"--- Result for '{user_msg}' are  ---")
  
    msg = response.message(result[0])
    msg = response.message(result[1])
    msg = response.message(result[2])
    msg = response.message(result[3])
    msg = response.message(result[4])
  
    return str(response)
  
  
if __name__ == "__main__":
    app.run()