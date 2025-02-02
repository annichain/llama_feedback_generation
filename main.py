import csv
from langchain_ollama import OllamaLLM
import datetime
import pathlib
from input import Input

model = OllamaLLM(model="llama3.2")

def generate_feedback(filename):

    file = open(filename, "w")
    writer = csv.writer(file, delimiter=";")
    # Kopf der CSV Datei
    head = ["prompt", "submission_id", "timestamp", "currenttime", "feedback"]
    writer.writerow(head)

    idnumber = 00000 
    for x in range(3500): #replace with actual number or condition

        submission_id = str(idnumber)
        if pathlib.Path("submissions/" + submission_id + ".java").exists(): #replace with actual filepaths
            prompt = Input.generate_prompt(submission_id)
            timestamp = datetime.datetime.now()
            response = model.invoke(prompt)
            currenttime = datetime.datetime.now()
            line = [prompt, submission_id, timestamp, currenttime, response]
            writer.writerow(line)
            print(idnumber)

        idnumber += 1

   
    file.close()

generate_feedback("feedback_round1.txt")

