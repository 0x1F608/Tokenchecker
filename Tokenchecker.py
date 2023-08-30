from urllib.request import Request, urlopen


def checktoken(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False

with open("tokens.txt", "r") as f:
    tokenslst = [line.strip() for line in f.readlines()]  # Remove newline characters
    for token in tokenslst:
        is_valid_token = checktoken(token)
        if is_valid_token:
            print(f"Token '{token}' is valid.")
        else:
            print(f"Token '{token}' is NOT valid.")
