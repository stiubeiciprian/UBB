package ubb.ui;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import ubb.domain.Grade;
import ubb.domain.LabProblem;
import ubb.domain.Student;
import ubb.domain.validators.ValidatorException;
import ubb.service.GradeService;
import ubb.service.ProblemService;
import ubb.service.StudentService;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.Scanner;

@Component
public class Console {
    @Autowired
    private StudentService studentService;

    @Autowired
    private ProblemService problemService;

    @Autowired
    private GradeService gradeService;

    public Console(StudentService studentService, ProblemService problemService, GradeService gradeService) {
        this.studentService = studentService;
        this.problemService = problemService;
        this.gradeService = gradeService;
    }

    private void printMenu() {
        String menu = "0.Exit." + "\n" +
                "1.Add student." +  "\n" +
                "2.Filter students by name." + "\n" +
                "3.Update Student." + "\n" +
                "4.Delete student." + "\n" +
                "5.Print all students." + "\n" +
                "---------------" + "\n" +
                "6.Add problem." + "\n" +
                "7.Filter problem." + "\n" +
                "8.Update problem." + "\n" +
                "9.Delete problem." + "\n" +
                "10.Print all problems." + "\n" +
                "---------------" + "\n" +
                "11.Add grade." + "\n" +
                "12.Print all grades." + '\n' +
                "13.Update grade." + '\n' +
                "14.Delete grade." + '\n' +
                "15.Filter grade." + '\n' +
                "---------------" + '\n' +
                "16.Get top N grades." + '\n' +
                "17.Get top students for problem";

        System.out.println(menu);
    }

    public void runConsole() {
        Scanner scanner = new Scanner(System.in);

        while(true) {
            printMenu();
            int command = scanner.nextInt();
            try {
                switch (command) {
                    case 1:
                        addStudent();
                        break;
                    case 2:
                        filterStudents();
                        break;
                    case 3:
                        updateStudent();
                        break;
                    case 4:
                        deleteStudent();
                        break;
                    case 5:
                        printAllStudents();
                        break;
                    case 6:
                        addLabProblem();
                        break;
                    case 7:
                        filterStudents();
                        break;
                    case 8:
                        updateLabProblem();
                        break;
                    case 9:
                        deleteLabProblem();
                        break;
                    case 10:
                        printAllProblems();
                        break;
                    case 11:
                        addGrade();
                        break;
                    case 12:
                        printAllGrades();
                        break;
                    case 13:
                        updateGrade();
                        break;
                    case 14:
                        deleteGrade();
                        break;
                    case 15:
                        filterGrades();
                        break;
                    case 16:
                        getHighestNGrades();
                        break;
                    case 17:
                        getTopStudentsForProblem();
                        break;
                    case 0:
                        return;
                }

            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }

    private void getTopStudentsForProblem() {
        try {
            Integer n;
            Scanner in = new Scanner(System.in);
            System.out.println("Enter problem number: ");
            n = in.nextInt();
            System.out.println("Top students for selected problem:");

            gradeService.getTopStudentsForProblem(n).forEach(System.out::println);
        }
        catch (Exception e){
            System.out.println("Invalid input!");
        }
    }

    private void getHighestNGrades() {
        try {
            Integer n;
            Scanner in = new Scanner(System.in);
            System.out.println("Enter number of grades: ");
            n = in.nextInt();
            System.out.println("Top grades:");

            gradeService.getHighestNGrades(n).forEach(System.out::println);
        }
        catch (Exception e){
            System.out.println("Invalid input!");
        }
    }

    private void filterStudents() {
        String filter;
        System.out.println("Enter filter string:");
        BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));
        try {
            filter = bufferRead.readLine();
        } catch (IOException e) {
            return;
        }
        System.out.println("Filtered students (name containing " + filter + "):");
        List<Student> students = studentService.filterStudentsByName(filter);
        students.stream().forEach(System.out::println);
    }

    private void printAllStudents() {
        List<Student> students = studentService.getAllStudents();
        students.stream().forEach(System.out::println);
    }

    private void addStudent() {
        Student student = readStudent();
        try {
            studentService.addStudent(student);
        } catch (ValidatorException e) {
            e.printStackTrace();
        }
    }

    private void updateStudent(){
        System.out.println("Update student");
        try {
            Student student = readStudent();
            studentService.updateStudent(student);
        }
        catch (Exception e){
            System.out.println("Invalid input!");
        }
    }

    private void deleteStudent(){
        System.out.println("Delete student");
        try {
            String sid;
            Scanner in = new Scanner(System.in);
            System.out.println("Id: ");
            sid = in.nextLine();
            Long id = Long.valueOf(sid);
            studentService.deleteStudent(id);

            for (Grade grade : gradeService.getAllGrades()) {
                if (grade.getStudentId().equals(id)) {
                    Grade g = new Grade(0L, 0L, 0f);
                    g.setId(grade.getId());
                    gradeService.deleteGrade(g);
                }
            }
        }
        catch (Exception e){
            e.printStackTrace();
            System.out.println("Invalid input!");
        }
    }

    private Student readStudent() {
        System.out.println("Read student {serialNumber, name, group}");

        BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));
        try {
            String serialNumber = bufferRead.readLine();
            String name = bufferRead.readLine();
            int group = Integer.parseInt(bufferRead.readLine());

            Student student = new Student(serialNumber, name, group);
            return student;
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return null;
    }

    private void addLabProblem() {
        LabProblem labProblem = readLabProblem();
        try {
            problemService.addProblem(labProblem);
        } catch (ValidatorException e) {
            e.printStackTrace();
        }
    }

    private LabProblem readLabProblem() {
        System.out.println("Read problem {number, description}");

        BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));

        try {
            int number = Integer.parseInt(bufferRead.readLine());
            String description = bufferRead.readLine();
            LabProblem labProblem = new LabProblem(description, number);

            return labProblem;
        } catch (IOException ex) {
            ex.printStackTrace();
        }

        return null;
    }

    private void printAllProblems() {
        List<LabProblem> problems = problemService.getAllProblems();
        problems.stream().forEach(System.out::println);
    }

    private void updateLabProblem(){
        System.out.println("Update lab problem");
        try {
            LabProblem labProblem = readLabProblem();
            problemService.updateProblem(labProblem);
        }
        catch (Exception e){
            System.out.println("Invalid input!");
        }
    }

    private void deleteLabProblem(){
        System.out.println("Delete lab problem");
        try {
            String sid;
            Scanner in = new Scanner(System.in);
            System.out.println("Id: ");
            sid = in.nextLine();
            Long id = Long.valueOf(sid);
            LabProblem labProblem = new LabProblem("", 0);
            labProblem.setId(id);
            problemService.deleteProblem(labProblem);

            for (Grade grade : gradeService.getAllGrades()) {
                if (grade.getProblemId().equals(id)) {
                    Grade g = new Grade(0L, 0L, 0f);
                    g.setId(grade.getId());
                    gradeService.deleteGrade(g);
                }
            }
        }
        catch (Exception e){
            System.out.println("Invalid input!");
        }
    }

    private Grade readGrade() {
        System.out.println("Read grade {studentId, problemId, grade}");

        BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));
        try {
            Long studentId = Long.valueOf(bufferRead.readLine());
            Long problemId = Long.valueOf(bufferRead.readLine());
            Float value = Float.valueOf(bufferRead.readLine());

            Grade grade = new Grade(studentId, problemId, value);

            return grade;
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return null;
    }

    private void addGrade() {
        Grade grade = readGrade();
        try {
            gradeService.addGrade(grade);
        } catch (ValidatorException e) {
            e.printStackTrace();
        }
    }

    private void printAllGrades() {
        List<Grade> grades = gradeService.getAllGrades();
        grades.stream().forEach(System.out::println);
    }

    private void updateGrade(){
        System.out.println("Update grade: ");
        try {
            Grade grade = readGrade();
            gradeService.updateGrade(grade);
        }
        catch (Exception e){
            System.out.println("Invalid input!");
        }
    }

    private void deleteGrade(){
        System.out.println("Delete grade.");
        try {
            String sid;
            Scanner in = new Scanner(System.in);
            System.out.println("Id: ");
            sid = in.nextLine();
            Long id = Long.valueOf(sid);
            Grade grade = new Grade(0L,0L,0f);
            grade.setId(id);
            gradeService.deleteGrade(grade);
        }
        catch (Exception e){
            System.out.println("Invalid input!");
        }
    }

    private void filterGrades() {
        Float value;
        System.out.println("Enter filter grade:");
        BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));
        try {
            value = Float.valueOf(bufferRead.readLine());
            gradeService.filterGradesByValue(value);
        } catch (IOException e) {
            return;
        }
        System.out.println("Filtered grades (grade containing " + value + "):");
        List<Grade> grades = gradeService.filterGradesByValue(value);
        grades.stream().forEach(System.out::println);
    }
}