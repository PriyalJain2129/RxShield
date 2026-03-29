from werkzeug.security import generate_password_hash
from database import db_execute

# Clear existing test users to avoid "Already Exists" errors
db_execute("DELETE FROM users WHERE email = 'doctor@rxshield.com'", is_select=False)

# Create the fresh doctor account
name = "Dr. Atishay"
email = "doctor@rxshield.com"
password = generate_password_hash("password123")

db_execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)", 
           (name, email, password, 'Doctor'), is_select=False)

print("✅ SUCCESS: User 'doctor@rxshield.com' with password 'password123' is now in Neon!")