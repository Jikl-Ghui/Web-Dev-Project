export interface Category {
  id: number;
  name: string;
}

export interface Task {
  id: number;
  title: string;
  description: string;
  difficulty: string;
  category: number;
  category_name: string;
}

export interface TaskStats {
  total_tasks: number;
  difficulty_level: string;
}

export interface ProjectInfo {
  project: string;
  version: string;
}