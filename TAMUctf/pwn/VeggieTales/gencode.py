import base64

EPISODE_NUMBER = 13

HEADER = "b4 d0 2a a4 33 5b 24"
FOOTER = "30 5e"
EPISODE_SEP = "24"

# The data for episode 5
episode = "" 
episode += "ed 0d 34 d3 75 62 f3 6d 11 34 b6 30 53 ae a3 30 ed" 
episode += "a9 3b b2 55 1a 9c 2c 9e 74 55 23 9c 2f 68 1f 30 a4"

# Counter that increments after each episode
footer_ctr = 78

result = ""
result += HEADER
for x in range(EPISODE_NUMBER):

    # Formats the episode
    ep = episode + " " + str(hex(footer_ctr))[2:] + " " + EPISODE_SEP
    footer_ctr += 1

    result += ep

result += episode + " " + str(hex(footer_ctr))[2:] + " "
result += FOOTER

hexBytes = bytes.fromhex(result)
print(base64.b64encode(hexBytes).decode('utf-8'))