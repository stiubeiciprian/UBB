import {Component, OnInit} from '@angular/core';
import {Student} from "../shared/student.model";
import {StudentService} from "../shared/student.service";
import {Router} from "@angular/router";


@Component({
  moduleId: module.id,
  selector: 'ubb-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.css'],
})
export class StudentListComponent implements OnInit {
  errorMessage: string;
  students: Array<Student>;

  constructor(private studentService: StudentService,
              private router: Router) {
  }

  ngOnInit(): void {
    this.getStudents();
  }

  getStudents() {
    this.studentService.getStudents()
      .subscribe(
        students => this.students = students,
        error => this.errorMessage = <any>error
      );
  }

  onSelect(student: Student): void {
    this.router.navigate(['/student/detail', student.id]);
  }

  addStudent(): void {
    this.router.navigate(['/student/add']);
  }

}
