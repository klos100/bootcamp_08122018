import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
nothing = "8022"

while True:
    x_url = url.format(nothing)
    resp = requests.get(x_url)
    print(x_url)
    try:

        nothing = int(resp.text.split()[-1])
    except ValueError:
        print(resp.text)
        break

# resp.content
# resp.text
#
# resp.text.split()[-1]