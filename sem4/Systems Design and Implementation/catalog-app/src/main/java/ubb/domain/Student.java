package ubb.domain;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "student", schema = "public")
public class Student extends BaseEntity<Long>{

    @Column(name = "serial_number")
    private String serialNumber;

    @Column(name = "name")
    private String name;

    @Column(name = "\"group\"")
    private int group;

    public Student() {

    }

    public Student(String serialNumber, String name, int group) {
        this.serialNumber = serialNumber;
        this.name = name;
        this.group = group;
    }

    public String getSerialNumber() {
        return serialNumber;
    }

    public void setSerialNumber(String serialNumber) {
        this.serialNumber = serialNumber;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getGroup() {
        return group;
    }

    public void setGroup(int group) {
        this.group = group;
    }

    @Override
    public String toString() {
        return "Student{" +
                "serialNumber='" + serialNumber + '\'' +
                ", name='" + name + '\'' +
                ", group=" + group +
                "} " + super.toString();
    }
}
