class Exam {
  int id;
  String name;
  String group;
  String details;
  String status;
  String type;
  int students;

  Exam({
    this.id,
    this.name,
    this.group,
    this.details,
    this.status,
    this.type,
    this.students,
  });

  factory Exam.fromJson(Map<String, dynamic> json) {
    return Exam(
      id: json['id'],
      name: json['name'],
      group: json['group'],
      details: json['details'],
      type: json['type'],
      status: json['status'],
      students: json['students'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'group': group,
      'details': details,
      'type': type,
      'status': status,
      'students': students,
    };
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'name': name,
      'group': group,
      'details': details,
      'type': type,
      'status': status,
      'students': students,
    };
  }

  @override
  String toString() {
    return this.name;
  }
}
