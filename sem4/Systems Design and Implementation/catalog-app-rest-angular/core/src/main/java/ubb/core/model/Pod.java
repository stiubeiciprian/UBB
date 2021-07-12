package ubb.core.model;

import lombok.*;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "pod", schema = "public")
@NoArgsConstructor
@AllArgsConstructor
@Data
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true)
@Builder
public class Pod extends BaseEntity<Long> {
    
    @Column(name = "name", unique = true)
    String name;

    @Column(name = "cost")
    Integer cost;
}
