import React, { useState } from 'react';
import { PlusCircle, AlignLeft, Type } from 'lucide-react'; // Optional: npm install lucide-react

interface TodoFormProps {
  onAddTodo: (title: string, description?: string) => void;
}

const TodoForm: React.FC<TodoFormProps> = ({ onAddTodo }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [isFocused, setIsFocused] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!title.trim()) {
      return; 
    }
    
    onAddTodo(title, description);
    
    setTitle('');
    setDescription('');
  };

  return (
    <div className={`transition-all duration-300 transform ${isFocused ? 'scale-[1.01]' : 'scale-100'}`}>
      <form 
        onSubmit={handleSubmit} 
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
        className="bg-white/90 backdrop-blur-md shadow-xl rounded-2xl p-6 border border-indigo-50/50"
      >
        <div className="space-y-5">
          {/* Title Input */}
          <div>
            <label htmlFor="title" className="flex items-center text-xs font-bold text-indigo-600 uppercase tracking-widest mb-2 ml-1">
              <Type className="h-3 w-3 mr-1" />
              Task Title
            </label>
            <div className="relative group">
              <input
                type="text"
                id="title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                required
                className="block w-full px-4 py-3 bg-gray-50/50 border border-gray-200 rounded-xl text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition-all duration-200"
                placeholder="What's on your mind today?"
              />
            </div>
          </div>

          {/* Description Input */}
          <div>
            <label htmlFor="description" className="flex items-center text-xs font-bold text-indigo-600 uppercase tracking-widest mb-2 ml-1">
              <AlignLeft className="h-3 w-3 mr-1" />
              Notes (Optional)
            </label>
            <textarea
              id="description"
              rows={2}
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="block w-full px-4 py-3 bg-gray-50/50 border border-gray-200 rounded-xl text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition-all duration-200 resize-none"
              placeholder="Add some details..."
            />
          </div>

          {/* Submit Button */}
          <div className="flex justify-end pt-2">
            <button
              type="submit"
              className="group inline-flex items-center px-6 py-3 border border-transparent text-sm font-bold rounded-xl shadow-lg text-white bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all duration-200 transform hover:-translate-y-1 active:scale-95"
            >
              <PlusCircle className="h-5 w-5 mr-2 group-hover:rotate-90 transition-transform duration-300" />
              Create Task
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};

export default TodoForm;