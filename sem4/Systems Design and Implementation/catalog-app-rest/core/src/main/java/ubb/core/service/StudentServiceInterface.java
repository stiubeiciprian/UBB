package ubb.core.service;

import ubb.core.model.Student;

import java.util.List;
import java.util.Optional;

public interface StudentServiceInterface {
     void addStudent(Student student);
     void updateStudent(Student student);
     void deleteStudent(Long studentId);
     List<Student> getAllStudents();
     List<Student> filterStudentsByName(String s);
     Optional<Student> getStudentById(Long id);
}
