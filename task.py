greetings = {
    'English' : 'Dear [Firstname] [Lastname], \n\nCompliments of the season to you and your family. Wishing you the very best of the season.',
    'Greek' : 'Αγαπητέ/ή [Firstname] [Lastname], \n\nΚαλές γιορτές σε εσάς και την οικογένειά σας. Σας εύχομαι τα καλύτερα για αυτή την περίοδο του χρόνου.',
    'French' : 'Cher [Firstname] [Lastname], \n\nMeilleurs vœux de saison à vous et à votre famille. Je vous souhaite le meilleur pour cette période de l’année.',
}


import csv
with open('file.csv') as f:
    reader = csv.reader(f)
    for row in reader :
        Firstname, Lastname, phoneno, language = row
        if language in greetings:
            greeting = greetings[language].replace("[Firstname]", Firstname).replace("[Lastname]", Lastname)
            filename = f"{phoneno}.txt"
            f = open(filename, "w", encoding="utf-8")
            f.write(greeting)
            f.close()
            print(f"Greeting saved to {filename}")
