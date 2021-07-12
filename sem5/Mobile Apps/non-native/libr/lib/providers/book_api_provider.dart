import 'package:libr/model/book.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:developer';

class BookApiProvider {
  static const BOOKS_URL = 'http://10.0.2.2:8000/books/';

  List<Book> _parseBooks(String responseBody) {
    final parsed = jsonDecode(responseBody).cast<Map<String, dynamic>>();

    return parsed.map<Book>((json) => Book.fromJson(json)).toList();
  }

  Future<List<Book>> getAllBooks() async {
    final response = await http.get(BOOKS_URL);

    if (response.statusCode == 200) {
      return _parseBooks(response.body);
    } else {
      throw Exception('Failed to get books');
    }
  }

  Future<Book> getBook(Book book) async {
    final url = '$BOOKS_URL${book.id}/';
    final response = await http.post(url);

    if (response.statusCode == 200) {
      return Book.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Failed to get book');
    }
  }

  Future<void> postBook(Book book) async {
    final headers = <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    };

    http.post(BOOKS_URL, headers: headers, body: jsonEncode(book.toJson()));
  }

  Future<void> putBook(Book book) async {
    final url = '$BOOKS_URL${book.id}/';
    final headers = <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    };

    http.put(url, headers: headers, body: jsonEncode(book.toJson()));
  }

  Future<void> deleteBook(int id) async {
    final url = '$BOOKS_URL$id/';
    http.delete(url);
  }

  Future<void> syncData(List<Book> books) async {
    final url = '${BOOKS_URL}delete_all/';
    final headers = <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    };
    await http.get(url);
    log(jsonEncode(books));
    await http.post(BOOKS_URL, headers: headers, body: jsonEncode(books));
  }
}
