// frontend/src/services/api.ts
import axios, { type AxiosInstance } from 'axios';

// Interfaces are already exported here, no need to export them at the bottom
export interface Todo {
  id: number;
  title: string;
  description: string;
  completed: boolean;
  user_id: number;
  created_at: string;
  updated_at: string;
}

export interface User {
  id: number;
  email: string;
  created_at: string;
  updated_at: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
  user: User;
}

class ApiService {
  private api: AxiosInstance;
  private token: string | null = null;

  constructor() {
    this.api = axios.create({
      baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    this.api.interceptors.request.use(
      (config) => {
        if (this.token) {
          config.headers.Authorization = `Bearer ${this.token}`;
        }
        return config;
      },
      (error) => Promise.reject(error)
    );

    this.api.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response?.status === 401) {
          this.clearToken();
        }
        return Promise.reject(error);
      }
    );
  }

  setToken(token: string) {
    this.token = token;
  }

  clearToken() {
    this.token = null;
  }

  async signup(email: string, password: string): Promise<User> {
    const response = await this.api.post('/auth/signup', { email, password });
    return response.data;
  }

  async signin(email: string, password: string): Promise<TokenResponse> {
    const response = await this.api.post('/auth/signin', { email, password });
    const data = response.data;
    this.setToken(data.access_token);
    return data;
  }

  async signout(): Promise<void> {
    // Some backends don't have a signout endpoint if using stateless JWT, 
    // but keeping it as per your original structure.
    try {
      await this.api.post('/auth/signout');
    } finally {
      this.clearToken();
    }
  }

  async getTodos(): Promise<Todo[]> {
    const response = await this.api.get('/todos');
    return response.data;
  }

  async createTodo(title: string, description?: string): Promise<Todo> {
    const response = await this.api.post('/todos', { title, description });
    return response.data;
  }

  async updateTodo(id: number, updates: Partial<Todo>): Promise<Todo> {
    const response = await this.api.put(`/todos/${id}`, updates);
    return response.data;
  }

  async toggleTodoCompletion(id: number): Promise<Todo> {
    const response = await this.api.patch(`/todos/${id}/toggle`);
    return response.data;
  }

  async deleteTodo(id: number): Promise<void> {
    await this.api.delete(`/todos/${id}`);
  }
}

// Fixed: Export only the default instance. 
// The interfaces are already exported individually above.
export default new ApiService();