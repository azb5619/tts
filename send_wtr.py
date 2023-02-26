from twilio.rest import Client 
from dotenv import load_dotenv
import os
import sys
 
# these set as environment variables
load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token) 
number = sys.argv[1]

message = client.messages.create(  
                              messaging_service_sid='MG8a3e197d48f6cbcfe4694e1906a5ec97', 
                              body='meesagge',      
                              media_url='https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/ne/GEOCOLOR/20230562316_GOES16-ABI-ne-GEOCOLOR-2400x2400.jpg',
                              to=number
                          ) 
 
print(message.sid)