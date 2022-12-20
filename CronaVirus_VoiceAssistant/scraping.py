import requests
from bs4 import BeautifulSoup as bs
import pyttsx3
import json
import speech_recognition as sr
import re  # regex search patterns
import threading
import time

# https://www.worldometers.info/coronavirus/

# API Key t-1DkqpJ3GOmXYSj5JTyToken tdBtD27D0T-1

api_key = "t-1DkqpJ3GOm"
project_token = "t1XYSj5JTy-L"
run_token = "tdBtD27D0T-1"


class data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.data = self.get_data()

    def get_data(self):
        response = requests.get(
            f'https://www.parsehub.com/api/v2/projects/{project_token}/last_ready_run/data', params={"api_key": api_key})
        data = json.loads(response.text)
        return data

    def total_cases(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Coronavirus Cases:":
                return content['value']

    def total_deaths(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Deaths:":
                return content['value']

        return "0"

    def get_country(self, country):
        data = self.data['country']

        for content in data:
            if content['name'].lower() == country.lower():
                return content
        return "0"

    def get_list_of_countries(self):
        countries = []
        for country in self.data['country']:
            countries.append(country['name'])
        return countries

    def update_data(self):
        response = requests.post(
            f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run', params=self.params)

        def poll():
            time.sleep(0.1)
            old_data = self.data
            while True:
                new_data = self.get_data()
                if new_data != old_data:
                    self.data = new_data
                    print("Data updated")
                    break
                time.sleep(5)

        t = threading.Thread(target=poll)
        t.start()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception:", str(e))

    return said.lower()


def main():
    print("Start Program")
    enddata = data(api_key, project_token)
    end_phrase = "stop"
    total_patterns = {
        re.compile("[\w\s]+ total [\w\s]+ cases"): enddata.total_cases,
        re.compile("[\w\s]+ total cases"): enddata.total_cases,
        re.compile("[\w\s]+ total [\w\s]+ deaths"): enddata.total_deaths,
        re.compile("[\w\s]+ total deaths"): enddata.total_deaths
    }

    country_patterns = {
        re.compile("[\w\s]+ cases [\w\s]+"): lambda country: data.get_country(country)['total_cases'],
        re.compile("[\w\s]+ deaths [\w\s]+"): lambda country: data.get_country(country)['total_deaths']
    }

    Update_command = "update"
    while True:
        print("Listening...")
        text = get_audio()
        print(text)
        result = None
        country_list = (data.get_list_of_countries)

        for pattern, func in total_patterns.items():
            if pattern.match(text):
                result = func()
                break

        for pattern, func in country_patterns.items():
            if pattern.match(text):
               words = set(text.split(" "))
               for country in country_list:
                if country in words:
                    result = func(country)
                    break

        if text == Update_command:
            result = "Data is being updated. This may take a moment!"
            data.update_data()
        if result:
            speak(result)

        if text.find(end_phrase) != -1:  # stop loop
            print("Exit")
            break


main()


# ## Simple file write object
# # class writeToFile(object):
# #     def __init__(self, fileName):
# #         self.fileName = fileName

# #     def __enter__(self):
# #         self.file = open(self.fileName, 'w')
# #         return self.file

# #     def __exit__(self, *args):
# #         self.file.close()

# # with writeToFile('helloworld') as xfile: # refers to file descriptor resource
# #     xfile.write("new line written to file\n")
