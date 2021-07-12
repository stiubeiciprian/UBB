import 'package:exam_mobile/screens/stats_section.dart';
import 'package:exam_mobile/screens/stats_section_select.dart';
import 'package:exam_mobile/screens/teacher_section.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:exam_mobile/model/exam.dart';
import 'package:exam_mobile/provider/exam_api_provider.dart';
import 'dart:io';
import 'dart:async';
import 'dart:convert';
import 'dart:developer';

class StudentSection extends StatefulWidget {
  StudentSection({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _StudentSectionState createState() => _StudentSectionState();
}

class _StudentSectionState extends State<StudentSection> {
  Future<List<Exam>> futureExams;
  ExamApiProvider examApiProvider;
  final GlobalKey<ScaffoldState> _scaffoldKey = new GlobalKey<ScaffoldState>();
  bool loadedData;

  @override
  void initState() {
    super.initState();
    examApiProvider = ExamApiProvider();
    loadedData = false;
  }

  onError(err) {
    _scaffoldKey.currentState
        .showSnackBar(SnackBar(content: Text("No internet connection.")));
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
        title: Text('Student section'),
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
        child: FutureBuilder<List<Exam>>(
          future: futureExams,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return ListView.builder(
                  itemCount: snapshot.data.length,
                  itemBuilder: (BuildContext context, int index) {
                    return ListTile(
                      title: Text(snapshot.data[index].name),
                      subtitle: Text(snapshot.data[index].details),
                      onTap: () {
                        _joinExam(snapshot.data[index].id);
                      },
                    );
                  });
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

  _joinExam(examId) async {
    log("tapped");
    try {
      final result = await InternetAddress.lookup('google.com');
      if (result.isNotEmpty && result[0].rawAddress.isNotEmpty) {
        setState(() {
          this.examApiProvider.joinExam(examId);
          _scaffoldKey.currentState
              .showSnackBar(SnackBar(content: Text("Joined exam.")));
          log("joinedExam");
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

  _reloadData(BuildContext context) async {
    try {
      final result = await InternetAddress.lookup('google.com');
      if (result.isNotEmpty && result[0].rawAddress.isNotEmpty) {
        setState(() {
          this.futureExams = this.examApiProvider.getAllDraftExams();
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
