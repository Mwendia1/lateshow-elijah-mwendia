### Late Show Flask API
## Date: 2026/01/11
## By: Elijah Mwendia
## Description

-The Late Show Flask API is a backend web application built using Flask that manages television episodes, guests, and their appearances on the show.

-The application provides a structured RESTful API for handling many-to-many relationships between episodes and guests through appearances, including validations and nested serialization.

-The API replaces manual or static data handling with a fully functional database-backed system that supports creating, reading, and validating records.

-The API follows REST principles and returns JSON responses that can be tested using the provided Postman collection.

## Features

-View a list of all episodes

-View a single episode with its guest appearances

-View a list of all guests

-Create a new appearance linking a guest to an episode

-Validate appearance ratings (must be between 1 and 5)

## Learning Goals

-Understand how to build relational data models using SQLAlchemy

-Practice implementing many-to-many relationships with an association table

-Learn how to apply model validations

-Build RESTful routes using Flask

-Handle errors and HTTP status codes correctly

-Use Postman to test API endpoints

-Work with database migrations and seeding

## Installation
-Download the project files from GitHub
-Navigate into the project directory
-Create and activate a virtual environment
-Install dependencies

## Installation Requirements
-Git
-Python 3.8+
-Flask
-Flask-SQLAlchemy
-Flask-Migrate
-SQLite
-Postman
-Git & GitHub

# GitHub Profile:
https://github.com/elijah-mwendia

## License
-The content of this project is licensed under the MIT License
Copyright © 2026

## About
-This project is part of a Phase 4 backend development challenge focused on building a relational Flask API with validations, serialization rules, database migrations, and proper RESTful routing.

## Languages
-Python