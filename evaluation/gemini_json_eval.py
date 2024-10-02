import base64
import os
import json

import numpy as np
import time
import openai
from openai import OpenAI
import anthropic
import re
# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key

genai.configure(api_key="xxxxxxxxx")



# print(response.text)


# exit()


def image_encoding(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def preprocess(str1):
    while str1[0] != "{":
        str1 = str1[1:]
    while str1[-1] != "}":
        str1 = str1[:-1]
    str2 = str1.replace("\\", "")
    str2 = str2.replace("\\n", "\n")
    return str2

import json
import re

def extract_json(response):
    # Find the start and end of the JSON object
    json_start = response.find("{")
    json_end = response.rfind("}")
    
    if json_start == -1 or json_end == -1:
        raise ValueError("No valid JSON object found in the response")
    
    # Extract the JSON substring
    json_str = response[json_start:json_end + 1]
    
    # Remove any invalid control characters
    json_str = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', json_str)
    
    # Parse the cleaned JSON string
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {str(e)}")
        print(f"Problematic JSON string: {json_str}")
        raise


def transfer(str1):
    if "\u03c0" in str1:
        strs = str1.split('\u03c0')
        str1 = strs[0]
        return float(str1) * np.pi
    else:
        return float(str1)


guide = """
### Response Format
Answer Instruction Please provide an answer to the question outlined above. Your response should adhere to the following JSON format, which includes two keys: 'solution' and 'short answer'. 
# The 'solution' key can contain reasoning steps needed to solve the question.
# The 'short answer' key should only provide a concise response. If the problem is a multiple choice problem, just provide the corresponing choice option, 
such as 'A', 'B', 'C', or 'D'. If the answer is a numerical value, format it as a three-digit floating-point number.  

Example of expected JSON response format:

"""

example = {
    "solution": "[Detailed step-by-step explanation]",
    "short answer": "[Concise Answer]"
}
text_example = json.dumps(example, indent=4)

data = {}
count = 0
client = anthropic.Anthropic()
image_media_type = "image/png"
start = time.time()

for trial in range(0, 1):
    data = {}
    count = 0
    folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")

    with open(f'{folder}dataset.json') as file:
        json_dict = json.load(file)

    for i in range(1, 502):
        print(f"working on trial {trial} problem {i}")
        temp = i
        text = "## Question\n" + json_dict.get(f"{temp}").get('question')
        if json_dict.get(f"{temp}").get("answer_type") == "float":
            text = text + "Please answer in a floating-point number."
        text = text + guide + text_example
        image_path = f"{folder}image/image{temp}.png"

        model = genai.GenerativeModel('gemini-1.5-pro')
        sample_file = genai.upload_file(path=image_path)
        response = model.generate_content([sample_file, text])

        message = response.text

        try:
            dj = extract_json(message)
            print("Successfully extracted JSON:", dj)
        except Exception as e:
            dj = {
                "solution": message,
                "short answer": "wait for check"
            }
            print(f"Error extracting JSON: {str(e)}")

        temp_data = {"question": json_dict.get(f"{temp}").get('question'),
                     "subject": json_dict.get(f"{temp}").get('subject'),
                     "knowledge level": json_dict.get(f"{temp}").get('level'),
                     "Ground truth": json_dict.get(f"{temp}").get('answer'),
                     "image": f"image/image{i}.png",
                     "response": dj}
        answer = str(dj.get("short answer"))
        try:
            if json_dict.get(f"{temp}").get('answer_type') == "float":
                if not answer.isdigit():
                    parts = answer.split(' ')
                    answer = parts[0]
                    answer = transfer(answer)
                diff = float(answer) - float(temp_data.get("Ground truth"))
                if abs(diff) <= 0.001:
                    temp_data["result"] = "correct"
                    count += 1
                else:
                    temp_data["result"] = "fail"
            elif json_dict.get(f"{temp}").get('answer_type') == "multiple choice":
                if len(answer) == 1:
                    if answer == temp_data.get("Ground truth"):
                        temp_data["result"] = "correct"
                        count += 1
                    else:
                        temp_data["result"] = "fail"
                else:
                    if temp_data.get("Ground truth") in answer[0:3]:
                        temp_data["result"] = "correct"
                        count += 1
                    else:
                        temp_data["result"] = "fail"
            else:
                if temp_data.get("Ground truth") in answer:
                    temp_data["result"] = "correct"
                    count += 1
                else:
                    temp_data["result"] = "fail"
        except:
            temp_data["result"] = "fail"

        data[f"{i}"] = temp_data


        data[f"{temp}"] = temp_data


        with open(f'{folder}report_gemini_5.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

end = time.time()

print(f"The running time is {end-start}")