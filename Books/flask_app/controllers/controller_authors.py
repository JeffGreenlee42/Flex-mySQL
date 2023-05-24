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
    author = Author.get_author(author_id)
    author_name = author["name"]
    return render_template("author_show.html", author_name = author_name)


