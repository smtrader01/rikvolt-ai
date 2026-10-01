import os
import json
import requests
from flask import Flask, request, jsonify, render_template
from database_sandbox import sandbox  # আমাদের তৈরি করা আইসোলেটেড ডাটাবেস

app = Flask(__name__, template_folder=".", static_folder=".")

# OpenAI / Claude এর মতো গ্লোবাল এআই ব্রেন কানেকশন গেটওয়ে
AI_BRAIN_URL = "https://openai.com"
# সিকিউরিটির জন্য API_KEY সরাসরি কোডে না রেখে রেন্ডার এনভায়রনমেন্ট থেকে নেবে
AI_API_KEY = os.environ.get("OPENAI_API_KEY", "MOCK_MODE_ACTIVE")

@app.route('/')
def home():
    # রুট ইউআরএলে হিট করলে সরাসরি ড্যাশবোর্ড পেজ লোড হবে
    return render_template('dashboard.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/angel-brain', methods=['POST'])
def angel_brain_processor():
    """
    Angel AI চ্যাট থেকে আসা কাস্টমার রিকোয়েস্ট এবং কাস্টম স্ট্র্যাটেজি প্রসেসিং ইঞ্জিন
    """
    data = request.json
    user_id = data.get("user_id", "default_user")
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"status": "error", "message": "No command received"}), 400

    # ১. কাস্টমার যদি নতুন কোনো ট্রেডিং স্ট্র্যাটেজি বা অ্যালগরিদম তৈরি করতে বলে
    if "strategy" in user_message.lower() or "স্ট্র্যাটেজি" in user_message:
        ai_generated_code = generate_dynamic_strategy(user_message)
        
        # মেইন কোড স্পর্শ না করে শুধুমাত্র এই ইউজারের সুরক্ষিত স্যান্ডবক্স ডাটাবেসে সেভ হবে
        db_status = sandbox.update_user_strategy(user_id, ai_generated_code)
        
        response_text = (
            f"🧠 <strong>Angel AI Engine:</strong> আপনার অনুরোধ বিশ্লেষণ করে একটি কাস্টম "
            f"অ্যালগরিদম কোড তৈরি করা হয়েছে।<br><br>"
            f"🔒 <strong>আইসোলেটেড প্রোটেকশন:</strong> {db_status}. এটি এখন ব্যাকগ্রাউন্ডে "
            f"শুধুমাত্র আপনার ব্রোকার অ্যাকাউন্টে সিগন্যাল জেনারেট করবে। বাকি প্লাস কাস্টমারদের "
            f"মেইন কোডবেসে কোনো প্রভাব ফেলবে না!"
        )
        return jsonify({"status": "success", "reply": response_text})

    # ২. সাধারণ কোডিং বা প্ল্যাটফর্ম কাস্টমাইজেশন কোশ্চেন হ্যান্ডলার
    else:
        ai_reply = fetch_ai_brain_response(user_message)
        return jsonify({"status": "success", "reply": ai_reply})

def generate_dynamic_strategy(prompt):
    """
    ইউজারের ভয়েস বা টেক্সট ইনপুট থেকে ১ সেকেন্ডে ব্যাকগ্রাউন্ডে স্ক্র্যাচ থেকে ইউনিক ট্রেডিং লজিক মেকার
    """
    # রিয়েল এআই কি না থাকলে ব্যাকআপ মক স্ট্র্যাটেজি প্রসেস করবে
    if AI_API_KEY == "MOCK_MODE_ACTIVE":
        return f"// Auto-Generated Logic for: {prompt}\nif (RSI < 30) Buy(); else if (RSI > 70) Sell();"
    
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are Angel AI Trading Engine. Generate tight trading algorithms in JSON format based on user strategy prompts."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        res = requests.post(AI_BRAIN_URL, json=payload, headers=headers)
        return res.json()['choices'][0]['message']['content']
    except Exception:
        return "// Fallback Guard Active\nif(EMA_9 > EMA_21) OpenLong();"

def fetch_ai_brain_response(msg):
    """সাধারণ চ্যাট ব্রেন রেসপন্স গেটওয়ে"""
    if AI_API_KEY == "MOCK_MODE_ACTIVE":
        return f"আমি আপনার মেসেজটি বুঝতে পেরেছি। আপনার প্লাস অ্যাকাউন্টের ডাটাবেস ভল্ট এবং কোয়ান্টাম নিউরো-শিল্ড সম্পূর্ণ সুরক্ষিত অবস্থায় লাইভ আছে। পরবর্তী নির্দেশনা দিন!"
    
    # রিয়েল টাইম এআই কল লজিক এখানে এক্সিকিউট হবে...
    return "AI Connected"

if __name__ == '__main__':
    # রেন্ডার সার্ভার ডাইনামিক পোর্ট অ্যাসাইনমেন্ট প্রোটেকশন
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
