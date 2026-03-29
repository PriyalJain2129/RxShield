from database import db_execute
res = db_execute("SELECT NOW();")
print("Database Connection Success:", res)