#charange7

#Q1
with open("st.txt", "w") as f:
    f.write("fruits = [apple, banana, orange]")

with open("st.txt", "r") as f:
    print(f.read())

#Q2
question = "what are you name?"
with open("st.txt", "w") as f:
    f.write(question)

#Q3
import csv

with open("im.csv", "w", newline='') as p:
    w = csv.writer(p, delimiter=",")
    w.writerow(["Top Gun","Risky Business"])
    w.writerow(["Tintail","Obama","Choco"])
    w.writerow(["Man on Fire","level 5"])

#Q4
import csv

with open("im.csv1", "w", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["トップガン", "リスキービジネス"])
    w.writerow(["チンタル","オバマ","チョコ"])
    w.writerow(["マンオンファイア","レヴェル５"])

import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
