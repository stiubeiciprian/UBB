import {Component, Input, OnInit} from '@angular/core';
import {ProblemService} from "../shared/problem.service";
import {ActivatedRoute, Params} from "@angular/router";
import {Location} from "@angular/common";
import {Problem} from "../shared/problem.model";

@Component({
  selector: 'app-problem-form',
  templateUrl: './problem-form.component.html',
  styleUrls: ['./problem-form.component.css']
})
export class ProblemFormComponent implements OnInit {

  @Input() problem: Problem;

  constructor(private problemService: ProblemService,
              private  route: ActivatedRoute,
              private location: Location) { }


  ngOnInit(): void {
    this.problem = new Problem();
  }

  goBack(): void {
    this.location.back();
  }

  save(): void {
    this.problemService.save(this.problem)
      .subscribe(_ => this.goBack());
  }

}
