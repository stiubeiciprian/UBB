package ubb.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ubb.core.model.Grade;
import ubb.core.model.Student;
import ubb.core.repository.GradeRepository;
import ubb.core.validators.CatalogException;
import ubb.core.validators.GradeValidator;
import ubb.core.validators.ValidatorException;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class GradeService implements GradeServiceInterface{
    @Autowired
    private GradeRepository repository;

    @Autowired
    private GradeValidator validator;

    @Autowired
    private ProblemServiceInterface problemService;

    @Autowired
    private StudentServiceInterface studentService;

    private Logger logger = LoggerFactory.getLogger(ProblemService.class);

    public void addGrade(Grade grade) throws ValidatorException, CatalogException {
        try {
            validator.validate(grade);

            if (problemService.getProblemById(grade.getProblemId()).isEmpty() || studentService.getStudentById(grade.getStudentId()).isEmpty()) {
                throw new CatalogException("Invalid id!");
            }

            long grades = getAllGrades().stream()
                    .filter(g -> g.getStudentId().equals(grade.getStudentId()))
                    .filter(g -> g.getProblemId().equals(grade.getProblemId()))
                    .count();

            if(grades != 0) {
                throw new ValidatorException("Grade already assigned!");
            }

            repository.save(grade);
        } catch (Exception e) {
            logger.error("addGrade failed", e);
            throw e;
        }

        logger.info("Added grade " + grade);
    }


    public List<Grade> getAllGrades() {
        return repository.findAll();
    }

    public List<Grade> getHighestNGrades(int n) {
        return getAllGrades().stream()
                .sorted((o1, o2) -> -1 * o1.getValue().compareTo(o2.getValue()))
                .limit(n)
                .collect(Collectors.toList());
    }

    public List<Student> getTopStudentsForProblem(int number) {
        return getAllGrades().stream()
                .sorted((o1, o2) -> -1 * o1.getValue().compareTo(o2.getValue()))
                .filter(e -> problemService.getProblemById(e.getProblemId()).get().getNumber() == number)
                .map(s -> studentService.getStudentById(s.getStudentId()).get())
                .collect(Collectors.toList());
    }

    public void updateGrade(Grade grade) throws ValidatorException {
        try {
            validator.validate(grade);
            repository.save(grade);
        } catch (Exception e) {
            logger.error("updateGrade failed", e);
        }
        logger.info("Updated grade" + grade);
    }

    public List<Grade> filterGradesByValue(Float val) {
        return repository.findAll().stream().filter(grade -> grade.getValue().equals(val)).collect(Collectors.toList());
    }

    public void deleteGrade(Grade grade) {
        try {
            repository.delete(grade);
        } catch (Exception e) {
            logger.error("deleteGrade failed", e);
        }

        logger.info("Deleted grade with id " + grade.getId());
    }
}
