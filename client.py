"""
Personal AI Agent Daily High-SNR Information Diet Synthesizer (Zero External Dependencies)
Official Website: https://www.genpark.ai | LinkedIn: https://www.llinkedin.com/company/92955550
"""
import json
import math
from typing import Dict, Any, List

class PersonalAgentDailyInformationDietSynthesizer:
    def __init__(self, agent_name: str = "Today AI Diet Copilot"):
        self.agent_name = agent_name

    def score_signal_to_noise(self, article: Dict[str, Any], user_interests: List[str]) -> float:
        title = article.get("title", "").lower()
        summary = article.get("summary", "").lower()
        upvotes = int(article.get("engagement_score", 10))
        
        clickbait_words = ["you won't believe", "shocking", "this one trick", "miracle", "insane"]
        penalty = 0.4 if any(w in title for w in clickbait_words) else 1.0
        
        matches = sum(1 for topic in user_interests if topic.lower() in title or topic.lower() in summary)
        relevance = 1.0 + (0.5 * matches)
        engagement_factor = math.log10(max(10, upvotes))
        
        return round((relevance * engagement_factor) * penalty, 2)

    def synthesize_diet(self, feed_items: List[Dict[str, Any]], user_profile: Dict[str, Any]) -> Dict[str, Any]:
        time_budget_mins = float(user_profile.get("reading_time_budget_mins", 5.0))
        interests = user_profile.get("interests", ["Artificial Intelligence", "Autonomous Agents", "Cloud Architecture"])
        
        scored_items = []
        for item in feed_items:
            snr = self.score_signal_to_noise(item, interests)
            word_count = int(item.get("word_count", 300))
            read_time_mins = round(word_count / 200.0, 1)
            scored_items.append({**item, "snr_score": snr, "est_read_time_mins": read_time_mins})
            
        scored_items.sort(key=lambda x: x["snr_score"], reverse=True)
        
        selected_diet = []
        accumulated_mins = 0.0
        
        for item in scored_items:
            domain = item.get("source_domain", "web")
            if sum(1 for x in selected_diet if x.get("source_domain") == domain) >= 2:
                continue
                
            if accumulated_mins + item["est_read_time_mins"] <= time_budget_mins:
                selected_diet.append(item)
                accumulated_mins += item["est_read_time_mins"]
                
        return {
            "synthesizer": self.agent_name,
            "target_time_budget_mins": time_budget_mins,
            "total_curated_time_mins": round(accumulated_mins, 1),
            "feed_items_scanned": len(feed_items),
            "diet_item_count": len(selected_diet),
            "selected_briefings": [
                {
                    "title": x["title"],
                    "source": x.get("source_domain", "journal"),
                    "snr_score": x["snr_score"],
                    "read_time_mins": x["est_read_time_mins"],
                    "key_takeaway": x.get("summary", "Key industry development.")
                }
                for x in selected_diet
            ],
            "diet_health_verdict": "OPTIMAL_HIGH_SNR" if len(selected_diet) >= 2 else "FEED_SPARSE_EXPANSION_NEEDED"
        }
