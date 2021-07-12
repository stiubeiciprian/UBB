package com.stiubeiciprian.libr

import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.stiubeiciprian.libr.data.Book
import com.stiubeiciprian.libr.data.BookAdapter
import com.stiubeiciprian.libr.data.BookViewModel
import kotlinx.android.synthetic.main.fragment_book_list.*
import kotlinx.android.synthetic.main.fragment_book_list.view.*


class BookListFragment : Fragment(), BookAdapter.OnItemClickListener {
    private lateinit var bookViewModel: BookViewModel
    private lateinit var bookList: List<Book>
    private lateinit var recyclerView: RecyclerView
    private lateinit var viewAdapter: BookAdapter

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_book_list, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        bookList = ArrayList<Book>()
        viewAdapter = BookAdapter(bookList, this)

        view.rv_book_list.adapter = viewAdapter
        view.rv_book_list.layoutManager = LinearLayoutManager(context)

        viewModels()


        fab_add_book.setOnClickListener {findNavController().navigate(R.id.action_BookListFragment_to_AddBookFragment)}

        swipeToRefresh.setOnRefreshListener {
            viewAdapter.setData(bookList)
            swipeToRefresh.isRefreshing = false
        }
    }

    private fun viewModels() {
        bookViewModel = ViewModelProvider(this.requireActivity()).get(BookViewModel::class.java)

        bookViewModel.getAllBooks.observe(viewLifecycleOwner, Observer {
            viewAdapter.setData(it)
            bookList = it
        })
    }

    override fun onItemClick(position: Int) {

        val clickedItem = bookList[position]
        val book = Book(clickedItem.id, clickedItem.coverResource, clickedItem.title, clickedItem.author, clickedItem.description, clickedItem.genres, clickedItem.pages, clickedItem.currentPage)
        val action = BookListFragmentDirections.actionBookListFragmentToBookDetailFragment(book)
        findNavController().navigate(action)
    }
}