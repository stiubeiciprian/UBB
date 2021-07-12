package ubb.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ubb.core.model.Student;
import ubb.core.repository.StudentRepository;
import ubb.core.validators.StudentValidator;
import ubb.core.validators.ValidatorException;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;


@Service
public class StudentService implements StudentServiceInterface{
    @Autowired
    private StudentValidator validator;
    
    @Autowired
    private StudentRepository repository;

    private Logger logger = LoggerFactory.getLogger(StudentService.class);

    public void addStudent(Student student) throws ValidatorException {
        try {
            validator.validate(student);
            repository.save(student);
        } catch (Exception e) {
            logger.error("addStudent failed:", e);
            throw e;
        }
        logger.info("Added student: " + student.toString() + " to the database;");
    }

    public void updateStudent(Student student) {
        try {
        validator.validate(student);
        repository.save(student);
        } catch (Exception e) {
            logger.error("updateStudent failed:", e);
        }
        logger.info("Updated student: " + student.toString() + ";");
    }

    public void deleteStudent(Long studentId) {
        try {
            repository.deleteById(studentId);
        } catch (Exception e) {
            logger.error("deleteStudent failed:", e);
        }
        logger.info("Student with id: " + studentId.toString() + " was deleted from the database;");
    }

    public List<Student> getAllStudents() {
        List<Student> students = repository.findAll();
        logger.info("Fetched students: " + students);
        return students;
    }

    public List<Student> filterStudentsByName(String s) {
        List<Student> students =  repository.findAll().stream().filter(student -> student.getName().contains(s)).collect(Collectors.toList());
        logger.info("Filtered students by name: " + students);
        return students;
    }

    public Optional<Student> getStudentById(Long id) {
        return this.repository.findById(id);
    }
}
