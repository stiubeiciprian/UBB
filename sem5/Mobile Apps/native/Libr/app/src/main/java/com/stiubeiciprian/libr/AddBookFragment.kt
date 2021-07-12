package com.stiubeiciprian.libr

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import com.stiubeiciprian.libr.data.Book
import com.stiubeiciprian.libr.data.BookViewModel
import kotlinx.android.synthetic.main.fragment_add_book.*
import kotlinx.android.synthetic.main.fragment_add_book.view.*


class AddBookFragment : Fragment() {
    private lateinit var bookViewModel: BookViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.fragment_add_book, container, false)

        bookViewModel = ViewModelProvider(this.requireActivity()).get(BookViewModel::class.java)
        view.add_book_button.setOnClickListener { addBook() }

        return view
    }

    private fun addBook() {

        //Get text from editTexts
        val title = title_input.text.toString()
        val author = author_input.text.toString()
        val genres = genres_input.text.toString()
        val pages = page_input.text.toString()
        val currentPage = current_page_input.text.toString()
        val description = description_input.text.toString()
        val cover = R.drawable.none

        if (!(title.isEmpty() || description.isEmpty() || genres.isEmpty() || pages.isEmpty() || currentPage.isEmpty())) {
            val book = Book(bookViewModel.getID(), cover, title, author, description, genres, pages.toInt(), currentPage.toInt())

            //add the habit if all the fields are filled
            bookViewModel.addBook(book)
            Toast.makeText(this.requireContext(), "Book added", Toast.LENGTH_SHORT).show()

            //navigate back to our home fragment
            findNavController().navigate(R.id.action_AddBookFragment_to_BookListFragment)
        } else {
            Toast.makeText(context, "Please fill all the fields", Toast.LENGTH_SHORT).show()
        }
    }

}