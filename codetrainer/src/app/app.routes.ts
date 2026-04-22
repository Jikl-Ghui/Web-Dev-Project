import { Routes } from '@angular/router';
import { authGuard } from './guards/auth.guard';

export const routes: Routes = [
  { path: '', redirectTo: 'categories', pathMatch: 'full' },
  { path: 'login', loadComponent: () => import('./pages/login/login.component').then(m => m.LoginComponent) },
  { path: 'register', loadComponent: () => import('./pages/register/register.component').then(m => m.RegisterComponent) },
  { path: 'categories', loadComponent: () => import('./pages/categories/categories.component').then(m => m.CategoriesComponent), canActivate: [authGuard] },
  { path: 'categories/:id/tasks', loadComponent: () => import('./pages/tasks/tasks.component').then(m => m.TasksComponent), canActivate: [authGuard] },
  { path: 'tasks/:id', loadComponent: () => import('./pages/workspace/workspace.component').then(m => m.WorkspaceComponent), canActivate: [authGuard] },
  { path: 'submissions', loadComponent: () => import('./pages/submissions/submissions.component').then(m => m.SubmissionsComponent), canActivate: [authGuard] },
];

