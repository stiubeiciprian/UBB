package ubb.client.ui;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;
import ubb.core.model.LabProblem;
import ubb.web.dto.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

@Component
public class Console {
    public static final String URL_STUDENTS = "http://localhost:8080/api/students";
    public static final String URL_PROBLEMS = "http://localhost:8080/api/problems";
    public static final String URL_GRADES = "http://localhost:8080/api/grades";

    @Autowired
    RestTemplate restTemplate;

    private void printMenu() {
        String menu = "0.Exit." + "\n" +
                "1.Add student." +  "\n" +
                "2.Update Student." + "\n" +
                "3.Delete student." + "\n" +
                "4.Print all students." + "\n" +
                "---------------" + "\n" +
                "5.Add problem." + "\n" +
                "6.Update problem." + "\n" +
                "7.Delete problem." + "\n" +
                "8.Print all problems." + "\n" +
                "---------------" + "\n" +
                "9.Add grade." + "\n" +
                "10.Update grade." + '\n' +
                "11.Delete grade." + '\n' +
                "12.Print all grades.";

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
                        updateStudent();
                        break;
                    case 3:
                        deleteStudent();
                        break;
                    case 4:
                        printAllStudents();
                        break;
                    case 5:
                        addLabProblem();
                        break;
                    case 6:
                        updateLabProblem();
                        break;
                    case 7:
                        deleteLabProblem();
                        break;
                    case 8:
                        printAllProblems();
                        break;
                    case 9:
                        addGrade();
                        break;
                    case 10:
                        updateGrade();
                        break;
                    case 11:
                        deleteGrade();
                        break;
                    case 12:
                        printAllGrades();
                        break;
                    case 0:
                        return;
                }

            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }


    private void printAllStudents() {
        StudentsDto allStudents = restTemplate.getForObject(URL_STUDENTS, StudentsDto.class);
        allStudents.getStudents().forEach(System.out::println);
    }

    private void addStudent() {
        StudentDto student = readStudent();
        restTemplate.postForObject(
                URL_STUDENTS,
                student,
                StudentDto.class);
    }

    private void updateStudent(){
        System.out.println("Update student");
        try {
            StudentDto student = readStudent();
            restTemplate.put(URL_STUDENTS + "/{id}", student, student.getId());
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
            restTemplate.delete(URL_STUDENTS + "/{id}", id);

            GradesDto allGrades = restTemplate.getForObject(URL_GRADES, GradesDto.class);
            for (GradeDto grade : allGrades.getGrades()) {
                if (grade.getStudentId().equals(id)) {
                    restTemplate.delete(URL_GRADES + "/{id}", grade.getId());
                }
            }
        }
        catch (Exception e){
            e.printStackTrace();
            System.out.println("Invalid input!");
        }
    }

    private StudentDto readStudent() {
        System.out.println("Read student {serialNumber, name, group}");

        BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));
        try {
            String serialNumber = bufferRead.readLine();
            String name = bufferRead.readLine();
            int group = Integer.parseInt(bufferRead.readLine());

            StudentDto student = new StudentDto(serialNumber, name, group);
            return student;
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return null;
    }

    private void addLabProblem() {
        ProblemDto problem = readLabProblem();
        restTemplate.postForObject(
                URL_PROBLEMS,
                problem,
                ProblemDto.class);
    }

    private ProblemDto readLabProblem() {
        System.out.println("Read problem {number, description}");

        BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));

        try {
            int number = Integer.parseInt(bufferRead.readLine());
            String description = bufferRead.readLine();
            ProblemDto labProblem = new ProblemDto(description, number);

            return labProblem;
        } catch (IOException ex) {
            ex.printStackTrace();
        }

        return null;
    }

    private void printAllProblems() {
        ProblemsDto allProblems = restTemplate.getForObject(URL_PROBLEMS, ProblemsDto.class);
        System.out.println(allProblems);
    }

    private void updateLabProblem(){
        System.out.println("Update lab problem");
        try {
            ProblemDto labProblem = readLabProblem();
            restTemplate.put(URL_PROBLEMS + "/{id}", labProblem, labProblem.getId());
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
            restTemplate.delete(URL_PROBLEMS + "/{id}", id);

            GradesDto allGrades = restTemplate.getForObject(URL_GRADES, GradesDto.class);
            for (GradeDto grade : allGrades.getGrades()) {
                if (grade.getProblemId().equals(id)) {
                    restTemplate.delete(URL_GRADES + "/{id}", grade.getId());
                }
            }
        }
        catch (Exception e){
            System.out.println("Invalid input!");
        }
    }

    private GradeDto readGrade() {
        System.out.println("Read grade {studentId, problemId, grade}");

        BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));
        try {
            Long studentId = Long.valueOf(bufferRead.readLine());
            Long problemId = Long.valueOf(bufferRead.readLine());
            Float value = Float.valueOf(bufferRead.readLine());

            GradeDto grade = new GradeDto(studentId, problemId, value);

            return grade;
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return null;
    }

    private void addGrade() {
        GradeDto grade = readGrade();
        restTemplate.postForObject(
                URL_GRADES,
                grade,
                GradeDto.class);
    }

    private void printAllGrades() {
        GradesDto allGrades = restTemplate.getForObject(URL_GRADES, GradesDto.class);
        System.out.println(allGrades);
    }

    private void updateGrade(){
        System.out.println("Update grade: ");
        try {
            GradeDto grade = readGrade();
            restTemplate.put(URL_GRADES + "/{id}", grade, grade.getId());
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

            restTemplate.delete(URL_GRADES + "/{id}", id);
        }
        catch (Exception e){
            System.out.println("Invalid input!");
        }
    }
}