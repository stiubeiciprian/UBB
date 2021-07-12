package com.stiubeiciprian.libr.data

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.stiubeiciprian.libr.R
import kotlinx.android.synthetic.main.book_list_item_layout.view.*


class BookAdapter(
    private var bookList: List<Book>,
    private val listener: OnItemClickListener
    ) : RecyclerView.Adapter<BookAdapter.BookViewHolder>() {



    inner class BookViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView),
    View.OnClickListener {
        val bookCover: ImageView = itemView.book_cover
        val bookTitle: TextView = itemView.book_title
        val bookAuthor: TextView = itemView.book_author

        init {
            itemView.setOnClickListener(this)
        }

        override fun onClick(v: View?) {
            val position = adapterPosition
            if (position != RecyclerView.NO_POSITION) {
                listener.onItemClick(position)
            }
        }

    }




    interface OnItemClickListener {
        fun onItemClick(position: Int)
    }




    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): BookAdapter.BookViewHolder {
        val itemView = LayoutInflater.from(parent.context).inflate(R.layout.book_list_item_layout, parent, false)

        return BookViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: BookAdapter.BookViewHolder, position: Int) {
        val currentItem = bookList[position]

        holder.bookCover.setImageResource(currentItem.coverResource)
        holder.bookTitle.text = currentItem.title
        holder.bookAuthor.text = "written by ${currentItem.author}"
    }

    override fun getItemCount() = bookList.size

    public fun setData(books: List<Book>) {
        this.bookList = books
        notifyDataSetChanged()
    }

}