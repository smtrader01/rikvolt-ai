import os
import sqlite3

class AngelSandboxEngine:
    def __init__(self):
        # লোকাল টেস্টিং ও রেন্ডার স্টার্টআপের জন্য SQLite ডাটাবেস ভল্ট
        self.init_database()

    def get_connection(self):
        return sqlite3.connect('local_sandbox.db')

    def init_database(self):
        """কাস্টমারদের আইসোলেটেড প্রোফাইল এবং কাস্টম AI স্ট্র্যাটেজি টেবিল তৈরি"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_profiles (
                user_id TEXT PRIMARY KEY,
                username TEXT,
                trading_mode TEXT DEFAULT 'DEMO',
                demo_balance REAL DEFAULT 10000.0,
                live_api_key TEXT,
                live_secret_key TEXT,
                custom_ai_strategy TEXT DEFAULT 'DEFAULT_ZERO_LOSS'
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("🟢 Angel AI Isolated Sandbox Database Initialized Successfully!")

    def update_user_strategy(self, user_id, new_strategy_code):
        """মেইন কোড স্পর্শ না করে শুধুমাত্র নির্দিষ্ট কাস্টমারের ভার্চুয়াল স্যান্ডবক্সে স্ট্র্যাটেজি আপডেট"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO user_profiles (user_id, custom_ai_strategy)
            VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET custom_ai_strategy = excluded.custom_ai_strategy
        """, (user_id, new_strategy_code))
        
        conn.commit()
        cursor.close()
        conn.close()
        return f"🔒 Strategy successfully isolated and loaded for User: {user_id}"

# গলোবাল ইঞ্জিন ইনিশিয়েলাইজেশন
sandbox = AngelSandboxEngine()
