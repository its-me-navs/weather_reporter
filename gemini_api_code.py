import weather_api
from google import genai

client = genai.Client(api_key="<your_gemini_api_key_here>")

print(weather_api.weather())   

system_prompt="Act like a weather reporter, and give me a weather report in about 100 words.\n"

system_prompt+="Here is the json data about today's weather"
system_prompt+=weather_api.weather()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=system_prompt,
)
print(response.text)
    
 



