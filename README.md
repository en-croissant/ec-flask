# Welcome to En Croissant!

<!-- badges -->

[![MIT license](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/mit-license.php)
[![GitHub latest commit](https://img.shields.io/github/last-commit/en-croissant/ec-flask.svg)](https://github.com/en-croissant/ec-flask)
[![GitHub forks](https://img.shields.io/github/forks/en-croissant/ec-flask.svg)](https://github.com/en-croissant/ec-flask)

This repo hosts the server side of [En Croissant](https://github.com/en-croissant/ec-client).

## Table of Contents

- [Installation & Usage](#installation--usage)
- [Technologies](#technologies)
- [Database Schema](#database-schema)
- [Routes](#routes)

# Installation & Usage

### Installation & Local Usage

- Clone the repo
- Open terminal and navigate to the `/ec-flask` folder
- Run `pipenv install` to install dependencies
- Run `pipenv run start` to run the server locally

### Deployment

This server is continuosly deployed on [Heroku](https://en-croissant.herokuapp.com/)

## Technologies

- [Flask 🔗](https://flask.palletsprojects.com/en/2.1.x/)
- [Socket.io 🔗](https://socket.io/)
- [Pytest 🔗](https://docs.pytest.org/en/7.1.x/s)
- [MongoDB 🔗](https://www.mongodb.com/)
- [MongoDB Atlas 🔗](https://www.mongodb.com/atlas/database)

# Database Schema

- `users`

#### Users schema example:

```json
{
  "username": "test_guy",
  "email": "test_guy@email.com",
  "password_digest": "$2a$10$tCppT1FG0aL9Hj4sHGyZHh6r5OUTLEvAcIorq"
}
```

# Routes

## Auth Routes

| **URL**        | **HTTP Verb** | **Action**     |
| -------------- | ------------- | -------------- |
| /auth/login    | POST          | authentication |
| /auth/register | POST          | authentication |

#### Body for registration request

```json
{
  "username": "new_username",
  "email": "new_email",
  "password": "new_password"
}
```

#### Body for login request

```json
{
  "username": "example_guy",
  "password": "example_password"
}
```

## User Routes

| **URL**          | **HTTP Verb** | **Action** |
| ---------------- | ------------- | ---------- |
| /users           | GET           | index      |
| /users/:username | GET           | show       |


