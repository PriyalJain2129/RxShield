import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

# Load local .env file (for local development only)
load_dotenv()

# 🔥 THE FIX: Get the URL from the environment variable
# If not found (locally), it falls back to your string for now
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_6bHre5oCdTfq@ep-broad-cherry-a13boule-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require")

def db_execute(query, vars=None, is_select=True):
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        # RealDictCursor is great - it keeps your frontend keys working perfectly
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, vars)
            if is_select:
                return cur.fetchall()
            conn.commit()
            return None
    except Exception as e:
        print(f"❌ Database Error: {e}")
        return [] if is_select else None
    finally:
        if conn:
            conn.close()