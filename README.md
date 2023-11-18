# Todo-app


- Access the [Todo App documentation](https://todo-app-34vp.onrender.com/docs) for detailed information and instructions on using the application.
- The application is deployed on [Render](https://dashboard.render.com/select-repo?type=web). Click the link to access the deployment and explore the live environment.


# FastAPI Todo and User Management

This FastAPI application provides endpoints for managing todos and users. The application uses MongoDB as its database.

## Todo Management

### Get Todos

- **Endpoint:** `/gettodo`
- **Method:** GET
- **Description:** Retrieves a list of todos.
- **Response:**
  - `todos`: List of todos.
  - `total`: Total number of todos.

### Post Todo

- **Endpoint:** `/posttodo`
- **Method:** POST
- **Description:** Adds a new todo.
- **Request Body:**
  - `title`: Title of the todo.
  - `description`: Description of the todo.
- **Response:**
  - `id`: Unique identifier of the newly created todo.
  - `title`: Title of the todo.
  - `description`: Description of the todo.

### Update Todo

- **Endpoint:** `/{id}`
- **Method:** PUT
- **Description:** Updates an existing todo.
- **Path Parameter:**
  - `id`: Unique identifier of the todo to be updated.
- **Request Body:**
  - `title`: New title of the todo.
  - `description`: New description of the todo.
- **Response:**
  - `message`: Success message.

### Delete Todo

- **Endpoint:** `/deletetodo/{id}`
- **Method:** DELETE
- **Description:** Deletes a todo.
- **Path Parameter:**
  - `id`: Unique identifier of the todo to be deleted.
- **Response:**
  - `message`: Success message.

## User Management

### Post User

- **Endpoint:** `/postuser`
- **Method:** POST
- **Description:** Adds a new user.
- **Request Body:**
  - `username`: Unique username of the user.
  - `email`: Email address of the user.
  - `password`: Password of the user.
- **Response:**
  - `id`: Unique identifier of the newly created user.
  - `username`: Username of the user.
  - `email`: Email address of the user.

### Get Users

- **Endpoint:** `/getusers`
- **Method:** GET
- **Description:** Retrieves a list of users.
- **Response:**
  - `users`: List of users.
  - `total`: Total number of users.

## Error Handling

- If a todo with a specific ID is not found during update or delete operations, a `404 Not Found` error is returned.
- If a duplicate username is detected during user creation, a `400 Bad Request` error is returned with the message "Username already exists."
- If any other error occurs during the operation, a generic `500 Internal Server Error` is returned with details of the error.

Feel free to use the provided endpoints to manage your todos and users efficiently! If you have any questions or encounter issues, please contact the system administrator.
