package ubb.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ubb.core.model.Grade;
import ubb.core.service.GradeServiceInterface;
import ubb.web.converter.GradeConverter;
import ubb.web.dto.GradeDto;
import ubb.web.dto.GradesDto;

@RestController
public class GradeController {
    public static final Logger logger = LoggerFactory.getLogger(Grade.class);

    @Autowired
    private GradeServiceInterface gradeService;

    @Autowired
    private GradeConverter gradeConverter;


    @RequestMapping(value = "/grades", method = RequestMethod.GET)
    GradesDto getGrades() {
        return new GradesDto(gradeConverter.convertModelsToDtos(gradeService.getAllGrades()));
    }

    @RequestMapping(value = "/grades", method = RequestMethod.POST)
    GradeDto addGrade(@RequestBody GradeDto gradeDto) {

        Grade grade = gradeConverter.convertDtoToModel(gradeDto);
        gradeService.addGrade(grade);

        logger.info("Added grade " + grade.toString());

        return gradeDto;
    }

    @RequestMapping(value = "/grades/{id}", method = RequestMethod.PUT)
    GradeDto updateGrade(@PathVariable Long id, @RequestBody GradeDto gradeDto) {

        Grade grade = gradeConverter.convertDtoToModel(gradeDto);
        gradeService.updateGrade(grade);

        logger.info("Updated grade " + grade.toString());
        return gradeDto;
    }

    @RequestMapping(value = "/grades/{id}", method = RequestMethod.DELETE)
    ResponseEntity<?> deleteGrade(@PathVariable Long id){
        Grade grade = new Grade();
        grade.setId(id);
        gradeService.deleteGrade(grade);
        logger.info("Deleted grade with id: " + id);
        return new ResponseEntity<>(HttpStatus.OK);
    }
}
