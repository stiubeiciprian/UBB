package ubb.core.model;

import lombok.*;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "problem", schema = "public")
@NoArgsConstructor
@AllArgsConstructor
@Data
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true)
@Builder
public class LabProblem extends BaseEntity<Long>{

    @Column(name = "description")
    private String description;

    @Column(name = "number")
    private int number;
}
