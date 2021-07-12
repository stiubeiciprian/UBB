package ubb.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ubb.core.model.LabProblem;
import ubb.core.repository.ProblemRepository;
import ubb.core.validators.LabProblemValidator;
import ubb.core.validators.ValidatorException;

import java.util.List;
import java.util.Optional;

@Service
public class ProblemService implements ProblemServiceInterface {

    @Autowired
    private ProblemRepository repository;

    @Autowired
    private LabProblemValidator validator;

    private Logger logger = LoggerFactory.getLogger(ProblemService.class);


    public void addProblem(LabProblem problem) throws ValidatorException {
        try {
            validator.validate(problem);
            repository.save(problem);
        } catch (Exception e) {
            logger.error("addProblem failed:", e);
        }
        logger.info("Added problem " + problem);
    }

    public void deleteProblem(LabProblem problem) throws ValidatorException {
        try {
            repository.delete(problem);
        } catch (Exception e) {
            logger.error("deleteProblem failed:", e);
        }
        logger.info("Deleted problem with id " + problem.getId());
    }

    public void updateProblem(LabProblem problem) throws ValidatorException {
        try {
            validator.validate(problem);
            repository.save(problem);
        } catch (Exception e) {
            logger.error("updateProblem failed:", e);
        }
        logger.info("Updated problem " + problem);
    }

    public List<LabProblem> getAllProblems() {
      return repository.findAll();
    }

    public Optional<LabProblem> getProblemById(Long id) {
        return this.repository.findById(id);
    }
}
