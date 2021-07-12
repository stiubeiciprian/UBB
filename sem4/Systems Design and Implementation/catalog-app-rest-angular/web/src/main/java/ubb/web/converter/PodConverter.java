package ubb.web.converter;

import org.springframework.stereotype.Component;
import ubb.core.model.Pod;
import ubb.web.dto.PodDto;

@Component
public class PodConverter extends BaseConverter<Pod, PodDto> {

    @Override
    public Pod convertDtoToModel(PodDto dto) {
        Pod pod = Pod.builder()
                .name(dto.getName())
                .cost(dto.getCost())
                .build();
        pod.setId(dto.getId());
        return pod;
    }

    @Override
    public PodDto convertModelToDto(Pod pod) {
        PodDto dto = PodDto.builder()
                .name(pod.getName())
                .cost(pod.getCost())
                .build();
        dto.setId(pod.getId());
        return dto;
    }
}
