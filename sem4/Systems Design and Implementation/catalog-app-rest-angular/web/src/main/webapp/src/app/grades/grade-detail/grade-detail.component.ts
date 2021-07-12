import {Component, Input, OnInit} from '@angular/core';
import {ActivatedRoute, Params} from "@angular/router";
import {Location} from "@angular/common";
import {switchMap} from "rxjs/operators";
import {GradeService} from "../shared/grade.service";
import {Grade} from "../shared/grade.model";

@Component({
  selector: 'app-grade-detail',
  templateUrl: './grade-detail.component.html',
  styleUrls: ['./grade-detail.component.css']
})
export class GradeDetailComponent implements OnInit {

  @Input() grade: Grade;

  constructor(private gradeService: GradeService,
              private route: ActivatedRoute,
              private location: Location) { }

  ngOnInit(): void {
    this.route.params
      .pipe(switchMap((params: Params) => this.gradeService.getGrade(+params['id'])))
      .subscribe(grade => this.grade = grade);
  }

  goBack(): void {
    this.location.back();
  }

  save(): void {
    this.gradeService.update(this.grade)
      .subscribe(_ => this.goBack());
  }

  delete(): void {
    this.gradeService.delete(this.grade)
      .subscribe(_ => this.goBack());
  }

}
