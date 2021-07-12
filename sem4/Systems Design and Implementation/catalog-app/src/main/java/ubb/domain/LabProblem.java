package ubb.domain;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "problem", schema = "public")
public class LabProblem extends BaseEntity<Long>{

    @Column(name = "description")
    private String description;

    @Column(name = "number")
    private int number;

    public LabProblem() {

    }

    public LabProblem(String description, int number) {
        this.description = description;
        this.number = number;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    @Override
    public String toString() {
        return "Problem{" +
                "number='" + number + '\'' +
                ", description=" + description +
                "} " + super.toString();
    }
}
