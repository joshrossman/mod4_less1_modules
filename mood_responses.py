def mood_response(mood):
    if mood.lower() == "happy":
        return "I so glad you're happy!"
    elif mood.lower() == "sad":
        return "I'm so sad that you're sad!"
    elif mood.lower() == "angry":
        return "I no! I'm sorry you're so angry. Let me know if I could help."
    elif mood.lower() == "sleepy":
        return "I hope you get some rest!"
    elif mood.lower() == "scared":
        return "I know. I hope everything is okay!"
    else:
        return "I did not understand your response! Please choose from the options listed. Have a great day!"
