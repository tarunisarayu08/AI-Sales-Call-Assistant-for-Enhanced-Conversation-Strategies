class PromptGenerator:
    def __init__(self):
        self.objection_handlers = {
            "price": [
                "What would be your ideal budget for this solution?",
                "Let me show you the ROI that justifies this investment",
                "We have flexible payment options available"
            ],
            "time": [
                "How soon do you need this implemented?",
                "We can start with a pilot to show quick wins",
                "What's your timeline for this project?"
            ],
            "competition": [
                "What specifically do you like about their offering?",
                "Let me highlight our unique advantages",
                "Would you be open to a side-by-side comparison?"
            ]
        }
    
    def generate_prompts(self, sentiment, text):
        """Generate context-aware prompts"""
        prompts = []
        
        # Sentiment-based prompts
        if sentiment == 'NEGATIVE':
            prompts.append("Acknowledge their concern: 'I understand your hesitation...'")
            # Detect objection type
            text_lower = text.lower()
            for objection, responses in self.objection_handlers.items():
                if objection in text_lower:
                    prompts.append(f"Handle objection: {responses[0]}")
                    break
        
        elif sentiment == 'NEUTRAL':
            prompts.append("Ask open-ended question: 'What are your main goals for this year?'")
        
        elif sentiment == 'POSITIVE':
            prompts.append("Build momentum: 'Sounds like this aligns perfectly with your goals!'")
            prompts.append("Close: 'Shall we proceed with the next steps?'")
        
        return prompts[:3]
