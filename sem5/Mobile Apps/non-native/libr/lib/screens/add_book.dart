import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:libr/notifiers/book_notifier.dart';
import 'package:libr/utils/libr_text_style.dart';
import 'package:provider/provider.dart';

class AddBookForm extends StatefulWidget {
  @override
  AddBookFormState createState() {
    return AddBookFormState();
  }
}

class AddBookFormState extends State<AddBookForm> {
  final _formKey = GlobalKey<FormState>();

  final _titleInputController = TextEditingController();
  final _authorInputController = TextEditingController();
  final _descriptionInputController = TextEditingController();
  final _genresInputController = TextEditingController();
  final _numberOfPagesInputController = TextEditingController();
  final _currentPageInputController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    BookNotifier bookNotifier = Provider.of<BookNotifier>(context);

    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
        title: Text('Add book', style: LibrTextStyle.h1()),
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

                    if (int.tryParse(value) == null) {
                      return 'Please enter a positive integer';
                    }

                    if (int.tryParse(value) < 0) {
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

                    if (int.tryParse(value) == null) {
                      return 'Please enter a positive integer';
                    }

                    if (int.tryParse(value) < 0) {
                      return 'Please enter a positive integer';
                    }

                    return null;
                  },
                ),
                ElevatedButton(
                  onPressed: () {
                    if (_formKey.currentState.validate()) {
                      setState(() {
                        bookNotifier.add(
                            _titleInputController.text,
                            _authorInputController.text,
                            _descriptionInputController.text,
                            int.parse(_numberOfPagesInputController.text),
                            int.parse(_currentPageInputController.text),
                            _genresInputController.text);
                      });

                      Navigator.of(context).popUntil((route) => route.isFirst);
                    }
                  },
                  child: Text('Add book'),
                  style: ElevatedButton.styleFrom(
                    primary: Colors.green,
                  ),
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
