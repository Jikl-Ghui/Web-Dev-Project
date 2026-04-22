import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Category, Task, Submission } from '../models/models';

@Injectable({ providedIn: 'root' })
export class TaskService {
  private apiUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  getCategories(): Observable<Category[]> {
    return this.http.get<Category[]>(`${this.apiUrl}/categories/`);
  }

  getTasksByCategory(categoryId: number): Observable<Task[]> {
    return this.http.get<Task[]>(`${this.apiUrl}/categories/${categoryId}/tasks/`);
  }

  getTask(taskId: number): Observable<Task> {
    return this.http.get<Task>(`${this.apiUrl}/tasks/${taskId}/`);
  }

  getMySubmissions(): Observable<Submission[]> {
    return this.http.get<Submission[]>(`${this.apiUrl}/submissions/`);
  }

  submitSolution(taskId: number, code: string, language: string): Observable<Submission> {
    return this.http.post<Submission>(`${this.apiUrl}/submissions/`, {
      task_id: taskId,
      code,
      language,
    });
  }

  updateSubmission(id: number, code: string): Observable<Submission> {
    return this.http.put<Submission>(`${this.apiUrl}/submissions/${id}/`, { code });
  }

  deleteSubmission(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/submissions/${id}/`);
  }
}

