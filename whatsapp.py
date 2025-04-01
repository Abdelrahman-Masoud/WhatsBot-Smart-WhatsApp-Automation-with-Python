import pandas as pd
import time
import pywhatkit as kit

# Load contact data from Excel
file_path = r"C:\Users\aaf88\OneDrive\Documents\whatsapp.xlsx"
df = pd.read_excel(file_path)

def get_message(name, gender, msg_type):
    """Returns the appropriate Eid greeting message."""
    if gender == "male" and msg_type == "formal":
        return f"السلام عليكم {name}\nكل سنة وحضرتك طيب وربنا يعيده عليك وعلى اسرتك بكل خير يارب ❤️"
    elif gender == "male" and msg_type == "friendly":
        return f"حبيبى {name}\nكل سنة وانت طيب يا صديقى وربنا يعيده عليك وعلى حبايبك بكل خير يارب ❤️"
    elif gender == "female" and msg_type == "formal":
        return f"السلام عليكم {name}\nكل سنة وحضرتك طيبة وربنا يعيده عليكي وعلى اسرتك بكل خير يارب ❤️"
    elif gender == "female" and msg_type == "friendly":
        return f"حبيبتى {name}\nكل سنة وانتي طيبة وربنا يعيده عليكي وعلى حبايبك بكل خير يارب ❤️"
    else:
        return ""

# Loop through each contact and send a personalized message
for index, row in df.iterrows():
    phone_number = row["Phone"]  # Assuming the first column is named 'Phone'
    name = row["Name"]  # Second column: 'Name'
    gender = row["Gender"].strip().lower()  # Third column: 'Gender'
    msg_type = row["Message Type"].strip().lower()  # Fourth column: 'Message Type'
    
    message = get_message(name, gender, msg_type)
    
    if message:
        kit.sendwhatmsg_instantly(f"+{phone_number}", message, wait_time=10)
        time.sleep(5)  # Small delay to avoid blocking
    else:
        print(f"Skipping {name}: Invalid gender or message type")

print("All messages sent successfully!")
