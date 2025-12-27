import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '../services/auth';
import api, { Todo } from '../services/api';
import TodoForm from '../components/TodoForm';
import TodoList from '../components/TodoList';
import { LogOut, CheckCircle2, User as UserIcon, Loader2, LayoutGrid } from 'lucide-react';

const Dashboard = () => {
  const { user, signout, isAuthenticated, loading } = useAuth();
  const [todos, setTodos] = useState<Todo[]>([]);
  const [isInitialLoading, setIsInitialLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    if (!loading && !isAuthenticated()) {
      router.push('/signin');
    } else if (isAuthenticated()) {
      fetchTodos();
    }
  }, [loading, isAuthenticated, router]);

  const fetchTodos = async () => {
    try {
      const data = await api.getTodos();
      setTodos(data);
    } catch (error) {
      console.error('Failed to fetch todos:', error);
    } finally {
      setIsInitialLoading(false);
    }
  };

  const handleAddTodo = async (title: string, description?: string) => {
    try {
      const newTodo = await api.createTodo(title, description);
      setTodos([newTodo, ...todos]);
    } catch (error) {
      console.error('Failed to add todo:', error);
    }
  };

  const handleUpdateTodo = async (id: number, updates: Partial<Todo>) => {
    try {
      const updated = await api.updateTodo(id, updates);
      setTodos(todos.map((t) => (t.id === id ? updated : t)));
    } catch (error) {
      console.error('Failed to update todo:', error);
    }
  };

  const handleDeleteTodo = async (id: number) => {
    try {
      await api.deleteTodo(id);
      setTodos(todos.filter((t) => t.id !== id));
    } catch (error) {
      console.error('Failed to delete todo:', error);
    }
  };

  const handleToggleComplete = async (id: number) => {
    try {
      const updated = await api.toggleTodoCompletion(id);
      setTodos(todos.map((t) => (t.id === id ? updated : t)));
    } catch (error) {
      console.error('Failed to toggle todo:', error);
    }
  };

  if (loading || isInitialLoading) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center bg-slate-50 space-y-4">
        <Loader2 className="h-12 w-12 text-indigo-600 animate-spin" />
        <p className="text-slate-500 font-bold text-sm uppercase tracking-widest">Loading Workspace</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#f8fafc]">
      {/* Premium Navbar */}
      <nav className="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-18 py-4 items-center">
            <div className="flex items-center space-x-3">
              <div className="bg-gradient-to-tr from-indigo-600 to-purple-600 p-2 rounded-xl shadow-lg shadow-indigo-200">
                <CheckCircle2 className="h-6 w-6 text-white" />
              </div>
              <div>
                <span className="text-xl font-black text-slate-900 tracking-tight block leading-none">FocusFlow</span>
                <span className="text-[10px] font-bold text-indigo-500 uppercase tracking-tighter">Workspace</span>
              </div>
            </div>
            
            <div className="flex items-center space-x-6">
              <div className="hidden md:flex items-center space-x-3 px-4 py-2 bg-slate-50 border border-slate-100 rounded-2xl">
                <div className="h-8 w-8 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-600">
                   <UserIcon size={16} />
                </div>
                <div className="flex flex-col">
                  <span className="text-[10px] font-bold text-slate-400 uppercase leading-none">Logged in as</span>
                  <span className="text-sm font-bold text-slate-700">{user?.email.split('@')[0]}</span>
                </div>
              </div>
              <button
                onClick={() => {
                  signout();
                  router.push('/signin');
                }}
                className="group flex items-center space-x-2 px-5 py-2.5 text-sm font-bold text-slate-600 hover:text-red-600 hover:bg-red-50 rounded-2xl transition-all duration-200"
              >
                <LogOut className="h-4 w-4 transition-transform group-hover:-translate-x-1" />
                <span>Logout</span>
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Content Area */}
      <main className="max-w-4xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12">
          
          {/* Left Column: Stats & Form */}
          <div className="lg:col-span-5 space-y-8">
            <div className="bg-gradient-to-br from-indigo-600 to-purple-700 p-8 rounded-[2rem] text-white shadow-2xl shadow-indigo-200 relative overflow-hidden">
               <LayoutGrid className="absolute top-[-20px] right-[-20px] h-32 w-32 opacity-10 rotate-12" />
               <h1 className="text-3xl font-black tracking-tight">Daily Progress</h1>
               <p className="mt-2 text-indigo-100 font-medium opacity-80">You have {todos.filter(t => !t.completed).length} tasks remaining today.</p>
               <div className="mt-6 h-2 w-full bg-white/20 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-white transition-all duration-1000" 
                    style={{ width: `${todos.length > 0 ? (todos.filter(t => t.completed).length / todos.length) * 100 : 0}%` }}
                  ></div>
               </div>
            </div>

            <div className="bg-white p-2 rounded-[2rem] shadow-sm border border-slate-100">
               <TodoForm onAddTodo={handleAddTodo} />
            </div>
          </div>

          {/* Right Column: The List */}
          <div className="lg:col-span-7">
            <div className="flex items-center justify-between mb-6 px-2">
              <h2 className="text-lg font-black text-slate-800 tracking-tight">Your Roadmap</h2>
              <span className="bg-slate-200 text-slate-600 text-[10px] font-black px-3 py-1 rounded-full uppercase">
                {todos.length} Total
              </span>
            </div>
            
            <div className="space-y-4">
              <TodoList
                todos={todos}
                onUpdateTodo={handleUpdateTodo}
                onDeleteTodo={handleDeleteTodo}
                onToggleComplete={handleToggleComplete}
              />
            </div>
          </div>

        </div>
      </main>
    </div>
  );
};

export default Dashboard;