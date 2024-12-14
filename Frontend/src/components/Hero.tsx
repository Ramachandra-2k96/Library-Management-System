import React from 'react';
import { motion } from 'framer-motion';
import { BookOpen, Users, BookMarked } from 'lucide-react';


const Hero = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50 pt-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20">
        <div className="text-center">
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-5xl md:text-6xl font-bold text-gray-900 mb-6"
          >
            Your College Library
            <span className="text-indigo-600"> Reimagined</span>
          </motion.h1>
          
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto"
          >
            Access academic resources, research materials, and course textbooks with our modern digital library platform.
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="flex flex-wrap justify-center gap-4"
          >
            <a 
              href="/reader/profile"
              className="bg-indigo-600 text-white px-8 py-3 rounded-full hover:bg-indigo-700 transition-colors text-lg">
              Get Started
            </a>

            <a href = "#features">
              <button className="border-2 border-indigo-600 text-indigo-600 px-8 py-3 rounded-full hover:bg-indigo-50 transition-colors text-lg">
                Learn More
              </button>
            </a>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.6 }}
            className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto"
          >
            <div className="bg-white p-6 rounded-xl shadow-md transform hover:scale-105 transition-transform">
              <BookOpen className="h-12 w-12 text-indigo-600 mx-auto mb-4" />
              <h3 className="text-xl font-semibold mb-2">Course Materials</h3>
              <p className="text-gray-600">Access textbooks and course readings instantly.</p>
            </div>
            <div className="bg-white p-6 rounded-xl shadow-md transform hover:scale-105 transition-transform">
              <Users className="h-12 w-12 text-indigo-600 mx-auto mb-4" />
              <h3 className="text-xl font-semibold mb-2">Study Groups</h3>
              <p className="text-gray-600">Connect with classmates and form study groups.</p>
            </div>
            <div className="bg-white p-6 rounded-xl shadow-md transform hover:scale-105 transition-transform">
              <BookMarked className="h-12 w-12 text-indigo-600 mx-auto mb-4" />
              <h3 className="text-xl font-semibold mb-2">Research Tools</h3>
              <p className="text-gray-600">Access academic journals and research papers.</p>
            </div>
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export default Hero;