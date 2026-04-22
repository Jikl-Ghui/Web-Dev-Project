export interface User {
  id: number;
  username: string;
  email: string;
}

export interface AuthResponse {
  user: User;
  access: string;
  refresh: string;
}

export interface Category {
  id: number;
  name: string;
  description: string;
  icon: string;
  task_count: number;
}

export interface Task {
  id: number;
  title: string;
  description: string;
  examples: string;
  difficulty: 'easy' | 'medium' | 'hard';
  category: number;
  category_name: string;
  created_at: string;
}

export interface Submission {
  id: number;
  task: number;
  task_title: string;
  username: string;
  code: string;
  language: string;
  status: 'accepted' | 'wrong' | 'pending';
  submitted_at: string;
  updated_at: string;
}

