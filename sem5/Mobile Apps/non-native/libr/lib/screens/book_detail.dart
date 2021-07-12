import 'package:flutter/material.dart';
import 'package:libr/model/book.dart';
import 'package:libr/notifiers/book_notifier.dart';
import 'package:libr/screens/update_book.dart';
import 'package:libr/utils/libr_text_style.dart';
import 'package:provider/provider.dart';

class BookDetail extends StatelessWidget {
  final Book book;

  BookDetail({Key key, @required this.book}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    BookNotifier bookNotifier = Provider.of<BookNotifier>(context);
    Book currentBook = bookNotifier.book(book.id);

    return Scaffold(
      body: Container(
        child: Column(
          children: <Widget>[
            _bookMainDetails(currentBook),
            Container(
              margin: EdgeInsets.only(top: 30),
              child: Card(
                child: Container(
                  padding: EdgeInsets.all(15),
                  child: Column(
                    children: [
                      Text('Description', style: LibrTextStyle.pBold()),
                      SizedBox(height: 5),
                      Text(currentBook.description, style: LibrTextStyle.p()),
                      SizedBox(height: 20),
                      Text('Genres', style: LibrTextStyle.pBold()),
                      SizedBox(height: 5),
                      Text(currentBook.genres, style: LibrTextStyle.p()),
                      SizedBox(height: 20),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Builder(
                            builder: (ctx) => Container(
                              width: 150,
                              child: ElevatedButton(
                                onPressed: () {
                                  _showDeleteDialog(context, bookNotifier);
                                },
                                child: Text('Delete'),
                                style: ElevatedButton.styleFrom(
                                  primary: Colors.red,
                                ),
                              ),
                            ),
                          ),
                          Builder(
                            builder: (ctx) => Container(
                              width: 150,
                              child: ElevatedButton(
                                onPressed: () {
                                  _navigateToUpdateBook(context, currentBook);
                                },
                                child: Text('Update'),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ],
                    crossAxisAlignment: CrossAxisAlignment.start,
                  ),
                ),
              ),
            ),
          ],
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.start,
        ),
        padding: EdgeInsets.all(32.0),
      ),
    );
  }

  _navigateToUpdateBook(BuildContext context, Book book) async {
    await Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => UpdateBookForm(book: book)),
    );
  }

  Future<void> _showDeleteDialog(
      BuildContext context, BookNotifier bookNotifier) async {
    return showDialog<void>(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text(
            'Are you sure you want to delete this book?',
            textAlign: TextAlign.center,
          ),
          actions: <Widget>[
            TextButton(
              child: Text('DELETE'),
              onPressed: () {
                bookNotifier.remove(book.id);
                Navigator.of(context).popUntil((route) => route.isFirst);
              },
            ),
            TextButton(
              child: Text('CANCEL'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  Widget _bookMainDetails(Book currentBook) {
    return Container(
      child: Row(
        children: [
          Container(
            margin: EdgeInsets.only(right: 10),
            child: ClipRRect(
              borderRadius: BorderRadius.circular(8.0),
              child: Image.asset('assets/images/we.jpg',
                  width: 150, fit: BoxFit.fitWidth),
            ),
          ),
          Column(
            children: [
              Text(currentBook.title, style: LibrTextStyle.h1()),
              Text('written by ' + currentBook.author,
                  style: LibrTextStyle.subtitleH1()),
            ],
            crossAxisAlignment: CrossAxisAlignment.start,
          ),
        ],
      ),
    );
  }
}
