import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import {FormsModule} from '@angular/forms';

import {AppComponent} from './app.component';
import {AppRoutingModule} from "./app-routing.module";
import {StudentDetailComponent} from "./students/student-detail/student-detail.component";
import {StudentsComponent} from "./students/students.component";
import {StudentListComponent} from "./students/student-list/student-list.component";
import {StudentService} from "./students/shared/student.service";
import { ProblemsComponent } from './problems/problems.component';
import { GradesComponent } from './grades/grades.component';
import { ProblemListComponent } from './problems/problem-list/problem-list.component';
import {ProblemService} from "./problems/shared/problem.service";
import { ProblemDetailComponent } from './problems/problem-detail/problem-detail.component';
import { GradeDetailComponent } from './grades/grade-detail/grade-detail.component';
import { GradeListComponent } from './grades/grade-list/grade-list.component';
import {GradeService} from "./grades/shared/grade.service";
import { StudentFormComponent } from './students/student-form/student-form.component';
import { ProblemFormComponent } from './problems/problem-form/problem-form.component';
import { GradeFormComponent } from './grades/grade-form/grade-form.component';


@NgModule({
  declarations: [
    AppComponent,
    StudentDetailComponent,
    StudentsComponent,
    StudentListComponent,
    ProblemsComponent,
    GradesComponent,
    ProblemListComponent,
    ProblemDetailComponent,
    GradeDetailComponent,
    GradeListComponent,
    StudentFormComponent,
    ProblemFormComponent,
    GradeFormComponent,



  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
  ],
  providers: [StudentService, ProblemService, GradeService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
