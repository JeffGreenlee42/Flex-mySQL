from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.models_authors import Author
from flask_app.models.models_books import Book

@app.route("/authors")
def authors():
    all_authors = Author.get_all()
    print(all_authors)
    return render_template("authors.html", all_authors = all_authors)

@app.route("/books")
def books():
    all_books = Book.get_all()
    print(all_books)
    return render_template("books.html", all_books = all_books)


@app.route("/add_new_author", methods=["POST"])
def add_new_author():
    result = Author.save(request.form)
    return redirect("/authors")

@app.route("/add_new_book", methods=["POST"])
def add_new_book():
    result = Book.save(request.form)
    return redirect("/books")

@app.route("/authors/author_favorites/<int:author_id>")
def author_favorites(author_id):
    author_id = {
        "id" : author_id
    }
    print(f"from controller: author_id = {author_id}")
    all_books = Book.get_all()
    favorite_books = Author.get_author_favorites(author_id)
    print(f"from controller: Favorite books is {favorite_books}")
    author = Author.get_author(author_id)
    author_name = author[0]["name"]
    author_id = author_id["id"]
    return render_template("author_show.html", author_name = author_name, all_books = all_books, author_id = author_id, favorite_books = favorite_books)

@app.route("/authors/add_author_fav/<int:author_id>", methods=["POST"])
def add_author_fav(author_id):
    data = {
        "author_id": author_id,
        "book_id": request.form['book_id']
    }
    result = Author.create_author_favorite(data)
    return redirect(f"/authors/author_favorites/{data['author_id']}")
    
@app.route("/book/authors_pick/<int:book_id>")
def authors_pick(book_id):
    book_id = {
        "id": book_id
    }
    book = Book.get_book(book_id)
    book_title = book[0]["title"]
    picked_by_authors = Book.get_authors_selected_book(book_id)
    all_authors = Author.get_all()
    book_id = book_id["id"]
    print(f"From controller authors_pick: all_authors = {all_authors}")
    return render_template("book_show.html", book_id = book_id, book_title = book_title,  picked_by_authors = picked_by_authors, all_authors = all_authors)

@app.route("/book/add_author_pick/<int:book_id>", methods=["POST"])
def add_author_pick(book_id):
    data = {
        "book_id": book_id,
        "author_id": request.form['author_id']
    }
    result = Author.create_author_favorite(data)
    return redirect(f"/book/authors_pick/{book_id}")