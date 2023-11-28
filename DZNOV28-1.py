def analyze_sentiment(text):
    positive_words = ['good', 'excellent', 'fine']
    negative_words = ['bad', 'awful', 'disgusting']

    words = text.lower().split()

    score = 0
    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"

#пример
text_to_analyze = "This Marvel movie was awful but the food was good."
result = analyze_sentiment(text_to_analyze)
print(result)
