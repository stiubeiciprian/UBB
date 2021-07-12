import { Component, OnInit } from '@angular/core';
import {ProblemService} from "../shared/problem.service";
import {Problem} from "../shared/problem.model";
import {Router} from "@angular/router";

@Component({
  selector: 'app-problem-list',
  templateUrl: './problem-list.component.html',
  styleUrls: ['./problem-list.component.css']
})
export class ProblemListComponent implements OnInit {
  errorMessage: string;
  problems: Problem[];

  constructor(private problemService: ProblemService,
              private router: Router) { }

  ngOnInit(): void {
    this.getProblems();
  }

  getProblems() {
    this.problemService.getProblems()
      .subscribe(
        problems => this.problems = problems,
        error => this.errorMessage = <any>error
        );
  }

  onSelect(problem: Problem) {
    this.router.navigate(['problem/detail', problem.id]);
  }

  addProblem() {
    this.router.navigate(['problem/add']);
  }

}
