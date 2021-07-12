import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:libr/model/book.dart';
import 'package:libr/notifiers/book_notifier.dart';
import 'package:libr/utils/libr_text_style.dart';
import 'package:provider/provider.dart';

class UpdateBookForm extends StatefulWidget {
  final Book book;

  const UpdateBookForm({Key key, @required this.book}) : super(key: key);

  @override
  UpdateBookFormState createState() {
    return UpdateBookFormState(book);
  }
}

class UpdateBookFormState extends State<UpdateBookForm> {
  final _formKey = GlobalKey<FormState>();
  final Book book;

  final _titleInputController = TextEditingController();
  final _authorInputController = TextEditingController();
  final _descriptionInputController = TextEditingController();
  final _genresInputController = TextEditingController();
  final _numberOfPagesInputController = TextEditingController();
  final _currentPageInputController = TextEditingController();

  UpdateBookFormState(this.book);

  @override
  Widget build(BuildContext context) {
    BookNotifier bookNotifier = Provider.of<BookNotifier>(context);

    _titleInputController.text = book.title;
    _authorInputController.text = book.author;
    _descriptionInputController.text = book.description;
    _genresInputController.text = book.genres;
    _numberOfPagesInputController.text = book.numberOfPages.toString();
    _currentPageInputController.text = book.currentPage.toString();

    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
        title: Text('Update book', style: LibrTextStyle.h1()),
        backgroundColor: Colors.transparent,
        elevation: 0.0,
        centerTitle: false,
      ),
      body: Container(
        margin: EdgeInsets.fromLTRB(17, 0, 17, 0),
        child: SingleChildScrollView(
          child: Form(
            key: _formKey,
            child: Column(
              children: <Widget>[
                TextFormField(
                  controller: _titleInputController,
                  decoration: InputDecoration(labelText: 'Title:'),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'Please enter title';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _authorInputController,
                  decoration: InputDecoration(labelText: 'Author:'),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'Please enter author';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _descriptionInputController,
                  decoration: InputDecoration(labelText: 'Description:'),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'Please enter descrition';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _genresInputController,
                  decoration: InputDecoration(labelText: 'Genres:'),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'Please enter genres';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _numberOfPagesInputController,
                  decoration: InputDecoration(labelText: 'Number of pages:'),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'Please enter number of pages';
                    }

                    if (int.tryParse(value) == null ||
                        int.tryParse(value) < 0) {
                      return 'Please enter a positive integer';
                    }

                    return null;
                  },
                ),
                TextFormField(
                  controller: _currentPageInputController,
                  decoration: InputDecoration(labelText: 'Current page:'),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'Please enter current page';
                    }

                    if (int.tryParse(value) == null ||
                        int.tryParse(value) < 0) {
                      return 'Please enter a positive integer';
                    }

                    return null;
                  },
                ),
                ElevatedButton(
                  onPressed: () {
                    if (_formKey.currentState.validate()) {
                      setState(() {
                        bookNotifier.update(
                            book.id,
                            _titleInputController.text,
                            _authorInputController.text,
                            _descriptionInputController.text,
                            int.parse(_numberOfPagesInputController.text),
                            int.parse(_currentPageInputController.text),
                            _genresInputController.text);
                      });

                      Navigator.of(context).pop();
                    }
                  },
                  child: Text('Update'),
                ),
              ],
              crossAxisAlignment: CrossAxisAlignment.stretch,
              mainAxisAlignment: MainAxisAlignment.start,
            ),
          ),
          padding: EdgeInsets.fromLTRB(14, 0, 14, 0),
        ),
      ),
    );
  }
}
