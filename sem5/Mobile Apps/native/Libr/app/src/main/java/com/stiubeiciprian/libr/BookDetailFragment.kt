package com.stiubeiciprian.libr

import android.app.Dialog
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import androidx.navigation.fragment.navArgs
import com.stiubeiciprian.libr.data.BookViewModel
import kotlinx.android.synthetic.main.fragment_book_detail.view.*


class BookDetailFragment : Fragment() {
    private val args by navArgs<BookDetailFragmentArgs>()
    private lateinit var dialog: Dialog
    private lateinit var bookViewModel: BookViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.fragment_book_detail, container, false)

        view.book_title.text = args.currentBook.title
        view.book_author.text = "by ${args.currentBook.author}"
        view.book_cover.setImageResource( args.currentBook.coverResource)
        view.book_description.text =  args.currentBook.description
        view.book_pages.text = "${args.currentBook.currentPage}/${args.currentBook.pages}"
        view.book_genres.text = args.currentBook.genres

        bookViewModel = ViewModelProvider(this.requireActivity()).get(BookViewModel::class.java)

        view.update_book_button.setOnClickListener{ navigateToBookUpdate() }
        view.delete_book_button.setOnClickListener{ showConfirmDialog() }

        dialog = Dialog(this.requireContext())

        return view
    }

    private fun navigateToBookUpdate() {
        val action = BookDetailFragmentDirections.actionBookDetailFragmentToUpdateBookFragment(args.currentBook)
        findNavController().navigate(action)
    }

     private fun showConfirmDialog() {
        dialog.setContentView(R.layout.dialog_layout)
        dialog.window?.setBackgroundDrawable(ColorDrawable(Color.TRANSPARENT))

        dialog.findViewById<Button>(R.id.cancel_dialog_button).setOnClickListener { dialog.dismiss() }
        dialog.findViewById<Button>(R.id.delete_dialog_button).setOnClickListener {
            bookViewModel.deleteBook(args.currentBook)
            Toast.makeText(this.requireContext(), "Book removed", Toast.LENGTH_SHORT).show()
            dialog.dismiss()
            findNavController().navigate(R.id.action_BookDetailFragment_to_BookListFragment)
        }

        dialog.show()
    }



}