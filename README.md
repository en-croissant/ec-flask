# Welcome to En Croissant!

<!-- badges -->

[![MIT license](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/mit-license.php)
[![GitHub latest commit](https://img.shields.io/github/last-commit/en-croissant/ec-flask.svg)](https://github.com/en-croissant/ec-flask)
[![GitHub forks](https://img.shields.io/github/forks/en-croissant/ec-flask.svg)](https://github.com/en-croissant/ec-flask)

This repo hosts the server side of [En Croissant](https://github.com/en-croissant/ec-client).

## Table of Contents

- [Welcome to En Croissant!](#welcome-to-en-croissant)
  - [Table of Contents](#table-of-contents)
- [Installation & Usage](#installation--usage)
    - [Installation & Local Usage](#installation--local-usage)
    - [Deployment](#deployment)
  - [Technologies](#technologies)
- [Database Schema](#database-schema)
- [Routes](#routes)
  - [Auth Routes](#auth-routes)
      - [Body for registration request](#body-for-registration-request)
      - [Body for login request](#body-for-login-request)
  - [User Routes](#user-routes)
  - [Lobby Routes](#lobby-routes)
      - [Body for lobby creation request](#body-for-lobby-creation-request)
  - [Chat Routes](#chat-routes)
      - [Body for chat request](#body-for-chat-request)

# Installation & Usage

### Installation & Local Usage

- Clone the repo
- Open terminal and navigate to the `/ec-flask` folder
- Run `pipenv install` to install dependencies
- Create a `.env` file and add the following:
  - `DATABASE_URL=postgres://rbcbtrrvoeuhdt:10a5ae6e462f7f61df5cf135df75d9986ec4f6d44f87003cb33f47262897e81c@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/da7alfg2fe494l`
  - `SECRET=<choose_your_secret>`
- Run `pipenv run dev` to run the server locally

### Deployment

This server is continuosly deployed on [Heroku](https://en-croissant.herokuapp.com/)

## Technologies

- [Flask 🔗](https://flask.palletsprojects.com/en/2.1.x/)
- [Socket.io 🔗](https://socket.io/)
- [Pytest 🔗](https://docs.pytest.org/en/7.1.x/s)
- [PostgreSQL 🔗](https://www.postgresql.org/)

# Database Schema

We made use of Postgres for our database. 

![screenshot](app/images/db_schema.png)

Note: The chat feature is not curently implemented but storage is set up

View the live schema [here](https://lucid.app/lucidchart/5cc2dc81-b179-4890-b346-ee6bbebe02fe/edit?invitationId=inv_45439b7f-d487-4947-b733-a4a177009eb2&referringApp=slack&page=0_0#&referringApp=slack&loaddialog=SlackLinkPrompt)

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


## Lobby Routes

| **URL**          | **HTTP Verb** | **Action** |
| ---------------- | ------------- | ---------- |
| /lobby           | GET           | index      |
| /lobby           | POST          | create     |
| /lobby/:lobby_id | GET           | show       |

#### Body for lobby creation request

```json
{
  "player_1_username": "example_host",
  "player_2_username": "example_opponent",
  "history": "" // Empty string as no moves have been made
}
```

## Chat Routes

| **URL**          | **HTTP Verb** | **Action** |
| ---------------- | ------------- | ---------- |
| /chat            | GET           | index      |
| /chat            | POST          | create     |

#### Body for chat request

```json 
{
  "lobby_id": 1,
  "user_id": 1,
  "message": "example message",
  "time": "<time>" // format to be decided
}
```
