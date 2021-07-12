import 'package:exam_mobile/screens/stats_section.dart';
import 'package:exam_mobile/screens/student_section.dart';
import 'package:exam_mobile/screens/teacher_section.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:exam_mobile/model/exam.dart';
import 'package:exam_mobile/provider/exam_api_provider.dart';
import 'dart:io';
import 'dart:async';
import 'dart:convert';
import 'dart:developer';

class StatsSectionSelect extends StatefulWidget {
  StatsSectionSelect({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _StatsSectionSelectState createState() => _StatsSectionSelectState();
}

class _StatsSectionSelectState extends State<StatsSectionSelect> {
  final GlobalKey<ScaffoldState> _scaffoldKey = new GlobalKey<ScaffoldState>();
  final _formKey = GlobalKey<FormState>();
  final _groupInputController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      backgroundColor: Colors.grey.shade200,
      appBar: AppBar(
        title: Text('Stats section'),
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: <Widget>[
            DrawerHeader(
              child: Text('Menu'),
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
            ),
            ListTile(
              title: Text('Teacher section'),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => TeacherSection()),
                );
              },
            ),
            ListTile(
              title: Text('Student section'),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => StudentSection()),
                );
              },
            ),
          ],
        ),
      ),
      body: Container(
        margin: EdgeInsets.fromLTRB(17, 0, 17, 0),
        child: Form(
          key: _formKey,
          child: Column(
            children: <Widget>[
              TextFormField(
                controller: _groupInputController,
                decoration: InputDecoration(labelText: 'Group:'),
                validator: (value) {
                  if (value.isEmpty) {
                    return 'Please enter group';
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
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) =>
                              StatsSection(group: _groupInputController.text)),
                    );
                  }
                },
                child: Text('Get exams'),
                style: ElevatedButton.styleFrom(
                  primary: Colors.green,
                ),
              ),
            ],
            crossAxisAlignment: CrossAxisAlignment.stretch,
            mainAxisAlignment: MainAxisAlignment.start,
          ),
        ),
      ),
    );
  }
}
