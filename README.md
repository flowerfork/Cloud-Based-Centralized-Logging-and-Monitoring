# CloudPulse AI

### Cloud-Based Centralized Logging and Distributed Application Monitoring Platform

Hey! Welcome to our project, **CloudPulse AI**.

We're a team of three students working on a cloud-based monitoring platform as part of our Cloud Infrastructure and Services course.

So, here's the idea.

When an application runs on multiple servers, keeping track of everything happening behind the scenes isn't always easy. Logs are spread across different instances, errors can be difficult to trace, and figuring out why an application suddenly slows down can take a lot of time.

We wanted to build something that makes this process easier.

That's where CloudPulse AI comes in!

We're working on a platform that brings application logs, server information and performance metrics together in one place. The idea is to give developers a simple way to see what's happening with their applications without having to check every server individually.

## What are we trying to build?

We want our platform to make it easier to:

- View application logs from different servers in one place.
- Keep an eye on CPU usage, memory and overall system performance.
- Identify application errors and understand when something goes wrong.
- Monitor multiple Docker containers running on AWS.
- Use AWS CloudWatch to collect logs and monitor infrastructure.
- Automatically manage application instances using Auto Scaling.
- Distribute incoming traffic using a Load Balancer.
- Explore machine learning to identify unusual system behaviour.

## Tools and Technologies

Here's what we're planning to work with:

- **Python & FastAPI** – Backend development.
- **React.js** – Building the monitoring dashboard.
- **Docker** – Running applications inside containers.
- **AWS EC2** – Hosting our applications.
- **AWS CloudWatch** – Collecting logs and monitoring performance.
- **Application Load Balancer** – Distributing incoming requests.
- **Auto Scaling Groups** – Managing application instances.
- **PostgreSQL** – Storing application information.
- **Scikit-learn** – Exploring machine learning for anomaly detection.

## How do we imagine it working?

Our applications will run inside Docker containers on multiple AWS EC2 instances.

Whenever someone accesses the application, the Load Balancer will distribute incoming requests across the available instances. Auto Scaling will help manage changes in traffic.

Meanwhile, CloudWatch will collect information about what's happening in the background, including application logs, resource usage and errors.

All this information will eventually come together in our own monitoring dashboard, so we can understand the health and performance of our applications from one place.

## Our Development Progress

We're building this project step by step, and this repository will be updated as we make progress.

- [ ] Set up the project and development environment
- [ ] Build the backend using FastAPI
- [ ] Create the React dashboard
- [ ] Configure Docker containers
- [ ] Set up centralized logging
- [ ] Configure AWS infrastructure
- [ ] Deploy applications on EC2
- [ ] Set up Load Balancing and Auto Scaling
- [ ] Integrate CloudWatch
- [ ] Experiment with AI-based anomaly detection
- [ ] Test and document the complete system

## Meet the Team

We're Team 4, a group of three students working together to bring this project to life.

| Team Member | Roll Number |
|---|---|
| Mahathi | 2520080030 |
| Sahasra Y | 2520080062 |
| Satya Rishith | 2520080049 |

**Project Guide:** Dr. Gayatri

**Department:** AI & DS, CSIT

**Academic Year:** 2026–2027

---
