from client import PersonalAgentDailyInformationDietSynthesizer

def main():
    synth = PersonalAgentDailyInformationDietSynthesizer()
    feed = [
        {"title": "State of Agentic AI 2026", "summary": "Comprehensive survey on production agent deployments.", "source_domain": "ai-index.org", "word_count": 500, "engagement_score": 850},
        {"title": "Cloud FinOps: Cost Governance Patterns", "summary": "Architectural guide to token quota management.", "source_domain": "cloud-patterns.io", "word_count": 400, "engagement_score": 340}
    ]
    user = {"reading_time_budget_mins": 6.0, "interests": ["Agentic AI", "Cloud"]}
    diet = synth.synthesize_diet(feed, user)
    print(f"--- Daily Information Diet ({diet['total_curated_time_mins']} / {diet['target_time_budget_mins']} mins) ---")
    for item in diet['selected_briefings']:
        print(f"* [{item['source']}] {item['title']} (SNR: {item['snr_score']})")
        print(f"  Takeaway: {item['key_takeaway']}")

if __name__ == "__main__":
    main()
