package ubb.domain;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "grade", schema = "public")
public class Grade extends BaseEntity<Long> {

    @Column(name = "student_id")
    private Long studentId;

    @Column(name = "problem_id")
    private Long problemId;

    @Column(name = "value")
    private Float value;

    public Grade() {
    }

    public Grade(Long studentId, Long problemId, Float value) {
        this.studentId = studentId;
        this.problemId = problemId;
        this.value = value;
    }

    public Long getStudentId() {
        return studentId;
    }

    public void setStudentId(Long studentId) {
        this.studentId = studentId;
    }

    public Long getProblemId() {
        return problemId;
    }

    public void setProblemId(Long problemId) {
        this.problemId = problemId;
    }

    public Float getValue() {
        return value;
    }

    public void setValue(Float value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return "Grade{" +
                "studentId='" + studentId + '\'' +
                ", problemId='" + problemId + '\'' +
                ", grade='" + value + '\'' +
                "} " + super.toString();
    }
}