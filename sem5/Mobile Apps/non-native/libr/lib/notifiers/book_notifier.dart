import 'dart:collection';

import 'package:flutter/cupertino.dart';
import 'package:libr/model/book.dart';
import 'package:libr/persistence/book_persistence.dart';
import 'package:connectivity/connectivity.dart';
import 'package:libr/providers/book_api_provider.dart';
import 'dart:developer';

class BookNotifier with ChangeNotifier {
  BookApiProvider _bookApiProvider;
  BookPersistence _bookPersistence;
  List<Book> _books;

  BookNotifier() {
    _bookApiProvider = BookApiProvider();
    _bookPersistence = BookPersistence();
    _books = List<Book>();
    _loadDataToMemory();
  }

  void _syncData() async {
    try {
      var connected = await (Connectivity().checkConnectivity());

      if (connected == ConnectivityResult.mobile ||
          connected == ConnectivityResult.wifi) {
        _bookApiProvider.syncData(_books);
      }
    } catch (e) {
      log('Data sync failed');
    }
  }

  void _loadDataToMemory() async {
    _books = await _bookPersistence.books();
    _syncData();
    notifyListeners();
  }

  UnmodifiableListView<Book> get books => UnmodifiableListView(_books);

  Book book(int id) {
    return _books.firstWhere((element) => element.id == id,
        orElse: () => Book(
            id: -1,
            title: 'Not found',
            author: 'not found',
            description: 'Not found',
            numberOfPages: 0,
            currentPage: 0,
            genres: 'not found'));
  }

  void add(String title, String author, String description, int numberOfPages,
      int currentPage, String genres) {
    final book = Book(
        id: null,
        title: title,
        author: author,
        description: description,
        numberOfPages: numberOfPages,
        currentPage: currentPage,
        genres: genres);

    _postBook(book);
    _bookPersistence.insertBook(book);
    _loadDataToMemory();
  }

  void _postBook(book) async {
    var connected = await (Connectivity().checkConnectivity());
    if (connected == ConnectivityResult.mobile ||
        connected == ConnectivityResult.wifi) {
      _bookApiProvider.postBook(book);
    }
  }

  void update(int id, String title, String author, String description,
      int numberOfPages, int currentPage, String genres) {
    final book = Book(
        id: id,
        title: title,
        author: author,
        description: description,
        numberOfPages: numberOfPages,
        currentPage: currentPage,
        genres: genres);
    _putBook(book);
    _bookPersistence.updateBook(book);
    _loadDataToMemory();
  }

  void _putBook(book) async {
    var connected = await (Connectivity().checkConnectivity());
    if (connected == ConnectivityResult.mobile ||
        connected == ConnectivityResult.wifi) {
      _bookApiProvider.putBook(book);
    }
  }

  void remove(int id) {
    _deleteBook(id);
    _bookPersistence.deleteBook(id);
    _loadDataToMemory();
  }

  void _deleteBook(id) async {
    var connected = await (Connectivity().checkConnectivity());
    if (connected == ConnectivityResult.mobile ||
        connected == ConnectivityResult.wifi) {
      _bookApiProvider.deleteBook(id);
    }
  }
}
