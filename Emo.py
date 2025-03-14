import random

def emoji_generator():
    emojis = [
        "😊", "😂", "😎", "🥺", "😅", "😍", "😜", "🤔", "😇", "🤩",
        "😡", "🤗", "😢", "🙃", "🥳", "😜", "😆", "🤪", "😏", "😻"
    ]
    selected_emoji = random.choice(emojis)
    print("Your random emoji is:", selected_emoji)

emoji_generator()
