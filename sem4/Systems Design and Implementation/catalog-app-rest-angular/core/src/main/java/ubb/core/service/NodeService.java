package ubb.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import ubb.core.model.Node;
import ubb.core.repository.NodeRepository;
import ubb.core.validators.CatalogException;
import ubb.core.validators.NodeValidator;

import java.util.List;

public class NodeService implements NodeServiceInterface {

    @Autowired
    private NodeRepository nodeRepository;

    @Autowired
    private NodeValidator validator;

    private Logger logger = LoggerFactory.getLogger(NodeService.class);

    @Override
    public void add(String name, Integer totalCapacity) {
        try {
            Node node = Node.builder()
                    .name(name)
                    .totalCapacity(totalCapacity)
                    .build();

            validator.validate(node);
            nodeRepository.save(node);
        } catch (Exception e) {
            logger.error("addNode failed", e);
            throw e;
        }

        logger.info("Added node " + name);
    }

    @Override
    public List<Node> getNodes() {
        return nodeRepository.findAll();
    }

    @Override
    public Node update(String name, Integer totalCapacity) {
        Node node = null;
        try {
            node = Node.builder()
                    .name(name)
                    .totalCapacity(totalCapacity)
                    .build();

            validator.validate(node);
            node = nodeRepository.save(node);
        } catch (Exception e) {
            logger.error("updateNode failed", e);
        }
        logger.info("Updated node" + name);
        return node;
    }

    @Override
    public List<Node> getAvailableNodes() {
        return null;
    }

    @Override
    public Integer trySchedulePod(Long nodeId, Long podId) {
        return null;
    }

    @Override
    public void deleteSchedule(Long nodeId, Long podId) {
        return;
    }
}
