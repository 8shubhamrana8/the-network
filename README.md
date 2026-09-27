### The Network

A Twitter-like social network web application built with Django on the backend and modern JavaScript on the frontend, featuring real-time feed updates, dynamic post editing, follower feeds, and asynchronous like toggling.

🌟 Key Features
New Post Creation: Authenticated users can write and publish new text-based posts instantly.

<img width="1280" height="656" alt="ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/59d2fb65-7be3-418c-bf13-668029dc151f" />

All Posts Feed: A primary social feed listing all posts from all users in reverse chronological order.

Profile Pages:

Displays user metadata, total follower counts, and total following counts.

Lists all posts written by the target user.

<img width="1897" height="978" alt="Screenshot 2026-09-27 224133" src="https://github.com/user-attachments/assets/027cf6d3-828d-4b7a-bdf2-9ec6322bf8d6" />

Interactive Follow / Unfollow toggle button for logged-in users viewing another profile.

<img width="1280" height="661" alt="ezgif com-video-to-gif-converter (1)" src="https://github.com/user-attachments/assets/81ab4eef-88f3-4773-939a-79cd06ee6382" />

Following Feed: A dedicated, filtered feed displaying only posts from users that the logged-in user follows.

<img width="1897" height="980" alt="Screenshot 2026-09-27 224200" src="https://github.com/user-attachments/assets/f87a8f9b-d050-482c-bd59-1b21e0b801e3" />

Paginator Navigation: Server-side pagination breaking posts into manageable chunks (10 posts per page) with Next and Previous navigation controls.

In-Place Post Editing:

<img width="1917" height="980" alt="Screenshot 2026-09-27 224255" src="https://github.com/user-attachments/assets/d5b783b0-37f6-413b-a1d8-0be1a8870032" />

Users can edit their own posts directly within the feed using inline Textareas via JavaScript.

Saves updates via REST API calls without triggering a full page reload or security bypasses.

Asynchronous Like System: Interactive like/unlike counter powered by asynchronous fetch() calls that dynamically update counts and UI icons.

🛠️ Tech Stack
Backend: Python 3, Django

Frontend: JavaScript (ES6+), HTML5, CSS3, Bootstrap 4 / 5

Database: SQLite (Django ORM)

APIs: Custom Django JSON endpoints for post editing, pagination, and liking

💻 Technical Highlights & Architecture
RESTful Asynchronous Interactions: Leveraged native fetch() requests and CSRF token handling to update post content and toggles without page refreshes.

Relational Schema Design: Developed models connecting User, Post, Follow, and Like tables using foreign key relationships and unique constraints.

Client-Side DOM Manipulation: Utilized dynamic event listeners and hidden element switching for seamless in-place editing workflows.

Django Core Pagination: Implemented Django's Paginator class on backend views to optimize query performance and render clear navigation metadata.

🚀 Getting Started
Prerequisites
Python 3.x

Django 3.x or 4.x

pip package manager

Installation & Setup
Clone the repository

Bash
git clone https://github.com/your-username/cs50w-network.git
cd cs50w-network
