import {Injectable} from '@angular/core';

import {HttpClient} from "@angular/common/http";


import {Observable} from "rxjs";
import {Problem} from "./problem.model";
import {map} from "rxjs/operators";


@Injectable()
export class ProblemService {
  private problemsUrl = 'http://localhost:8080/api/problems';

  constructor(private httpClient: HttpClient) {
  }

  getProblems(): Observable<Problem[]> {
    return this.httpClient
      .get<Array<Problem>>(this.problemsUrl);
  }

  getProblem(id: number): Observable<Problem> {
    return this.getProblems()
      .pipe(
        map(problems => problems.find(problem => problem.id === id))
      );
  }

  update(problem): Observable<Problem> {
    const url = `${this.problemsUrl}/${problem.id}`;
    return this.httpClient
      .put<Problem>(url, problem);
  }

  delete(problem): Observable<ArrayBuffer> {
    const url = `${this.problemsUrl}/${problem.id}`;

    // @ts-ignore
    return this.httpClient
      .delete(url);
  }

  save(problem): Observable<Problem> {
    // @ts-ignore
    return this.httpClient.post(this.problemsUrl, problem);
  }
}
