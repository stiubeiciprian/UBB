package ubb.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ubb.core.model.Node;
import ubb.core.service.NodeServiceInterface;
import ubb.web.converter.NodeConverter;
import ubb.web.dto.NodeDto;

import java.util.List;

@RestController
public class NodeController {
    public static final Logger logger = LoggerFactory.getLogger(NodeController.class);

    @Autowired
    private NodeServiceInterface nodeService;

    @Autowired
    private NodeConverter nodeConverter;


    @RequestMapping(value = "/nodes", method = RequestMethod.GET)
    List<NodeDto> getNodes() {
        return nodeConverter.convertModelsToDtos(nodeService.getNodes());
    }

    @RequestMapping(value = "/nodes", method = RequestMethod.POST)
    NodeDto addGrade(@RequestBody NodeDto nodeDto) {
        nodeService.add(nodeDto.getName(), nodeDto.getTotalCapacity());
        logger.info("Added grade " + nodeDto.getName());
        return nodeDto;
    }
}
