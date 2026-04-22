import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs'; // 'of' создает поток из обычных данных
import { Category, Task, TaskStats } from '../models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private BASE_URL = 'http://127.0.0.1:8000/api';

  private mockCategories: Category[] = [
    { id: 1, name: 'Algorithms' },
    { id: 2, name: 'Web-Dev' }
  ];

  private mockTasks: Task[] = [
    { id: 10, title: 'Бинарный поиск', description: 'Реализуйте поиск за O(log n)', difficulty: 'Medium', category: 1, category_name: 'Алгоритмы' },
    { id: 11, title: 'Верстка Flexbox', description: 'Сделайте сетку на флексах', difficulty: 'Easy', category: 2, category_name: 'Веб-разработка' }
  ];

  constructor(private http: HttpClient) { }

  getCategories(): Observable<Category[]> {
    return of(this.mockCategories);
  }

  getTasksByCategory(id: number): Observable<Task[]> {
    const tasks = this.mockTasks.filter(t => t.category === id);
    return of(tasks);
  }

  getStats(): Observable<TaskStats> {
    return of({ total_tasks: 2, difficulty_level: 'Mixed' });
  }
}