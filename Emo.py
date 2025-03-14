import random

def emoji_generator():
    emojis = [
        "😊", "😂", "😎", "🥺", "😅", "😍", "😜", "🤔", "😇", "🤩",
        "😡", "🤗", "😢", "🙃", "🥳", "😜", "😆", "🤪", "😏", "😻"
    ]
    selected_emoji = random.choice(emojis)
    print("Din tilfældige emoji er:", selected_emoji)

emoji_generator()
