import tkinter
from database import query, cursor
from os import path
from PIL import Image, ImageTk



class Display:
    def __init__(self):
        self.word_input = ""
        self.film_searched = ""
        self.image_label = ""
        self.title_film = ""

        self.root = tkinter.Tk()
        self.root.geometry("1024x512+600+300")

        self.input = tkinter.Entry(self.root, textvariable=self.word_input)
        self.input.grid(row=0, column=0)

        self.button = tkinter.Button(self.root, text="Chercher", command=self.search)
        self.button.grid(row=1, column=0)

        self.root.mainloop()

    def search(self):
        # print("%s" % (self.input.get()))

        cursor.execute(query, {"title_to_find": "%"+self.input.get()+"%"})

        while True:
            self.film_searched = cursor.fetchone()
            if self.film_searched == None:
                break
            else:
                # print(films['title'])
                # self.list_films_searched.append(films['title'])
                result = tkinter.Label(self.root, text=self.film_searched["title"])
                result.film = self.film_searched
                result.bind("<Button>", self.show_one_moovie)
                result.grid(column=1)

    def show_one_moovie(self, event):
        # print(event.widget.film)
        film = event.widget.film
        # print(film["imdb_id"]+".jpg")
        try:
            self.image_label.destroy()
            self.title_film.destroy()
        except AttributeError:
            pass

        try:
            img_path = path.join("assets", film["imdb_id"]+".jpg")
            img_file = Image.open(img_path)

            # img_file = img_file.resize((256, 256))

            img_tk = ImageTk.PhotoImage(img_file)

            self.image_label = tkinter.Label(self.root)
            self.image_label.config(image=img_tk)
            self.image_label.grid(row=1, column=2)
            self.image_label.image = img_tk
        except FileNotFoundError:
            print(film["title"])
            self.title_film = tkinter.Label(self.root, text=film["title"])
            self.title_film.grid(row=1, column=2)

        

run = Display()
