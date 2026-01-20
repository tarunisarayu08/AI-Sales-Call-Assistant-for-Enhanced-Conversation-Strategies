def generate_summary(call_data):
    """Generate professional post-call summary"""
    transcript = call_data.get('transcript', [])
    sentiment_history = [item['sentiment'] for item in transcript]
    
    summary = {
        "call_duration": len(transcript),
        "avg_sentiment": max(set(sentiment_history), key=sentiment_history.count),
        "key_moments": [],
        "recommendations": call_data.get('recommendations', []),
        "action_items": [
            "Follow up with pricing details",
            "Send case studies for similar clients",
            "Schedule technical demo"
        ],
        "sentiment_trend": "Improving" if sentiment_history[-3:].count('POSITIVE') > 1 else "Needs attention"
    }
    
    # Key moments extraction
    for i, moment in enumerate(transcript[-5:]):
        if moment['sentiment'] == 'POSITIVE':
            summary['key_moments'].append(f"Moment {i+1}: {moment['text'][:100]}...")
    
    return summary
