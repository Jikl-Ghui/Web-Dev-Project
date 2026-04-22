import { Routes } from '@angular/router';
import { CategoriesComponent } from './components/categories/categories.component';
import { TaskListComponent } from './components/task-list/task-list.component';
import { LoginComponent } from './components/login/login.component';

export const routes: Routes = [
  { path: '', redirectTo: 'categories', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'categories', component: CategoriesComponent },
  { path: 'categories/:id/tasks', component: TaskListComponent },
  { path: '**', redirectTo: 'categories' }
];