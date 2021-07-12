package ubb.web.converter;

import org.springframework.stereotype.Component;
import ubb.core.model.Grade;
import ubb.web.dto.GradeDto;

@Component
public class GradeConverter extends BaseConverter<Grade, GradeDto>{
    @Override
    public Grade convertDtoToModel(GradeDto dto) {
        Grade grade = Grade.builder()
                .studentId(dto.getStudentId())
                .problemId(dto.getProblemId())
                .value(dto.getValue())
                .build();
        grade.setId(dto.getId());
        return grade;
    }

    @Override
    public GradeDto convertModelToDto(Grade grade) {
        GradeDto dto = GradeDto.builder()
                .studentId(grade.getStudentId())
                .problemId(grade.getProblemId())
                .value(grade.getValue())
                .build();
        dto.setId(grade.getId());
        return dto;
    }
}
