import { Component, OnInit , ChangeDetectorRef} from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { TaskService } from '../../services/task.service';
import { Task } from '../../models/models';

@Component({
  selector: 'app-workspace',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './workspace.component.html',
  styleUrl: './workspace.component.css',
})
export class WorkspaceComponent implements OnInit {
  task: Task | null = null;
  loading = true;
  error = '';

  code = '# Write your solution here\n\n';
  language = 'python';
  languages = ['python', 'javascript', 'java', 'cpp'];

  submitLoading = false;
  result: 'accepted' | 'wrong' | null = null;

  constructor(
    private taskService: TaskService,
    private route: ActivatedRoute,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    const taskId = Number(this.route.snapshot.paramMap.get('id'));
    this.taskService.getTask(taskId).subscribe({
      next: (data) => {
        this.task = data;
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: () => {
        this.error = 'Task not found.';
        this.loading = false;
      }
    });
  }

  onLanguageChange(): void {
    const starters: Record<string, string> = {
      python: '# Write your solution here\n\n',
      javascript: '// Write your solution here\n\n',
      java: '// Write your solution here\npublic class Solution {\n\n}\n',
      cpp: '// Write your solution here\n#include<iostream>\nusing namespace std;\n\n',
    };
    this.code = starters[this.language];
  }

  onSubmit(): void {
    if (!this.task || !this.code.trim()) return;
    this.submitLoading = true;
    this.result = null;

    this.taskService.submitSolution(this.task.id, this.code, this.language).subscribe({
      next: (submission) => {
        this.result = submission.status as 'accepted' | 'wrong';
        this.submitLoading = false;
      },
      error: () => {
        this.error = 'Failed to submit. Please try again.';
        this.submitLoading = false;
      }
    });
  }
}

