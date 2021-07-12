import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {StudentsComponent} from "./students/students.component";
import {StudentDetailComponent} from "./students/student-detail/student-detail.component";
import {ProblemsComponent} from "./problems/problems.component";
import {GradesComponent} from "./grades/grades.component";
import {ProblemDetailComponent} from "./problems/problem-detail/problem-detail.component";
import {GradeDetailComponent} from "./grades/grade-detail/grade-detail.component";
import {ProblemFormComponent} from "./problems/problem-form/problem-form.component";
import {StudentFormComponent} from "./students/student-form/student-form.component";
import {GradeFormComponent} from "./grades/grade-form/grade-form.component";


const routes: Routes = [
  // { path: '', redirectTo: '/home', pathMatch: 'full' },
  {path: 'students', component: StudentsComponent},
  {path: 'student/detail/:id', component: StudentDetailComponent},
  {path: 'student/add', component: StudentFormComponent},

  {path: 'problems', component: ProblemsComponent},
  {path: 'problem/detail/:id', component: ProblemDetailComponent},
  {path: 'problem/add', component: ProblemFormComponent},

  {path: 'grades', component: GradesComponent},
  {path: 'grade/detail/:id', component: GradeDetailComponent},
  {path: 'grade/add', component: GradeFormComponent}


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
