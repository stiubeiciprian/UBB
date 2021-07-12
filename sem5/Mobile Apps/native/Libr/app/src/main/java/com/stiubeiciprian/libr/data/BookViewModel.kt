package com.stiubeiciprian.libr.data

import android.app.Application
import android.util.Log
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.MutableLiveData
import com.stiubeiciprian.libr.R


class BookViewModel(application: Application) : AndroidViewModel(application) {
    private var books: ArrayList<Book>
    val getAllBooks: MutableLiveData<List<Book>>
    private var id: Int = 100

    init {
        books = generateDummyList(10)
        getAllBooks = MutableLiveData(books)
    }

    private fun generateDummyList(size: Int): ArrayList<Book> {
        val list = ArrayList<Book>()

        list += Book(0, R.drawable.none, "And then there were None", "Aghata Christie", "Lorem ipsum sim dolor. Bla bla bla...", "Science-Fiction, Novel", 231, 0)
        list += Book(1, R.drawable.martian, "The Martian", "Andy Weir", "Lorem ipsum sim dolor. Bla bla bla...", "Science-Fiction, Novel", 231, 0)
        list += Book(2, R.drawable.minimalism, "Digital Minimalism", "Cal Newport", "Lorem ipsum sim dolor. Bla bla bla...", "Science-Fiction, Drama", 304, 0)
        list += Book(3, R.drawable.nineteen, "Nineteen Eighty-four", "George Orwell", "Lorem ipsum sim dolor. Bla bla bla...", "Science-Fiction, Drama", 256, 0)

        for (i in 0 until size - 4) {
            list += Book(i + 4, R.drawable.none, "Another book", "Another author", "Another description", "Another genre", 100, 0)
        }

        return list
    }

    fun addBook(book: Book) {
        books.add(book)
    }

    fun updateBook(book: Book) {
        for (i in 0 until books.size) {
            if (book.id == books[i].id) {
                books[i].title = book.title
                books[i].author = book.author
                books[i].coverResource = book.coverResource
                books[i].description = book.description
                books[i].pages = book.pages
                books[i].currentPage = book.currentPage
                books[i].genres = book.genres
            }
        }
    }

    fun deleteBook(book: Book) {
        books.remove(book)
    }

    fun getSize(): Int {
        return books.size
    }

    fun getID(): Int {
        id++
        return id
    }

}