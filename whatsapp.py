import pywhatkit as kit
import time
import pandas as pd

# Hardcoded DataFrame with contacts and message parameters
data = pd.DataFrame({
    'Phone': ['+201140894327', '+966538796442'],  # Replace with actual phone numbers
    'Name': ['Ahmed', 'Sara'],
    'Message': ['Hello Ahmed! This is a test message.', 'Hi Sara! Your order has been shipped.']
})

# Define sending delay between messages
send_interval = 30  # Seconds

# Iterate over the data and send messages
for index, row in data.iterrows():
    phone_number = row['Phone']
    message = row['Message']
    
    try:
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=15)
        print(f"Message sent to {phone_number}")
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")
    
    time.sleep(send_interval)