import React from 'react';
import './Sidebar.css';
import { FaProjectDiagram, FaBug, FaUsers, FaUserCircle, FaCog } from 'react-icons/fa';
import { Link } from 'react-router-dom';

export default function Sidebar() {
  return (
    <div className='sidebar'>
      <div className="sidebar-header">
        <h2>Mini Jira</h2>
      </div>
      <div className="sidebar-nav">
        <Link  to="/dashboard"><span>Dashboard</span></Link>
        <Link  to="/projects"> <span>Projects</span></Link>
        <Link  to="#"><span>Bugs</span></Link>
        <Link  to="#"> <span>Teams</span></Link>
        <Link  to="#"> <span>Profile</span></Link>
        <Link  to="#"><span>Settings</span></Link>
      </div>
    </div>
  );
}
