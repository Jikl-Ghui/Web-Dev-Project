import { Component, OnInit,ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { TaskService } from '../../services/task.service';
import { Submission } from '../../models/models';

@Component({
  selector: 'app-submissions',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './submissions.component.html',
  styleUrl: './submissions.component.css',
})
export class SubmissionsComponent implements OnInit {
  submissions: Submission[] = [];
  loading = true;
  error = '';
  selectedCode: string | null = null;
  selectedTitle = '';

  constructor(private taskService: TaskService, private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.taskService.getMySubmissions().subscribe({
      next: (data) => {
        this.submissions = data;
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: () => {
        this.error = 'Failed to load submissions.';
        this.loading = false;
        this.cdr.detectChanges();
      }
    });
  }

  viewCode(submission: Submission): void {
    this.selectedCode = submission.code;
    this.selectedTitle = submission.task_title;
  }

  closeCode(): void {
    this.selectedCode = null;
  }

  deleteSubmission(id: number): void {
    if (!confirm('Delete this submission?')) return;
    this.taskService.deleteSubmission(id).subscribe({
      next: () => {
        this.submissions = this.submissions.filter(s => s.id !== id);
      },
      error: () => {
        this.error = 'Failed to delete submission.';
      }
    });
  }
}

