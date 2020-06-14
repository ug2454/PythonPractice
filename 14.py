def emoji_converter(message):
    words = enter.split(' ')

    emojis = {
        ":)": "😊",
        ":(": "☹"
    }

    output = ""
    for w in words:
        output = output + emojis.get(w, w) + " "

    return output


enter = input('>')
print(emoji_converter(enter))
