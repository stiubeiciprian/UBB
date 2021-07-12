package ubb.core.validators;

import org.springframework.stereotype.Component;
import ubb.core.model.Student;

@Component
public class StudentValidator implements Validator<Student> {
    @Override
    public void validate(Student entity) throws ValidatorException {
        if (entity.getName().isEmpty()) {
            throw new ValidatorException("Student name must not be empty.");
        }

        if (!entity.getName().matches("^[a-zA-Z]+")) {
            throw new ValidatorException("Student name must contain only letters.");
        }

        if (entity.getSerialNumber().isEmpty()) {
            throw new ValidatorException("Student serial number must not be empty.");
        }

        if (entity.getGroup() < 0) {
            throw new ValidatorException("Student group must be greater than 0.");
        }
    }
}

