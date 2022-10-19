from flask import Flask, render_template, request
import random
import pandas as pd
import csv
import time

app = Flask(__name__)

song_eng_data=[]

# title,description,appears on,artist,writers,producer,released,streak,position
with open('songeng.csv', encoding="utf8", errors='ignore') as file_obj:
    heading = next(file_obj)
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:  
        song_eng_data.append(row)        

books_data=[]
# bookID,title,authors,average_rating,isbn,isbn13,language_code,  num_pages,ratings_count,text_reviews_count,publication_date,publisher
with open('books.csv') as file_obj:
    heading = next(file_obj)
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        books_data.append(row)

recomend_books_data=[]

@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recomend = request.form.get('language')

        if recomend == 'booktosong':
            if request.method == 'POST':
                name = request.form.get('fname')

                if "amazon" in name:
                    recomend_songs_data=[]
                    for i in range(6):
                        recomend_songs_data.append(random.choice(song_eng_data))
                    time.sleep(5)
                    return render_template('spotify.html', data=recomend_songs_data)

        if recomend == 'songtobook':
            if request.method == 'POST':
                name = request.form.get('fname')

                if "spotify" in name:
                    recomend_books_data=[]
                    for i in range(6):
                        recomend_books_data.append(random.choice(books_data))
                    time.sleep(5)
                    return render_template('book.html', data=recomend_books_data)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
