import React, { useState } from 'react';
import { Todo } from '../services/api';
import { Edit3, Trash2, Check, X, Calendar, Clock } from 'lucide-react'; // npm install lucide-react

interface TodoItemProps {
  todo: Todo;
  onUpdate: (id: number, updates: Partial<Todo>) => void;
  onDelete: (id: number) => void;
  onToggleComplete: (id: number) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo, onUpdate, onDelete, onToggleComplete }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(todo.title);
  const [editDescription, setEditDescription] = useState(todo.description);

  const handleSave = () => {
    onUpdate(todo.id, { title: editTitle, description: editDescription });
    setIsEditing(false);
  };

  const handleCancel = () => {
    setEditTitle(todo.title);
    setEditDescription(todo.description);
    setIsEditing(false);
  };

  return (
    <li className={`group mb-4 list-none transition-all duration-300 transform hover:-translate-y-1 ${
      todo.completed ? 'opacity-80' : 'opacity-100'
    }`}>
      <div className={`p-5 rounded-2xl border transition-all duration-300 ${
        todo.completed 
          ? 'bg-gray-50/80 border-gray-200' 
          : 'bg-white shadow-lg hover:shadow-xl border-indigo-50'
      }`}>
        <div className="flex items-start justify-between">
          <div className="flex items-start flex-1">
            {/* Custom Checkbox */}
            <div className="pt-1">
              <button
                onClick={() => onToggleComplete(todo.id)}
                className={`h-6 w-6 rounded-full border-2 flex items-center justify-center transition-all duration-200 ${
                  todo.completed 
                    ? 'bg-green-500 border-green-500 text-white' 
                    : 'bg-white border-gray-300 hover:border-indigo-500'
                }`}
              >
                {todo.completed && <Check className="h-4 w-4 stroke-[3px]" />}
              </button>
            </div>

            <div className="ml-4 flex-1">
              {isEditing ? (
                <div className="space-y-3 animate-in fade-in slide-in-from-top-2 duration-200">
                  <input
                    type="text"
                    value={editTitle}
                    onChange={(e) => setEditTitle(e.target.value)}
                    className="block w-full px-3 py-2 bg-white border border-indigo-200 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                    placeholder="Task title"
                  />
                  <textarea
                    value={editDescription}
                    onChange={(e) => setEditDescription(e.target.value)}
                    className="block w-full px-3 py-2 bg-white border border-indigo-200 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none resize-none"
                    rows={2}
                    placeholder="Task description"
                  />
                  <div className="flex space-x-2">
                    <button
                      onClick={handleSave}
                      className="flex items-center px-3 py-1.5 bg-indigo-600 text-white text-xs font-bold rounded-lg hover:bg-indigo-700 transition-colors"
                    >
                      <Check className="h-3 w-3 mr-1" /> Save
                    </button>
                    <button
                      onClick={handleCancel}
                      className="flex items-center px-3 py-1.5 bg-gray-100 text-gray-600 text-xs font-bold rounded-lg hover:bg-gray-200 transition-colors"
                    >
                      <X className="h-3 w-3 mr-1" /> Cancel
                    </button>
                  </div>
                </div>
              ) : (
                <div>
                  <h3 className={`text-base font-bold transition-all duration-300 ${
                    todo.completed ? 'text-gray-400 line-through' : 'text-gray-800'
                  }`}>
                    {todo.title}
                  </h3>
                  {todo.description && (
                    <p className={`mt-1 text-sm leading-relaxed ${
                      todo.completed ? 'text-gray-400' : 'text-gray-600'
                    }`}>
                      {todo.description}
                    </p>
                  )}
                </div>
              )}
            </div>
          </div>

          {/* Action Buttons */}
          {!isEditing && (
            <div className="flex items-center ml-4 space-x-1 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
              <button
                onClick={() => setIsEditing(true)}
                className="p-2 text-gray-400 hover:text-indigo-600 hover:bg-indigo-50 rounded-lg transition-all"
                title="Edit Task"
              >
                <Edit3 className="h-4 w-4" />
              </button>
              <button
                onClick={() => onDelete(todo.id)}
                className="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition-all"
                title="Delete Task"
              >
                <Trash2 className="h-4 w-4" />
              </button>
            </div>
          )}
        </div>

        {/* Footer info: Dates */}
        <div className="mt-4 pt-4 border-t border-gray-100 flex items-center justify-between text-[10px] font-bold uppercase tracking-widest text-gray-400">
          <div className="flex items-center">
            <Calendar className="h-3 w-3 mr-1" />
            Created: {new Date(todo.created_at).toLocaleDateString()}
          </div>
          <div className="flex items-center">
            <Clock className="h-3 w-3 mr-1" />
            Last Updated: {new Date(todo.updated_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
          </div>
        </div>
      </div>
    </li>
  );
};

export default TodoItem;