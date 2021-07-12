package ubb.web.converter;

import org.springframework.stereotype.Component;
import ubb.core.model.LabProblem;
import ubb.web.dto.ProblemDto;

@Component
public class ProblemConverter extends  BaseConverter<LabProblem, ProblemDto> {
    @Override
    public LabProblem convertDtoToModel(ProblemDto dto) {
        LabProblem problem = LabProblem.builder()
                .description(dto.getDescription())
                .number(dto.getNumber())
                .build();
        problem.setId(dto.getId());
        return problem;
    }

    @Override
    public ProblemDto convertModelToDto(LabProblem problem) {
        ProblemDto dto = ProblemDto.builder()
                .description(problem.getDescription())
                .number(problem.getNumber())
                .build();
        dto.setId(problem.getId());
        return dto;
    }
}
