# This is the phase-4 social media flask api
# **CON-NECT**: Social Media Application(Project)
**Authours**: *John Maluki*, *Martin Nyaga*, *Edmond Wayama*, *Levina Njambi*, *Brian Maina*

## Prerequisites

**Technologies Used Within The Creation Of This Project**
<li>Python
<li>Flask
<li>Flask SQLAlchemy
<li>JSON


### The Guideline To The Creation Of **CON_NECT**

# Social Media App

#### Created By [John Maluki*,*Martin Nyaga*, *Edmond Wayama*, *Levina Njambi*, *Brian Maina*] [Date Created]

## Introduction

This is a social media app api designed for the con-nect web app. It provides users with a platform to connect, share updates, and engage with others in a social networking environment.


## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/MartinNyaga/social-media-api/tree/Development


## Relationships

- **Users and Posts**: Users can create and manage multiple posts. This is a one-to-many relationship, where each user can have many posts, but each post belongs to one user.

- **Users and Likes**: Users can like multiple posts, and posts can be liked by multiple users. This is a many-to-many relationship, facilitated by an intermediate table that connects users and posts.

- **Posts and Comments**: Posts can receive multiple comments. This is a one-to-many relationship, where each post can have many comments, but each comment is associated with one post.

- **Users and Location**: Each user can have an associated location, representing their physical or preferred location. This is a one-to-one relationship, where each user has one location.


## Routes

### `/sign_up`

- **Method**: POST
- **Purpose**: Allows users to create a new account.
- **Request Body**: User registration information (e.g., username, email, password).
- **Response**: Upon successful registration, the user is created, and a JSON response confirms the registration. In case of validation errors or duplicate username/email, appropriate error messages are returned.

### `/login`

- **Method**: POST
- **Purpose**: Enables users to log in to their existing accounts.
- **Request Body**: User login credentials (e.g., username/email and password).
- **Response**: Upon successful login, a JSON response confirms the authentication and provides an access token for subsequent requests. In case of invalid credentials or other errors, appropriate error messages are returned.

### `/reset_password`

- **Method**: POST
- **Purpose**: Allows users to reset their password if forgotten.
- **Request Body**: User's email address to send the password reset instructions.
- **Response**: If the email exists in the system, a JSON response indicates that password reset instructions have been sent. Otherwise, an error message is returned.

### `/posts`

- **Method**: GET
- **Purpose**: Retrieves a list of posts from users.
- **Response**: Returns a JSON array of posts, each containing information such as the post's content, author, timestamp, and comments. This endpoint may support query parameters for filtering and pagination.

### `/posts/{post_id}`

- **Method**: GET
- **Purpose**: Retrieves a specific post by its ID.
- **Response**: Returns a JSON object containing detailed information about the post, including its content, author, timestamp, and comments. If the post does not exist, an appropriate error message is returned.


## Known Bugs

No known bugs at the moment

## Support and contact details 

To make a contribution to the code used or any suggestions you can click on the contact link and email me your suggestions.

- Email: levina.njambi@student.moringaschool.com
- Email: wanyama@student.moringaschool.com
- Email: martin.nyaga@student.moringaschool.com
- Email: brian.maina@student.moringaschool.com
- Email: john.maluki@student.moringaschool.com


#### License
Copyright (c) {{ 2023 }}, {{CON_NECT.org}}

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
