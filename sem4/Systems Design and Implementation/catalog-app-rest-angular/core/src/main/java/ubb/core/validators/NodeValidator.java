package ubb.core.validators;

import org.springframework.stereotype.Component;
import ubb.core.model.Node;

@Component
public class NodeValidator implements Validator<Node> {

    @Override
    public void validate(Node entity) throws ValidatorException {
        if(entity.getName() == null || entity.getTotalCapacity() == null) {
            throw new CatalogException("Node must not have empty fields.");
        }

        if(entity.getName().length() < 5) {
            throw new CatalogException("Node name must have at least 5 chars.");
        }

        if(entity.getTotalCapacity() <= 0) {
            throw new CatalogException("Node capacity must be equal or greater than 0.");
        }
    }
}
