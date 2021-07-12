package ubb.web.dto;

import lombok.*;

@NoArgsConstructor
@AllArgsConstructor
@Data
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true)
@Builder
public class GradeDto extends BaseDto {
    private Long studentId;
    private Long problemId;
    private Float value;
}
