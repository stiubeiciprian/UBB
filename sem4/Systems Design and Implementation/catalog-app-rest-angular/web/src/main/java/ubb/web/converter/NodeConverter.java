package ubb.web.converter;

import org.springframework.stereotype.Component;
import ubb.core.model.Node;
import ubb.web.dto.NodeDto;

@Component
public class NodeConverter extends  BaseConverter<Node, NodeDto> {

    @Override
    public Node convertDtoToModel(NodeDto dto) {
        Node node = Node.builder()
                .name(dto.getName())
                .totalCapacity(dto.getTotalCapacity())
                .build();
        node.setId(dto.getId());
        return node;
    }

    @Override
    public NodeDto convertModelToDto(Node node) {
        NodeDto dto = NodeDto.builder()
                .name(node.getName())
                .totalCapacity(node.getTotalCapacity())
                .build();
        dto.setId(node.getId());
        return dto;
    }
}
