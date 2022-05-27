# What's your Story? App

This is the frontend repo for full prompted journaling application called 'What's Your Story?'. This app uses PostgreSQL as a database allowing users to document stories from their life based on a randomly provided question/prompt from our application.  Users can even submit their own suggestions for new prompts to provide additional ideas that they would like to write about, and even publish to other writers to use.

## Links 
- [Deployed App](https://robinson4623.github.io/WhatsYourStory/)
- [Frontend Repo](https://github.com/robinson4623/WhatsYourStory)
- [Backend Repo](https://github.com/robinson4623/WhatsYourStory-API)

### Technologies Used

Frontend:
- React
- JavaScript
- Node.js

Backend:
- Django
- PostgreSQL
- Python

## API

### Authentication

| HTTP Method | URL Path      | Action |
|--------|--------------------|-------------|
| POST   | `/sign-up`          | sign-up    |
| POST   | `/sign-in`          | sign-in    |
| PATCH  | `/change-password/` | change password  |
| DELETE | `/sign-out/`        | sign-out   |

### Story Creation

| HTTP Method   | URL Path        | Action |
|--------|------------------------|-------------------|
| POST   | `/stories`             | creates a story|
| GET   | `/stories`             | shows all stories from logged in user    |
| PATCH  | `/stories/:id` | updates upload details  |
| DELETE | `/stories/:id`        | deletes story   |

### Prompt Creation

| HTTP Method   | URL Path        | Action |
|--------|------------------------|-------------------|
| POST   | `/prompts`             | creates a prompt |

## Planning

In preparation for work on this app, I planned out wireframes, entity relationship diagrams, and user stories which can be found below.  

### Wireframe
![App Wireframe](https://drive.google.com/file/d/1opjInsCDzePzzgq_IzmTIb5zd8Qjul6P/view?usp=sharing "What's your Story? App Wireframe")

### Entity Relationship Diagram (ERD)
![App ERD](https://drive.google.com/file/d/1pWMG-DLMcj2gn4VO7MYLGdV2xWDafOPH/view?usp=sharing "What's Your Story? App ERD")

### User Stories
- As a user I want to be able to:
Sign up
Sign in
Change password
Sign out
Read a random prompt
Create a story
Create a prompt
Enter a title
Enter the story
Edit previous title
Edit previous story

### Future Functionality

There a a number of features I am looking to add in the future
- Integration for users to attach their own images to stories (AWS s3 for storage).
- User can select a different prompt if they do not want to write about the given topic without having to click on 'Create Story' button.
- When a user submits a prompt, it can be reviewed by an admin and made available to the public.
- Hide update fields on story index and only show the fields if the update button is clicked.
- Options to get an easy to output format for a users stories so they can be compiled into a different format (family website, hardcover book, etc.)

## About Me

Thanks for dropping by! I am a budding full stack software developer working on several projects for personal continuing education and because I love the process of developing apps that people enjoy!

If you'd like to checkout more of my work, visit the links below!

**Kelly Robinson**
- [GitHub](https://github.com/robinson4623)
- [LinkedIn](https://www.linkedin.com/in/kellymrobinson-dev/)

#### *Cheers!*
