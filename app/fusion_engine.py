import numpy as np

def hybrid_prediction(text_probs, emoji_score):
    """
    text_probs = array of probabilities from ML model
    emoji_score = score from emoji engine
    """

    # Copy probabilities
    adjusted_probs = text_probs.copy()

    # Weight factor (small so it doesn't overpower text model)
    weight = 0.05

    # Assuming order: [negative, neutral, positive]
    if emoji_score > 1:
        adjusted_probs[2] += abs(emoji_score) * weight
    elif emoji_score < -1:
        adjusted_probs[0] += abs(emoji_score) * weight
    else:
        adjusted_probs[1] += 0.01  # slight neutral boost

    # Normalize probabilities
    adjusted_probs = adjusted_probs / np.sum(adjusted_probs)

    final_index = np.argmax(adjusted_probs)

    labels = ["negative", "neutral", "positive"]

    return labels[final_index], adjusted_probs
