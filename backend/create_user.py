from werkzeug.security import generate_password_hash
from database import db_execute

name = "Dr. Atishay"
email = "doctor@rxshield.com"
password = generate_password_hash("password123")

db_execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)", 
           (name, email, password, 'Doctor'), is_select=False)
print("✅ User Created! Login with: doctor@rxshield.com / password123")