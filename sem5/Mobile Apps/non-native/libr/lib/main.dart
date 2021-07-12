import 'package:flutter/material.dart';
import 'package:libr/notifiers/book_notifier.dart';
import 'package:libr/screens/book_list.dart';
import 'package:provider/provider.dart';

void main() => runApp(
      ChangeNotifierProvider(
        create: (context) => BookNotifier(),
        child: Libr(),
      ),
    );

class Libr extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Libr',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: BookList(title: 'Libr'),
    );
  }
}
