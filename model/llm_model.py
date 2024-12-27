
import google.generativeai as genai
import json
import time
from utils.get_prompt import generate_iot_prompt
genai.configure(api_key = "AIzaSyDcUZtqYAbySiqyf-uoz4BARiQG0v4oehk") # MAVEN only


# Generate content
model = genai.GenerativeModel(model_name='gemini-1.5-flash-latest')



def api_call(input_prompt: str):
    retry = 3
    while retry > 0:
        try:
            # completion = client.chat.completions.create(
            #     model="gpt-4o",
            #     messages=[
            #         {"role": "system", "content": "You are a helpful assistant."},
            #         {
            #             "role": "user",
            #             "content": input_prompt
            #         }
            #     ]
            # )
            # content = completion.choices[0].message.content
            response = model.generate_content(input_prompt)
            time.sleep(1)
            content = response.text
            content = content.split('\n')[0]
            return content
        except:
            retry -= 1
    raise Exception("Error: Retried 3 times!")