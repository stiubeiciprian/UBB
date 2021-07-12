import 'dart:async';

import 'package:libr/model/book.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';
import 'package:flutter/widgets.dart';

class BookPersistence {
  Future<Database> database;

  BookPersistence() {
    WidgetsFlutterBinding.ensureInitialized();
    database = _connect();
  }

  Future<Database> _connect() async {
    return openDatabase(
      join(await getDatabasesPath(), 'books_database.db'),
      onCreate: (db, version) {
        return db.execute(
          "CREATE TABLE books(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, description TEXT, genres TEXT, numberOfPages INTEGER, currentPage INTEGER)",
        );
      },
      version: 1,
    );
  }

  Future<void> insertBook(Book book) async {
    final Database db = await database;

    await db.insert(
      'books',
      book.toMap(),
      conflictAlgorithm: ConflictAlgorithm.replace,
    );
  }

  Future<List<Book>> books() async {
    final Database db = await database;
    final List<Map<String, dynamic>> maps = await db.query('books');

    return List.generate(maps.length, (i) {
      return Book(
        id: maps[i]['id'],
        title: maps[i]['title'],
        author: maps[i]['author'],
        description: maps[i]['description'],
        numberOfPages: maps[i]['numberOfPages'],
        currentPage: maps[i]['currentPage'],
        genres: maps[i]['genres'],
      );
    });
  }

  Future<void> updateBook(Book book) async {
    final db = await database;

    await db.update(
      'books',
      book.toMap(),
      where: "id = ?",
      whereArgs: [book.id],
    );
  }

  Future<void> deleteBook(int id) async {
    final db = await database;

    await db.delete(
      'books',
      where: "id = ?",
      whereArgs: [id],
    );
  }

  Future<void> deleteAllData() async {
    final db = await database;

    await db.delete('books');
  }
}
