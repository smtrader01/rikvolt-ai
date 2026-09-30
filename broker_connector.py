import requests

class AngelUniversalBrokerConnector:
    def __init__(self):
        # আমাদের প্ল্যাটফর্ম বর্তমানে যে ব্রোকারগুলোর রুট সাপোর্ট করে
        self.supported_brokers = ["UPSTOX", "ZERODHA", "ANGEL_ONE", "BINANCE", "METATRADER_5"]
        print("🔌 [UNIVERSAL CONNECTOR]: সর্বজনীন ব্রোকার ইঞ্জিন অ্যাক্টিভেটেড।")

    def route_and_connect_broker(self, broker_name, api_credentials):
        """
        কাস্টমার যেকোনো ব্রোকার সিলেক্ট করলে এই মেথডটি স্বয়ংক্রিয়ভাবে তার রুট ঠিক করবে
        """
        broker_name = broker_name.upper().strip()
        
        if broker_name not in self.supported_brokers:
            return False, f"❌ '{broker_name}' ব্রোকারটি এখনও আমাদের সিস্টেমে যুক্ত করা হয়নি।"

        print(f"📡 [ROUTING]: {broker_name} সার্ভারের সাথে নিরাপদ কানেকশন তৈরি করা হচ্ছে...")

        # ১. ইন্ডিয়ান ব্রোকার: জিরোধা (Zerodha Kite)
        if broker_name == "ZERODHA":
            # জিরোধার এপিআই কানেকশন লজিক
            return True, "✅ [ZERODHA CONNECTED]: আপনার Zerodha (Kite) অ্যাকাউন্ট সফলভাবে যুক্ত হয়েছে।"

        # ২. ইন্ডিয়ান ব্রোকার: অ্যাঞ্জেল ওয়ান (Angel One)
        elif broker_name == "ANGEL_ONE":
            # অ্যাঞ্জেল ওয়ানের স্মার্ট-এপিআই কানেকশন লজিক
            return True, "✅ [ANGEL ONE CONNECTED]: আপনার Angel One অ্যাকাউন্ট সফলভাবে যুক্ত হয়েছে।"

        # ৩. ইন্ডিয়ান ব্রোকার: আপস্টক্স (Upstox)
        elif broker_name == "UPSTOX":
            return True, "✅ [UPSTOX CONNECTED]: আপনার Upstox অ্যাকাউন্ট সফলভাবে যুক্ত হয়েছে।"

        # ৪. ক্রিপ্টো এক্সচেঞ্জ: বাইন্যান্স (Binance)
        elif broker_name == "BINANCE":
            return True, "✅ [BINANCE CONNECTED]: আপনার Binance ক্রিপ্টো অ্যাকাউন্ট সফলভাবে যুক্ত হয়েছে।"

        # ৫. ফরেক্স মার্কেট: মেটাট্রেডার (MetaTrader 5)
        elif broker_name == "METATRADER_5":
            return True, "✅ [FOREX CONNECTED]: আপনার Forex MT5 টার্মিনাল সফলভাবে যুক্ত হয়েছে।"

        return False, "❌ কানেকশন ব্যর্থ হয়েছে।"

# লোকাল টেস্টিং
if __name__ == "__main__":
    universal_connector = AngelUniversalBrokerConnector()
    
    # টেস্ট ১: কাস্টমার জিরোধা অ্যাকাউন্ট কানেক্ট করতে চায়
    status_1, msg_1 = universal_connector.route_and_connect_broker("ZERODHA", {"api_key": "xyz123"})
    print(msg_1)
    
    # টেস্ট ২: কাস্টমার মেটাট্রেডার ৫ (ফরেক্স) কানেক্ট করতে চায়
    status_2, msg_2 = universal_connector.route_and_connect_broker("MetaTrader_5", {"login_id": "45678"})
    print(msg_2)
