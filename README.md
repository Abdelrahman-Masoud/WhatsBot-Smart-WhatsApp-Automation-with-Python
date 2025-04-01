# 🚀 WhatsApp Message Automation Bot

Automate personalized WhatsApp messages using Python and an Excel sheet! 🎯

## 📌 Features
- Reads contacts from an Excel file 📂
- Personalizes messages based on **name, gender, and message type (formal/friendly)**
- Sends messages via WhatsApp automatically 🟢
- Supports Arabic messages for **Eid greetings** 🎉

## 📄 Excel File Format
Your Excel file should have **4 columns**:

| Column Name | Description |
|------------|-------------|
| `Number` | WhatsApp phone number (with country code) |
| `Name` | Recipient's name |
| `Gender` | `male` or `female` |
| `Message Type` | `formal` or `friendly` |

## 📨 Message Formats
- **Male & Formal:**
  > السلام عليكم `name`
  > كل سنة وحضرتك طيب وربنا يعيده عليك وعلى اسرتك بكل خير يارب ❤️

- **Male & Friendly:**
  > حبيبي `name`
  > كل سنة وانت طيب يا صديقي وربنا يعيده عليك وعلى حبايبك بكل خير يارب ❤️

- **Female & Formal:**
  > السلام عليكم `name`
  > كل سنة وحضرتك طيبة وربنا يعيده عليكي وعلى اسرتك بكل خير يارب ❤️

- **Female & Friendly:**
  > حبيبتي `name`
  > كل سنة وانتي طيبة يا صديقتي وربنا يعيده عليكي وعلى حبايبك بكل خير يارب ❤️

## 🚀 How to Use
1. Install the required libraries:
   ```bash
   pip install pandas pywhatkit
   ```
2. Prepare your Excel sheet with the correct format.
3. Run the script:
   ```bash
   python whatsapp_sender.py
   ```
4. The script will open WhatsApp Web and send messages automatically.

## ⚠️ Notes
- Make sure your WhatsApp Web is logged in.
- Keep the Excel sheet updated with valid phone numbers.
- Avoid spamming to prevent WhatsApp from blocking your number.

---
📩 **Contributions are welcome!** Feel free to submit issues or PRs. 🚀
