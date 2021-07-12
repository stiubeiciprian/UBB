package ubb.domain.validators;

import org.springframework.stereotype.Component;
import ubb.domain.Grade;

@Component
public class GradeValidator implements Validator<Grade> {
    @Override
    public void validate(Grade entity) throws ValidatorException {
        if(entity.getProblemId() == null) {
            throw new ValidatorException("Problem id must not be null.");
        }

        if(entity.getStudentId() == null) {
            throw new ValidatorException("Student id must not be null.");
        }

        if (entity.getValue() == null) {
            throw new ValidatorException("Grade value must not be null.");
        }

        if(entity.getValue() > 10 || entity.getValue() < 0) {
            throw new ValidatorException("Grade value must be between 0 and 10.");
        }
    }
}