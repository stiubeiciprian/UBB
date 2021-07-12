import {Component, Input, OnInit} from '@angular/core';
import {StudentService} from "../../students/shared/student.service";
import {ProblemService} from "../../problems/shared/problem.service";
import {Student} from "../../students/shared/student.model";
import {Problem} from "../../problems/shared/problem.model";
import {GradeService} from "../shared/grade.service";
import {Grade} from "../shared/grade.model";
import {ActivatedRoute} from "@angular/router";
import {Location} from "@angular/common";

@Component({
  selector: 'app-grade-form',
  templateUrl: './grade-form.component.html',
  styleUrls: ['./grade-form.component.css']
})
export class GradeFormComponent implements OnInit {

  errorMessage: string;
  students: Array<Student>;
  problems: Array<Problem>;
  grade: Grade;

  studentId: number;
  problemId: number;


  constructor(private studentService: StudentService,
              private problemService: ProblemService,
              private gradeService: GradeService,
              private  route: ActivatedRoute,
              private location: Location) { }

  ngOnInit(): void {
    this.grade = new Grade();
    this.getStudents();
    this.getProblems();
  }

  getStudents() {
    this.studentService.getStudents()
      .subscribe(
        students => this.students = students,
        error => this.errorMessage = <any>error
      );
  }

  getProblems() {
    this.problemService.getProblems()
      .subscribe(
        problems => this.problems = problems,
        error => this.errorMessage = <any>error
      );
  }

  addGrade() {
    this.grade.studentId = this.studentId;
    this.grade.problemId = this.problemId;

    this.gradeService.save(this.grade)
      .subscribe(_ => this.goBack());
  }

  onSelectProblem(problem: Problem) {
    this.problemId = problem.id;
  }

  onSelectStudent(student: Student) {
    this.studentId = student.id;
  }

  goBack(): void {
    this.location.back();
  }

}
