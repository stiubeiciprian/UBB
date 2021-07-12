 package ubb.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ubb.core.model.Student;
import ubb.core.service.StudentServiceInterface;
import ubb.web.converter.StudentConverter;
import ubb.web.dto.StudentDto;
import ubb.web.dto.StudentsDto;

@RestController
public class StudentController {
    public static final Logger logger = LoggerFactory.getLogger(StudentController.class);

    @Autowired
    private StudentServiceInterface studentService;

    @Autowired
    private StudentConverter studentConverter;


    @RequestMapping(value = "/students", method = RequestMethod.GET)
    StudentsDto getStudents() {
        return new StudentsDto(studentConverter.convertModelsToDtos(studentService.getAllStudents()));
    }

    @RequestMapping(value = "/students", method = RequestMethod.POST)
    StudentDto addStudent(@RequestBody StudentDto studentDto) {

        Student student = studentConverter.convertDtoToModel(studentDto);
        studentService.addStudent(student);

        logger.trace("Added student " + student.toString());

        return studentDto;
    }

    @RequestMapping(value = "/students/{id}", method = RequestMethod.PUT)
    StudentDto updateStudent(@PathVariable Long id, @RequestBody StudentDto studentDto) {

        Student student = studentConverter.convertDtoToModel(studentDto);
        studentService.updateStudent(student);

        logger.trace("Updated student " + student.toString());
        return studentDto;
    }

    @RequestMapping(value = "/students/{id}", method = RequestMethod.DELETE)
    ResponseEntity<?> deleteStudent(@PathVariable Long id){
        studentService.deleteStudent(id);
        logger.trace("Deleted student with id: " + id);
        return new ResponseEntity<>(HttpStatus.OK);
    }
}
