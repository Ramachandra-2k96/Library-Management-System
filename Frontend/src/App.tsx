import React from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Features from './components/Features';
import Collections from './components/Collections';
import Testimonials from './components/Testimonials';
import Footer from './components/Footer';

function App() {
  return (
    <div className="relative">
      <Navbar />
      <Hero />
      <Features />
      <Collections />
      <Testimonials />
      <Footer />
    </div>
  );
}

export default App;