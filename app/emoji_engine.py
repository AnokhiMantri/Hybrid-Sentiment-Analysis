# Emoji Sentiment Scoring Engine

# Strong Positive Emojis
strong_positive = ["😍", "🔥", "🥰", "🤩", "💖", "💯"]

# Mild Positive Emojis
mild_positive = ["😊", "🙂", "👍", "😁"]

# Neutral Emojis
neutral_emojis = ["😐", "😶", "🤔"]

# Mild Negative Emojis
mild_negative = ["😕", "😔", "😞"]

# Strong Negative Emojis
strong_negative = ["😡", "😭", "💔", "😠"]


def calculate_emoji_score(text):
    score = 0
    emoji_count = 0

    for char in text:
        if char in strong_positive:
            score += 2
            emoji_count += 1
        elif char in mild_positive:
            score += 1
            emoji_count += 1
        elif char in neutral_emojis:
            emoji_count += 1
        elif char in mild_negative:
            score -= 1
            emoji_count += 1
        elif char in strong_negative:
            score -= 2
            emoji_count += 1

    return score, emoji_count
