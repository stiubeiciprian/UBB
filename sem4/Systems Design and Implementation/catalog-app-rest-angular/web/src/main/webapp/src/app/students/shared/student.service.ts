import {Injectable} from '@angular/core';

import {HttpClient} from "@angular/common/http";

import {Student} from "./student.model";

import {Observable} from "rxjs";
import {map} from "rxjs/operators";
import {Problem} from "../../problems/shared/problem.model";


@Injectable()
export class StudentService {
  private studentsUrl = 'http://localhost:8080/api/students';

  constructor(private httpClient: HttpClient) {
  }

  getStudents(): Observable<Student[]> {
    return this.httpClient
      .get<Array<Student>>(this.studentsUrl);
  }

  getStudent(id: number): Observable<Student> {
    return this.getStudents()
      .pipe(
        map(students => students.find(student => student.id === id))
      );
  }

  update(student): Observable<Student> {
    const url = `${this.studentsUrl}/${student.id}`;
    return this.httpClient
      .put<Student>(url, student);
  }

  delete(student): Observable<ArrayBuffer> {
    const url = `${this.studentsUrl}/${student.id}`;
    // @ts-ignore
    return this.httpClient
      .delete(url);
  }

  save(student): Observable<Student> {
    // @ts-ignore
    return this.httpClient.post(this.studentsUrl, student);
  }

}
