import {Component, Input, OnInit} from '@angular/core';
import {ActivatedRoute, Params} from "@angular/router";
import {Location} from "@angular/common";
import {switchMap} from "rxjs/operators";
import {ProblemService} from "../shared/problem.service";
import {Problem} from "../shared/problem.model";

@Component({
  selector: 'app-problem-detail',
  templateUrl: './problem-detail.component.html',
  styleUrls: ['./problem-detail.component.css']
})
export class ProblemDetailComponent implements OnInit {

  @Input() problem: Problem;

  constructor(private problemService: ProblemService,
              private  route: ActivatedRoute,
              private location: Location) { }

  ngOnInit(): void {
    this.route.params
      .pipe(switchMap((params: Params) => this.problemService.getProblem(+params['id'])))
      .subscribe(problem => this.problem = problem);
  }

  goBack(): void {
    this.location.back();
  }

  save(): void {
    this.problemService.update(this.problem)
      .subscribe(_ => this.goBack());
  }

  delete(): void {
    this.problemService.delete(this.problem)
      .subscribe(_ => this.goBack());
  }

}
