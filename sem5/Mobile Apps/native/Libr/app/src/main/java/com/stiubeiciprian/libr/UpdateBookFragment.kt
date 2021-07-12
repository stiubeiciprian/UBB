package com.stiubeiciprian.libr

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import androidx.navigation.fragment.navArgs
import com.stiubeiciprian.libr.data.Book
import com.stiubeiciprian.libr.data.BookViewModel
import kotlinx.android.synthetic.main.fragment_add_book.*
import kotlinx.android.synthetic.main.fragment_add_book.view.*
import kotlinx.android.synthetic.main.fragment_update_book.view.*
import kotlinx.android.synthetic.main.fragment_update_book.view.author_input
import kotlinx.android.synthetic.main.fragment_update_book.view.current_page_input
import kotlinx.android.synthetic.main.fragment_update_book.view.description_input
import kotlinx.android.synthetic.main.fragment_update_book.view.genres_input
import kotlinx.android.synthetic.main.fragment_update_book.view.page_input
import kotlinx.android.synthetic.main.fragment_update_book.view.title_input


class UpdateBookFragment : Fragment() {
    private val args by navArgs<UpdateBookFragmentArgs>()
    private lateinit var bookViewModel: BookViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.fragment_update_book, container, false)

        view.title_input.setText(args.bookData.title)
        view.author_input.setText(args.bookData.author)
        view.description_input.setText(args.bookData.description)
        view.page_input.setText(args.bookData.pages.toString())
        view.genres_input.setText(args.bookData.genres)
        view.current_page_input.setText(args.bookData.currentPage.toString())


        bookViewModel = ViewModelProvider(this.requireActivity()).get(BookViewModel::class.java)
        view.update_book_button.setOnClickListener { updateBook() }

        return view
    }

    private fun updateBook() {

        //Get text from editTexts
        val title = title_input.text.toString()
        val author = author_input.text.toString()
        val genres = genres_input.text.toString()
        val pages = page_input.text.toString()
        val currentPage = current_page_input.text.toString()
        val description = description_input.text.toString()
        val cover = args.bookData.coverResource

        if (!(title.isEmpty() || description.isEmpty() || genres.isEmpty() || pages.isEmpty() || currentPage.isEmpty())) {
            val book = Book(
                args.bookData.id,
                cover,
                title,
                author,
                description,
                genres,
                pages.toInt(),
                currentPage.toInt()
            )

            //add the habit if all the fields are filled
            bookViewModel.updateBook(book)
            Toast.makeText(this.requireContext(), "Book updated", Toast.LENGTH_SHORT).show()

            //navigate back to our home fragment
            findNavController().navigate(R.id.action_UpdateBookFragment_to_BookListFragment)
        } else {
            Toast.makeText(context, "Please fill all the fields", Toast.LENGTH_SHORT).show()
        }

    }
}