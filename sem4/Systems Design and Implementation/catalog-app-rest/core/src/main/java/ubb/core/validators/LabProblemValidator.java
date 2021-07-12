package ubb.core.validators;

import org.springframework.stereotype.Component;
import ubb.core.model.LabProblem;

@Component
public class LabProblemValidator implements Validator<LabProblem>{
    @Override
    public void validate(LabProblem entity) throws ValidatorException {
        StringBuilder s = new StringBuilder();
        if(entity.getNumber() < 0)
            s.append("Invalid problem number");

        if(entity.getDescription().isEmpty())
            s.append("Invalid problem statement");

        if(s.length() > 0)
            throw new ValidatorException(s.toString());
    }
}
