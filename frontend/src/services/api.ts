// frontend/src/services/api.ts
import axios, { type AxiosInstance, type InternalAxiosRequestConfig } from 'axios';

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
    // Initialize the API client with base configuration
    this.api = axios.create({
      baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Add request interceptor to include auth token
    this.api.interceptors.request.use(
      (config) => {
        if (this.token) {
          config.headers.Authorization = `Bearer ${this.token}`;
        }
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    // Add response interceptor to handle token expiration
    this.api.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response?.status === 401) {
          // Token might be expired, clear it
          this.clearToken();
        }
        return Promise.reject(error);
      }
    );
  }

  // Set authentication token
  setToken(token: string) {
    this.token = token;
  }

  // Clear authentication token
  clearToken() {
    this.token = null;
  }

  // Authentication methods
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
    await this.api.post('/auth/signout');
    this.clearToken();
  }

  // Todo methods
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

export default new ApiService();
export type { Todo, User, TokenResponse };