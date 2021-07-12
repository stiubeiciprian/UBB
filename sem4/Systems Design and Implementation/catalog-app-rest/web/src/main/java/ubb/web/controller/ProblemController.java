package ubb.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ubb.core.model.LabProblem;
import ubb.core.service.ProblemServiceInterface;
import ubb.web.converter.ProblemConverter;
import ubb.web.dto.ProblemDto;
import ubb.web.dto.ProblemsDto;

@RestController
public class ProblemController {

    public static final Logger logger = LoggerFactory.getLogger(ProblemController.class);

    @Autowired
    private ProblemServiceInterface problemService;

    @Autowired
    private ProblemConverter problemConverter;


    @RequestMapping(value = "/problems", method = RequestMethod.GET)
    ProblemsDto getProblems() {
        return new ProblemsDto(problemConverter.convertModelsToDtos(problemService.getAllProblems()));
    }

    @RequestMapping(value = "/problems", method = RequestMethod.POST)
    ProblemDto addStudent(@RequestBody ProblemDto problemDto) {

        LabProblem problem = problemConverter.convertDtoToModel(problemDto);
        problemService.addProblem(problem);

        logger.info("Added problem " + problem.toString());

        return problemDto;
    }

    @RequestMapping(value = "/problems/{id}", method = RequestMethod.PUT)
    ProblemDto updateStudent(@PathVariable Long id, @RequestBody ProblemDto problemDto) {

        LabProblem problem = problemConverter.convertDtoToModel(problemDto);
        problemService.updateProblem(problem);

        logger.info("Updated problem " + problem.toString());
        return problemDto;
    }

    @RequestMapping(value = "/problems/{id}", method = RequestMethod.DELETE)
    ResponseEntity<?> deleteStudent(@PathVariable Long id){
        LabProblem problem = new LabProblem("",0);
        problem.setId(id);
        problemService.deleteProblem(problem);

        logger.info("Deleted problem with id: " + id);
        return new ResponseEntity<>(HttpStatus.OK);
    }
}
