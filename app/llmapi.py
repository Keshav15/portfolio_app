from poe_api_wrapper import Poe
from poe_api_wrapper import PoeApi
import json
import re
from app.createRepo import createrepo
token = "-AWr3euMgNBkIZzqFvykXw%3D%3D"

client = PoeApi(token)
with open("app/configtemplate.json", "r") as configfile:
    config_data = json.load(configfile)

def formatdata(resumedata):
    bot = "chinchilla"
    message = f"This is my resume data {resumedata} and I want this data to be in this json format {config_data} and just plese give me this as json data seperately and send it like json''' ''' in this way.. and plese dont add some extra text in it"

    # Create new chat thread
    # Streamed example:

    for chunk in client.send_message(bot, message):
        pass
    newconfigfile = chunk["text"]
    json_pattern = r'```json(.*?)```'
    json_matches = re.findall(json_pattern, newconfigfile, re.DOTALL)

    # If there are multiple matches, you can choose the first one or iterate through them
    if json_matches:
        json_data = json_matches[0].strip()  # Choose the first match
        # Parse the JSON data
        try:
            
            json_obj = json.loads(json_data)
            name=json_obj['name']
            # Save the formatted JSON to config_file.json and overwrite it
            with open("app/config_file.json", "w") as jsonfile:
                json.dump(json_obj, jsonfile, indent=2)
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
    else:
        print("No JSON data found in the text.")
    
    finallink=createrepo(name)
    return finallink

# Poe.chat_with_bot(token)
