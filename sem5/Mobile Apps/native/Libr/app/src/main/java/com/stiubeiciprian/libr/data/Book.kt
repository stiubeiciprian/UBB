package com.stiubeiciprian.libr.data

import android.os.Parcelable
import kotlinx.android.parcel.Parcelize

@Parcelize
data class Book(val id: Int, var coverResource: Int, var title: String, var author: String, var description: String, var genres: String, var pages: Int, var currentPage: Int):
    Parcelable {
    override fun toString(): String = title
}