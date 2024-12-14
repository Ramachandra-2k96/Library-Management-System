    // Start of Selection
    import React from 'react';
    import { Book } from 'lucide-react';

    
    const Navbar = () => {
      return (
        <nav className="fixed w-full bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between items-center h-16">
              <div className="flex items-center space-x-2">
                <Book className="h-8 w-8 text-indigo-600" />
                <span className="text-xl font-bold text-gray-900">College LibraryHub</span>
              </div>
              <div className="flex items-center space-x-8">
                <a href="#features" className="text-gray-600 hover:text-indigo-600">Features</a>
                <a href="#collections" className="text-gray-600 hover:text-indigo-600">Collections</a>
                <a href="#testimonials" className="text-gray-600 hover:text-indigo-600">Testimonials</a>
                <a href="/reader/profile">
                  <button 
                    className="bg-indigo-600 text-white px-6 py-2 rounded hover:bg-indigo-700"
                  >
                    Register Now
                  </button>
                </a>
              </div>
            </div>
          </div>
        </nav>
      );
    };
    
    export default Navbar;