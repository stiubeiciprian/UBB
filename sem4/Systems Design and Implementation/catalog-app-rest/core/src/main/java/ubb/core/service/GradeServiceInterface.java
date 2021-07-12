package ubb.core.service;

import ubb.core.model.Grade;
import ubb.core.model.Student;

import java.util.List;

public interface GradeServiceInterface {
     void addGrade(Grade grade);
     List<Grade> getAllGrades();
     List<Student> getTopStudentsForProblem(int number);
     void updateGrade(Grade grade);
     List<Grade> filterGradesByValue(Float val);
     void deleteGrade(Grade grade);
}
