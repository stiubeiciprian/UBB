import {Injectable} from '@angular/core';

import {HttpClient} from "@angular/common/http";


import {Observable} from "rxjs";
import {Grade} from "./grade.model";
import {map} from "rxjs/operators";


@Injectable()
export class GradeService {
  private gradesUrl = 'http://localhost:8080/api/grades';

  constructor(private httpClient: HttpClient) {
  }

  getGrades(): Observable<Grade[]> {
    return this.httpClient
      .get<Array<Grade>>(this.gradesUrl);
  }

  getGrade(id: number): Observable<Grade> {
    return this.getGrades()
      .pipe(
        map(grades => grades.find(grade => grade.id === id))
      );
  }

  update(grade): Observable<Grade> {
    const url = `${this.gradesUrl}/${grade.id}`;
    return this.httpClient
      .put<Grade>(url, grade);
  }

  delete(grade): Observable<ArrayBuffer> {
    const url = `${this.gradesUrl}/${grade.id}`;

    // @ts-ignore
    return this.httpClient
      .delete(url);
  }

  save(grade): Observable<Grade> {
    // @ts-ignore
    return this.httpClient.post(this.gradesUrl, grade);
  }
}
