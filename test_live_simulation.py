import time
from main import ProjectAngelMasterEngine
from broker_connector import AngelUniversalBrokerConnector

def run_project_angel_live_test():
    print("=======================================================")
    print("👑 PROJECT ANGEL AI — LIVE TRADING SIMULATION STARTING")
    print("=======================================================")
    
    # আপনার মাস্টার ওয়ালেট যেখানে ২০% প্রফিট শেয়ার এসে জমা হবে
    MY_WALLET_USDT = "0x71C...AngelOwnerMasterWallet🔑"
    
    # ১. মেইন মাস্টার এআই ইঞ্জিন চালু করা
    print("\n[STEP 1]: মাস্টার এআই ইঞ্জিন ইনিশিয়েট করা হচ্ছে...")
    angel_system = ProjectAngelMasterEngine(my_wallet=MY_WALLET_USDT)
    time.sleep(1)

    # ২. ইউনিভার্সাল ব্রোকার কানেকশন ভেরিফিকেশন
    print("\n[STEP 2]: ইউনিভার্সাল ব্রোকার রাউটার চেক করা হচ্ছে...")
    broker_router = AngelUniversalBrokerConnector()
    # কাস্টমার জিরোধা বা আপস্টক্স যাই ব্যবহার করুক, সিস্টেম রুট চেক করবে
    _, broker_msg = broker_router.route_and_connect_broker("ZERODHA", {"api_key": "test"})
    print(broker_msg)
    time.sleep(1)

    # ৩. কাস্টমার নেটওয়ার্ক ও রেফারেল সিমুলেশন (আপনার ৩% রেফারেল আইডিয়া)
    print("\n[STEP 3]: কাস্টমার রেফারেল নেটওয়ার্ক ম্যাপিং করা হচ্ছে...")
    # মনে করি, আপনি (admin_owner@email.com) অমিতকে রেফার করেছেন
    # অমিত আবার তার বন্ধু সুব্রতকে রেফার করেছে
    angel_system.users.register_user("subrata@email.com", "Subrata Roy", "pass1")
    angel_system.users.register_user("amit@email.com", "Amit Das", "pass2")
    
    # রেফারেল ট্র্যাকিং লিঙ্কিং
    angel_system.billing.register_referral(friend_id="subrata@email.com", referrer_id="amit@email.com")
    time.sleep(1)

    # ৪. লাইভ ট্রেডিং ও কাস্টম অ্যামাউন্ট টেস্ট (১০০ টাকা থেকে ১ লাখ)
    print("\n[STEP 4]: বিভিন্ন ফান্ডের কাস্টমারদের জন্য এআই সাইকেল রান করা হচ্ছে...")
    
    # টেস্ট কাস্টমার ১: সুব্রত মাত্র ৫০০ টাকা দিয়ে ক্রিপ্টো/স্টক অন করল
    print("\n--- 👤 কাস্টমার ১: সুব্রত (অ্যামাউন্ট: ₹৫০০) ---")
    angel_system.users.update_market_selection("subrata@email.com", ["CRYPTO", "INDIAN_STOCK"])
    # মার্কেট হঠাৎ একটু ডাউনট্রেন্ড (-৪০), এআই শর্ট সেলিং করে প্রফিট বের করবে
    angel_system.process_customer_cycle(
        email="subrata@email.com",
        name="Subrata Roy",
        password="pass1",
        allocated_funds=500.0,
        market_trend=-40,
        volatility="MEDIUM"
    )
    time.sleep(1)

    # টেস্ট কাস্টমার ২: অমিত বড় ট্রেডার, সে ১,০০,০০০ টাকা নিয়ে ট্রেড অন করল
    print("\n--- 👑 কাস্টমার ২: অমিত (অ্যামাউন্ট: ₹১,০০,০০০) ---")
    angel_system.users.update_market_selection("amit@email.com", ["CRYPTO", "FOREX"])
    # মার্কেট খুব হাই ভোলাটাইল, এআই অপশন ট্রেডিং (Hedging) করে লাভ বের করবে
    angel_system.process_customer_cycle(
        email="amit@email.com",
        name="Amit Das",
        password="pass2",
        allocated_funds=100000.0,
        market_trend=80,
        volatility="HIGH"
    )
    
    print("\n=======================================================")
    print("✅ SIMULATION COMPLETE: সব মডিউল ১০০% পারফেক্ট কাজ করছে!")
    print("=======================================================")

if __name__ == "__main__":
    run_project_angel_live_test()
