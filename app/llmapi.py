from poe_api_wrapper import Poe
from poe_api_wrapper import PoeApi
import json
import re
token = "-AWr3euMgNBkIZzqFvykXw%3D%3D"


client = PoeApi(token)
with open("/home/keshav/Desktop/portfolio_app/app/configtemplate.json","r") as configfile:
    config_data=json.load(configfile)


def formatdata(resumedata):
    bot = "chinchilla"
    message = f"This is my resume data {resumedata} and I want this data to be in this json format {config_data}"

        # Create new chat thread
        # Streamed example:
    
    for chunk in client.send_message(bot, message):
        pass
    newconfigfile=chunk["text"]
    json_pattern = r'```json(.*?)```'
    json_matches = re.findall(json_pattern,newconfigfile, re.DOTALL)

    # If there are multiple matches, you can choose the first one or iterate through them
    if json_matches:
        json_data = json_matches[0].strip()  # Choose the first match
        # Parse the JSON data
        try:
            json_obj = json.loads(json_data)
            print(json.dumps(json_obj, indent=2))  # Print the formatted JSON
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
    else:
        print("No JSON data found in the text.")
    return chunk["text"]



# Poe.chat_with_bot(token)


