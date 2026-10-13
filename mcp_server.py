#!/usr/bin/env python3
import json
import sys
from client import PersonalAgentDailyInformationDietSynthesizer

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        synth = PersonalAgentDailyInformationDietSynthesizer()
        feeds = [
            {"title": "Formal Verification of Multi-Agent Protocols", "summary": "Mathematical bounds on BFT consensus in autonomous swarms.", "source_domain": "arxiv.org", "word_count": 400, "engagement_score": 150},
            {"title": "Shocking Trick to 10x Productivity", "summary": "Click here to see miracle results.", "source_domain": "spam.com", "word_count": 200, "engagement_score": 5000},
            {"title": "Zero-Copy Data Pipelines in Python 3.12", "summary": "Memory efficiency optimizations in standard library buffers.", "source_domain": "python.org", "word_count": 300, "engagement_score": 220}
        ]
        profile = {"reading_time_budget_mins": 5.0, "interests": ["Multi-Agent", "Python"]}
        res = synth.synthesize_diet(feeds, profile)
        assert res["diet_health_verdict"] == "OPTIMAL_HIGH_SNR"
        assert res["diet_item_count"] >= 2
        print(f"[TEST PASS] Information Diet Synthesized: {res['diet_item_count']} items ({res['total_curated_time_mins']} mins)")
        sys.exit(0)

    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            if method == "initialize":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"serverInfo": {"name": "genpark-information-diet-synthesizer", "version": "1.0.0"}}}))
            elif method == "tools/list":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [{"name": "synthesize_diet", "description": "Synthesize high SNR daily information diet"}]}}))
            elif method == "tools/call":
                args = req.get("params", {}).get("arguments", {})
                synth = PersonalAgentDailyInformationDietSynthesizer()
                out = synth.synthesize_diet(args.get("feed_items", []), args.get("user_profile", {}))
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(out)}]}}))
            else:
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
