import {Component, Input, OnInit} from '@angular/core';
import {Student} from "../shared/student.model";
import {ActivatedRoute} from "@angular/router";
import {Location} from "@angular/common";
import {StudentService} from "../shared/student.service";

@Component({
  selector: 'app-student-form',
  templateUrl: './student-form.component.html',
  styleUrls: ['./student-form.component.css']
})
export class StudentFormComponent implements OnInit {

  @Input() student: Student;

  constructor(private studentService: StudentService,
              private  route: ActivatedRoute,
              private location: Location) { }


  ngOnInit(): void {
    this.student = new Student();
  }

  goBack(): void {
    this.location.back();
  }

  save(): void {
    this.studentService.save(this.student)
      .subscribe(_ => this.goBack());
  }

}
