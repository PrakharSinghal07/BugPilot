import React from "react";
import Navbar from "../Components/Navbar";
import Sidebar from "../Components/Sidebar";

export default function Projects() {
  return (
    <>
      <Navbar />
      <Sidebar />
      <div className="temp-nav"></div>
      <div className="main-app">
        Hello Moto
      </div>
    </>
  );
}
