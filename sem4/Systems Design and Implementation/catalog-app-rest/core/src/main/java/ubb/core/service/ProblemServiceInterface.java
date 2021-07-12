package ubb.core.service;

import ubb.core.model.LabProblem;

import java.util.List;
import java.util.Optional;

public interface ProblemServiceInterface {
     void addProblem(LabProblem problem);
     void deleteProblem(LabProblem problem);
     void updateProblem(LabProblem problem);
     List<LabProblem> getAllProblems();
     Optional<LabProblem> getProblemById(Long id);
}