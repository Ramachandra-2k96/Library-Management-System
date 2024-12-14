import React from 'react';
import { motion } from 'framer-motion';
import { Book, Mail, Phone, MapPin, Facebook, Twitter, Instagram, Youtube } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-gradient-to-br from-indigo-900 to-indigo-800 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* About Section */}
          <div className="space-y-4">
            <div className="flex items-center space-x-2">
              <Book className="h-6 w-6" />
              <h3 className="text-xl font-bold">College LibraryHub</h3>
            </div>
            <p className="text-indigo-200">
              Empowering education through innovative library management solutions for students and faculty.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Quick Links</h4>
            <ul className="space-y-2">
              <li><a href="#features" className="text-indigo-200 hover:text-white transition-colors">Features</a></li>
              <li><a href="#collections" className="text-indigo-200 hover:text-white transition-colors">Collections</a></li>
              <li><a href="#testimonials" className="text-indigo-200 hover:text-white transition-colors">Testimonials</a></li>
              <li><a href="/profile" className="text-indigo-200 hover:text-white transition-colors">Student Portal</a></li>
            </ul>
          </div>

          {/* Contact Info */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Contact Us</h4>
            <ul className="space-y-2">
              <li className="flex items-center space-x-2">
                <Mail className="h-4 w-4" />
                <span className="text-indigo-200">library@college.edu</span>
              </li>
              <li className="flex items-center space-x-2">
                <Phone className="h-4 w-4" />
                <span className="text-indigo-200">+1 (555) 123-4567</span>
              </li>
              <li className="flex items-center space-x-2">
                <MapPin className="h-4 w-4" />
                <span className="text-indigo-200">123 College Ave, Campus Center</span>
              </li>
            </ul>
          </div>

          {/* Social Links */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Follow Us</h4>
            <div className="flex space-x-4">
              <a href="#" className="hover:text-indigo-300 transition-colors">
                <Facebook className="h-6 w-6" />
              </a>
              <a href="#" className="hover:text-indigo-300 transition-colors">
                <Twitter className="h-6 w-6" />
              </a>
              <a href="#" className="hover:text-indigo-300 transition-colors">
                <Instagram className="h-6 w-6" />
              </a>
              <a href="#" className="hover:text-indigo-300 transition-colors">
                <Youtube className="h-6 w-6" />
              </a>
            </div>
          </div>
        </div>

        <div className="mt-8 pt-8 border-t border-indigo-700">
          <p className="text-center text-indigo-200">
            © {new Date().getFullYear()} College LibraryHub. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;