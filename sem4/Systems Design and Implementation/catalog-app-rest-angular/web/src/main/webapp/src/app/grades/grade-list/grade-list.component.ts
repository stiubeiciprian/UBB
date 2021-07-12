import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import {Grade} from "../../grades/shared/grade.model";
import {GradeService} from "../../grades/shared/grade.service";

@Component({
  selector: 'app-grade-list',
  templateUrl: './grade-list.component.html',
  styleUrls: ['./grade-list.component.css']
})
export class GradeListComponent implements OnInit {
  errorMessage: string;
  grades: Grade[];

  constructor(private gradeService: GradeService,
              private router: Router) { }

  ngOnInit(): void {
    this.getGrades();
  }

  getGrades() {
    this.gradeService.getGrades()
      .subscribe(
        grades => {this.grades = grades;     console.log(this.grades);},
        error => this.errorMessage = <any>error
      );
  }

  onSelect(grade: Grade) {
    this.router.navigate(['grade/detail', grade.id]);
  }

  addGrade() {
    this.router.navigate(['grade/add']);
  }

}

