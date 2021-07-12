package ubb.core.model;

import lombok.*;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "grade", schema = "public")
@NoArgsConstructor
@AllArgsConstructor
@Data
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true)
@Builder
public class Grade extends BaseEntity<Long> {

    @Column(name = "student_id")
    private Long studentId;

    @Column(name = "problem_id")
    private Long problemId;

    @Column(name = "value")
    private Float value;
}