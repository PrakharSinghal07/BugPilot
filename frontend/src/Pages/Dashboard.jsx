import React, { useEffect, useState } from "react";
import Navbar from "../Components/Navbar";
import Sidebar from "../Components/Sidebar";
import ChartComponent from "../Components/ChartComponent"; // Importing Chart Component
import "./Dashboard.css";
export default function Dashboard() {
  const [data, setData] = useState([]);
  const [totalProjects, setTotalProjects] = useState(0);
  const [totalOpenBugs, setTotalOpenBugs] = useState(0);
  const [totalClosedBugs, setTotalClosedBugs] = useState(0);
  const [projects, setProjects] = useState([]);
  useEffect(() => {
    const getData = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await fetch("http://localhost:8000/bugs/assigned", {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          throw new Error("Failed to fetch projects");
        }

        const result = await response.json();
        // setTotalAssignedBugs(result.length);

        setData(result);
      } catch (error) {
        console.error("Error fetching bugs:", error);
      }
    };

    getData();
  }, []);
  useEffect(() => {
    const getData = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await fetch("http://localhost:8000/projects", {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          throw new Error("Failed to fetch projects");
        }

        const result = await response.json();
        setTotalProjects(result.length);
        setProjects(result);
        // setData(result);
      } catch (error) {
        console.error("Error fetching bugs:", error);
      }
    };

    getData();
  }, []);
  useEffect(() => {
    let openCount = 0;
    let closedCount = 0;

    for (let i = 0; i < data.length; i++) {
      const status = data[i].status.toLowerCase();

      if (status === "open") {
        openCount++;
      } else if (status === "closed") {
        closedCount++;
      }
    }

    setTotalOpenBugs(openCount);
    setTotalClosedBugs(closedCount);
  }, [data]);

  const graph1Data = {
    labels: ["January", "February", "March", "April", "May", "June"],
    datasets: [
      {
        label: "Project Completion",
        data: [65, 59, 80, 81, 56, 55],
        borderColor: "#2563eb",
        backgroundColor: "rgba(37, 99, 235, 0.2)",
        tension: 0.4,
      },
    ],
  };

  const graph2Data = {
    labels: ["January", "February", "March", "April", "May", "June"],
    datasets: [
      {
        label: "Bugs Reported",
        data: [12, 19, 3, 5, 2, 3],
        borderColor: "#d63b6a",
        backgroundColor: "rgba(214, 59, 106, 0.2)",
        tension: 0.4,
      },
    ],
  };
  return (
    <div>
      <Sidebar />
      <Navbar />
      <div className="temp-nav"></div>
      <div className="main-app">
        <div className="summary-cards">
          <div className="summary-card">
            <p className="card-title">Total Projects</p>
            <p className="card-value">{totalProjects}</p>
          </div>
          <div className="summary-card">
            <p className="card-title">Open Bugs</p>
            <p className="card-value">{totalOpenBugs}</p>
          </div>
          <div className="summary-card">
            <p className="card-title">Closed Bugs</p>
            <p className="card-value">{totalClosedBugs}</p>
          </div>
          <div className="summary-card">
            <p className="card-title">Team Members</p>
            <p className="card-value">8</p>
          </div>
        </div>

        <div className="graphs">
          <div className="graph1">
            <ChartComponent chartData={graph1Data} />
          </div>
          <div className="graph2">
            <ChartComponent chartData={graph2Data} />
          </div>
        </div>

        <div className="project-bug-list-dashboard">
          <div className="assigned-bugs-dashboard section-table">
            <h3 className="section-title">Recent Bugs</h3>
            <table className="custom-table">
              <thead>
                <tr>
                  <th>Bug</th>
                  <th>Status</th>
                  <th>Priority</th>
                  <th>Due</th>
                </tr>
              </thead>
              <tbody>
                {data.length !== 0 &&
                  data.map((bug, i) => {
                    if(i>=4) return
                    return (
                      <tr>
                        <td>{bug.title}</td>
                        <td>{bug.status}</td>
                        <td>{bug.priority}</td>
                        <td>{bug.due_date}</td>
                      </tr>
                    );
                  })}
              </tbody>
            </table>
          </div>
          <div className="my-projects-dashboard section-table">
            <h3 className="section-title">My Projects</h3>
            <table className="custom-table">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {projects.length !== 0 &&
                  projects.map((project) => {
                    return (
                      <tr>
                        <td>{project.title}</td>
                        <td>Open</td>
                      </tr>
                    );
                  })}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
