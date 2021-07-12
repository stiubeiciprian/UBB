package ubb.web.converter;

import org.springframework.stereotype.Component;
import ubb.core.model.Student;
import ubb.web.dto.StudentDto;


@Component
public class StudentConverter extends BaseConverter<Student, StudentDto> {
    @Override
    public Student convertDtoToModel(StudentDto dto) {
        Student student = Student.builder()
                .serialNumber(dto.getSerialNumber())
                .name(dto.getName())
                .group(dto.getGroup())
                .build();
        student.setId(dto.getId());
        return student;
    }

    @Override
    public StudentDto convertModelToDto(Student student) {
        StudentDto dto = StudentDto.builder()
                .serialNumber(student.getSerialNumber())
                .name(student.getName())
                .group(student.getGroup())
                .build();
        dto.setId(student.getId());
        return dto;
    }
}
