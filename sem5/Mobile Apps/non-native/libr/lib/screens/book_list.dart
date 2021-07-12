import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:libr/notifiers/book_notifier.dart';
import 'package:libr/screens/add_book.dart';
import 'package:libr/screens/book_detail.dart';
import 'package:libr/utils/libr_text_style.dart';
import 'package:provider/provider.dart';

class BookList extends StatefulWidget {
  BookList({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _BookListState createState() => _BookListState();
}

class _BookListState extends State<BookList> {
  @override
  Widget build(BuildContext context) {
    BookNotifier bookNotifier = Provider.of<BookNotifier>(context);

    return Scaffold(
      backgroundColor: Colors.grey.shade200,
      appBar: AppBar(
        title: Text('My Books', style: LibrTextStyle.h1()),
        backgroundColor: Colors.transparent,
        elevation: 0.0,
      ),
      body: Container(
        margin: EdgeInsets.fromLTRB(17, 0, 17, 0),
        child: ListView.builder(
            itemCount: bookNotifier.books.length,
            itemBuilder: (BuildContext context, int index) {
              return Container(
                margin: EdgeInsets.fromLTRB(0, 17, 0, 0),
                child: GestureDetector(
                  child: Card(
                    child: Row(
                      children: [
                        Container(
                          margin: EdgeInsets.only(right: 15),
                          child: ClipRRect(
                            borderRadius: BorderRadius.circular(8.0),
                            child: Image.asset('assets/images/we.jpg',
                                width: 90, fit: BoxFit.fitWidth),
                          ),
                        ),
                        Container(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                bookNotifier.books[index].title,
                                style: LibrTextStyle.h2(),
                                overflow: TextOverflow.ellipsis,
                              ),
                              Text(
                                "written by " +
                                    bookNotifier.books[index].author,
                                style: LibrTextStyle.subtitleH2(),
                                overflow: TextOverflow.ellipsis,
                              ),
                            ],
                          ),
                        )
                      ],
                    ),
                  ),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) =>
                              BookDetail(book: bookNotifier.books[index])),
                    );
                  },
                ),
              );
            }),
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () {
          _navigateToAddBook(context);
        },
      ),
    );
  }

  _navigateToAddBook(BuildContext context) async {
    await Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => AddBookForm()),
    );
  }
}
