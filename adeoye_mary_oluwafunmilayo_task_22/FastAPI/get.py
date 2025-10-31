from fastapi import FastAPI

books = ["Rich dad and poor dad", "Things fall aparts", "Queen primer"]


app=FastAPI()

@app.get("/")
def root():
    return({"message": "Hello World"})

@app.get("/books")    
def get_books():
    return("Books")

@app.post("/new_book")
def create_book(book_name: str):
    books.append(book_name)
    return(books)

@app.put("/update_book")
def update_book(index: int, name:str):
    books[index]= name
    return({"update_book": "books[index]", "to": name})

@app.delete("/delete_book")    
def delete_book(index:int):
    deleted_book= books.pop(index)
    return({"deleted": deleted_book, "books leftt":books})