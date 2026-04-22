import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
// Правильный путь к моделям (поднимись на одну папку вверх)
import { Category, Task, TaskStats, ProjectInfo } from '../models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private BASE_URL = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) { }

  getProjectInfo(): Observable<ProjectInfo> {
    return this.http.get<ProjectInfo>(`${this.BASE_URL}/info/`);
  }

  getStats(): Observable<TaskStats> {
    return this.http.get<TaskStats>(`${this.BASE_URL}/stats/`);
  }

  getCategories(): Observable<Category[]> {
    return this.http.get<Category[]>(`${this.BASE_URL}/categories/`);
  }

  getTasksByCategory(categoryId: number): Observable<Task[]> {
    return this.http.get<Task[]>(`${this.BASE_URL}/categories/${categoryId}/tasks/`);
  }
}