from billing_manager import AngelBillingManager

class AngelBillingBridge:
    def __init__(self, my_wallet_address):
        # আপনার মেইন বিলing ইঞ্জিন সক্রিয় করা হচ্ছে
        self.billing_engine = AngelBillingManager(admin_wallet_address=my_wallet_address)

    def get_dashboard_billing_data(self, user_id, user_name):
        """
        এই মেথডটি জাভাস্ক্রিপ্ট বা ফ্রন্টএন্ডের জন্য কাস্টমারের লাইভ আর্নিং ও রেফারেল ডেটা গুছিয়ে পাঠাবে
        """
        user_record = self.billing_engine.user_billing_ledger.get(user_id, {
            "total_earned": 0.0,
            "commission_paid": 0.0,
            "referral_rewards_earned": 0.0
        })
        
        # ফ্রন্টএন্ডে দেখানোর জন্য ডেটা ফরম্যাট করা
        return {
            "user_id": user_id,
            "user_name": user_name,
            "display_total_profit": f"₹{user_record['total_earned']:.2f}",
            "display_referral_rewards": f"₹{user_record['referral_rewards_earned']:.2f}",
            "wallet_status": "INSTANT_ROUTING_ACTIVE"
        }

# লোকাল টেস্টিং
if __name__ == "__main__":
    MY_WALLET = "0xAngelMasterWalletAddressUSDT🔑"
    bridge = AngelBillingBridge(my_wallet_address=MY_WALLET)
    
    # ১. টেস্ট করার জন্য প্রথমে ব্যাকএন্ডে একটি রেফারেল ও প্রফিট ডেটা জেনারেট করি
    bridge.billing_engine.register_referral(friend_id="amit@email.com", referrer_id="rahul@email.com")
    bridge.billing_engine.track_trade_result(user_id="amit@email.com", user_name="Amit Das", profit_amount=5000.0)
    
    # ২. এবার ব্রিজ ফাইলটি কীভাবে ড্যাশবোর্ডের জন্য ডেটা রেডি করে তা দেখি
    rahul_ui_data = bridge.get_dashboard_billing_data(user_id="rahul@email.com", user_name="Rahul K.")
    print("\n📊 [FRONTEND BRIDGE DATA]: ড্যাশবোর্ডে পাঠানোর জন্য রেডি ডেটা:")
    print(rahul_ui_data)
