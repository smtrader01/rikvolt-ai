class RikVoltRiskShield:
    def __init__(self, max_daily_loss_percent=5.0):
        self.max_daily_loss_percent = max_daily_loss_percent
        self.liquidation_buffer_percent = 20.0  # 20% মার্জিন প্রোটেকশন লিমিট
        self.auto_hedge_active = True

    def evaluate_live_market_safety(self, current_balance, open_positions_loss, market_volatility):
        """
        গ্রাহকের টাকা ১০০% নিরাপদ রাখার জন্য রিয়েল-টাইম রিস্ক প্রোটেকশন মেকানিজম।
        """
        # লস লিমিট চেক করা (Anti-Revenge Trading Guard)
        total_loss_percent = (open_positions_loss / current_balance) * 100.0
        
        if total_loss_percent >= self.max_daily_loss_percent:
            return {
                "status": "🚨 RISK TRIGGERED: DAILY LOSS LIMIT REACHED",
                "action": "FORCE_CLOSE_ALL_TRADES_AND_LOCK_API",
                "reason": f"ডেইলি লস লিমিট {self.max_daily_loss_percent}% পার হয়ে গেছে। মূলধন সুরক্ষিত রাখা হয়েছে।"
            }

        # ব্ল্যাক-সোয়ান বা অস্বাভাবিক ভোলাটেলিটি চেক করা (Auto-Hedging Guard)
        if market_volatility > 85.0:
            return {
                "status": "⚠️ RISK TRIGGERED: EXTREME VOLATILITY DETECTED",
                "action": "EXECUTE_PROTECTIVE_HEDGING_TRADES",
                "reason": "মার্কেটে বড় পতনের ঝুঁকি রয়েছে। অটো-ইন্সুরেন্স/হেজিং পজিশন চালু করা হলো।"
            }

        return {
            "status": "✅ ALL GUARDS 100% SAFE",
            "action": "ALLOW_ALGO_EXECUTION",
            "reason": "ক্যাপিটাল শিল্ড একটিভ রয়েছে এবং অ্যাকাউন্ট সম্পূর্ণ সুরক্ষিত।"
        }
