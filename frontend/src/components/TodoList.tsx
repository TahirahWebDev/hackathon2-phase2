import React from 'react';
import { Todo } from '../services/api';
import TodoItem from './TodoItem';
import { ClipboardList, Sparkles } from 'lucide-react'; // npm install lucide-react

interface TodoListProps {
  todos: Todo[];
  onUpdateTodo: (id: number, updates: Partial<Todo>) => void;
  onDeleteTodo: (id: number) => void;
  onToggleComplete: (id: number) => void;
}

const TodoList: React.FC<TodoListProps> = ({ todos, onUpdateTodo, onDeleteTodo, onToggleComplete }) => {
  if (todos.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-20 px-4 text-center bg-white/50 backdrop-blur-sm rounded-3xl border-2 border-dashed border-gray-200 animate-in fade-in zoom-in duration-500">
        <div className="relative mb-4">
          <ClipboardList className="h-16 w-16 text-gray-300" />
          <Sparkles className="h-6 w-6 text-indigo-400 absolute -top-1 -right-1 animate-pulse" />
        </div>
        <h3 className="text-xl font-bold text-gray-800">Your list is clear</h3>
        <p className="mt-2 text-gray-500 max-w-xs mx-auto">
          No todos yet. Add a new task above to start your productive journey!
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-1 animate-in fade-in slide-in-from-bottom-4 duration-500">
      <div className="flex items-center justify-between mb-4 px-2">
        <h2 className="text-sm font-black uppercase tracking-[0.2em] text-gray-400">
          Current Tasks ({todos.length})
        </h2>
      </div>
      <ul className="space-y-3">
        {todos.map((todo) => (
          <TodoItem
            key={todo.id}
            todo={todo}
            onUpdate={onUpdateTodo}
            onDelete={onDeleteTodo}
            onToggleComplete={onToggleComplete}
          />
        ))}
      </ul>
    </div>
  );
};

export default TodoList;