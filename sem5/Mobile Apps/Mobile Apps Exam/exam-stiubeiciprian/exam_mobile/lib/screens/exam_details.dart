import 'package:exam_mobile/screens/stats_section.dart';
import 'package:exam_mobile/screens/stats_section_select.dart';
import 'package:exam_mobile/screens/student_section.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:exam_mobile/model/exam.dart';
import 'package:exam_mobile/provider/exam_api_provider.dart';
import 'dart:io';
import 'dart:async';
import 'dart:convert';
import 'dart:developer';

class ExamDetail extends StatefulWidget {
  ExamDetail({Key key, @required this.examId}) : super(key: key);

  final String examId;

  @override
  _ExamDetailState createState() => _ExamDetailState();
}

class _ExamDetailState extends State<ExamDetail> {
  Future<Exam> futureExam;
  ExamApiProvider examApiProvider;
  final GlobalKey<ScaffoldState> _scaffoldKey = new GlobalKey<ScaffoldState>();
  bool loadedData;

  @override
  void initState() {
    super.initState();
    examApiProvider = ExamApiProvider();
    loadedData = false;
  }

  @override
  Widget build(BuildContext context) {
    if (loadedData == false) {
      _reloadData(context);
      setState(() {
        loadedData = true;
      });
    }

    return Scaffold(
      key: _scaffoldKey,
      backgroundColor: Colors.grey.shade200,
      appBar: AppBar(
        title: Text('Exam details'),
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
              title: Text('Student section'),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => StudentSection()),
                );
              },
            ),
            ListTile(
              title: Text('Stats section'),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => StatsSectionSelect()),
                );
              },
            ),
          ],
        ),
      ),
      body: Container(
        margin: EdgeInsets.fromLTRB(17, 0, 17, 0),
        child: FutureBuilder<Exam>(
          future: futureExam,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return Center(
                child: Padding(
                  padding: const EdgeInsets.all(18.0),
                  child: Column(
                    children: [
                      Text('id: ' + snapshot.data.id.toString()),
                      Text('name: ' + snapshot.data.name),
                      Text('group: ' + snapshot.data.group),
                      Text('details: ' + snapshot.data.details),
                      Text('status: ' + snapshot.data.status),
                      Text('type: ' + snapshot.data.type),
                      Text('students: ' + snapshot.data.students.toString()),
                    ],
                  ),
                ),
              );
            } else if (snapshot.hasError) {
              Scaffold.of(context)
                  .showSnackBar(SnackBar(content: Text("${snapshot.error}")));
              return Text("${snapshot.error}");
            }

            return Center(
                child: SizedBox(
                    width: 30, height: 30, child: CircularProgressIndicator()));
          },
        ),
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.autorenew),
        onPressed: () {
          _reloadData(context);
        },
      ),
    );
  }

  _reloadData(BuildContext context) async {
    try {
      final result = await InternetAddress.lookup('google.com');
      if (result.isNotEmpty && result[0].rawAddress.isNotEmpty) {
        setState(() {
          this.futureExam = this.examApiProvider.getExam(widget.examId);
          log("refreshed");
        });
      } else {
        _scaffoldKey.currentState
            .showSnackBar(SnackBar(content: Text("No internet connection!")));
      }
    } on SocketException catch (_) {
      _scaffoldKey.currentState
          .showSnackBar(SnackBar(content: Text("No internet connection!")));
    }
  }
}
