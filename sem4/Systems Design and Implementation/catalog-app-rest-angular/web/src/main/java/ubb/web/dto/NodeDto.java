package ubb.web.dto;

import lombok.*;

@NoArgsConstructor
@AllArgsConstructor
@Data
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true)
@Builder
public class NodeDto extends BaseDto {
    private Integer totalCapacity;
    private String name;
}