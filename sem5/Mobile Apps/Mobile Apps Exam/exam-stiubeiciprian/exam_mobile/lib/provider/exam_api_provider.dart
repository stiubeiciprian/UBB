import 'package:exam_mobile/model/exam.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:developer';

class ExamApiProvider {
  static const EXAMS_URL = 'http://10.0.2.2:2018/exams/';
  static const EXAM_BASE_URL = 'http://10.0.2.2:2018/exam/';
  static const DRAFT_BASE_URL = 'http://10.0.2.2:2018/draft/';
  static const JOIN_BASE_URL = 'http://10.0.2.2:2018/join/';
  static const GROUP_BASE_URL = 'http://10.0.2.2:2018/group/';

  List<Exam> _parseExams(String responseBody) {
    final parsed = jsonDecode(responseBody).cast<Map<String, dynamic>>();

    return parsed.map<Exam>((json) => Exam.fromJson(json)).toList();
  }

  Future<List<Exam>> getAllExams() async {
    final response = await http.get(EXAMS_URL);

    if (response.statusCode == 200) {
      return _parseExams(response.body);
    } else {
      throw Exception('Failed to get exams');
    }
  }

  Future<List<Exam>> getExamsFromGroup(String group) async {
    final url = '$GROUP_BASE_URL${group}/';
    final response = await http.get(url);

    if (response.statusCode == 200) {
      List<Exam> exams = _parseExams(response.body);
      exams.sort((a, b) {
        return b.type.compareTo(a.type);
      });
      exams.sort((a, b) {
        return a.students.compareTo(b.students);
      });

      return exams;
    } else {
      throw Exception('Failed to get exams');
    }
  }

  Future<Exam> getExam(String examId) async {
    final url = '$EXAM_BASE_URL${examId}/';
    final response = await http.get(url);

    if (response.statusCode == 200) {
      return Exam.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Failed to get exam');
    }
  }

  void joinExam(int examId) async {
    final headers = <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    };

    final body = <String, String>{
      'id': examId.toString(),
    };

    http.post(JOIN_BASE_URL, headers: headers, body: json.encode(body));
  }

  Future<List<Exam>> getAllDraftExams() async {
    final response = await http.get(DRAFT_BASE_URL);

    if (response.statusCode == 200) {
      return _parseExams(response.body);
    } else {
      throw Exception('Failed to get draft exams');
    }
  }

  // Future<List<Exam>> getTop10Messages() async {
  //   final response = await http.get(MESSAGES_URL);

  //   if (response.statusCode == 200) {
  //     List<Message> messages = _parseMessages(response.body);
  //     messages.sort((a, b) {
  //       return b.date.compareTo(a.date);
  //     });

  //     return messages.sublist(0, 10);
  //   } else {
  //     throw Exception('Failed to get messages');
  //   }
  // }

  // Future<List<Message>> getSentMessages(String user) async {
  //   final response = await http.get(MESSAGES_URL);

  //   if (response.statusCode == 200) {
  //     List<Message> messages = _parseMessages(response.body);
  //     messages.where((m) => m.sender == user).toList();

  //     return messages;
  //   } else {
  //     throw Exception('Failed to get messages');
  //   }
  // }

  // Future<List<Message>> getRecievedMessages(String user) async {
  //   final response = await http.get(MESSAGES_URL);

  //   if (response.statusCode == 200) {
  //     List<Message> messages = _parseMessages(response.body);
  //     messages.where((m) => m.receiver == user).toList();

  //     return messages;
  //   } else {
  //     throw Exception('Failed to get messages');
  //   }
  // }

  // Future<Message> getMessage(Message book) async {
  //   final url = '$BOOKS_URL${book.id}/';
  //   final response = await http.post(url);

  //   if (response.statusCode == 200) {
  //     return Message.fromJson(jsonDecode(response.body));
  //   } else {
  //     throw Exception('Failed to get book');
  //   }
  // }

  // Future<void> postMessage(Message book) async {
  //   final headers = <String, String>{
  //     'Content-Type': 'application/json; charset=UTF-8',
  //   };

  //   http.post(BOOKS_URL, headers: headers, body: jsonEncode(book.toJson()));
  // }

  // Future<void> putMessage(Message book) async {
  //   final url = '$BOOKS_URL${book.id}/';
  //   final headers = <String, String>{
  //     'Content-Type': 'application/json; charset=UTF-8',
  //   };

  //   http.put(url, headers: headers, body: jsonEncode(book.toJson()));
  // }

  // Future<void> deleteMessage(int id) async {
  //   final url = '$BOOKS_URL$id/';
  //   http.delete(url);
  // }

  // Future<void> syncData(List<Message> books) async {
  //   final url = '${BOOKS_URL}delete_all/';
  //   final headers = <String, String>{
  //     'Content-Type': 'application/json; charset=UTF-8',
  //   };
  //   await http.get(url);
  //   log(jsonEncode(books));
  //   await http.post(BOOKS_URL, headers: headers, body: jsonEncode(books));
  // }
}
