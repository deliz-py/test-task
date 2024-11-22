# Test task
This repository contains the test task. While the task is partially completed, this document outlines the current state of the project and provides a list for the remaining steps needed to finalize the functionality.

## Setup Instructions, how to run
Follow these steps to set up the project.

Clone this repository to your local machine :
```bash
git clone https://github.com/deliz-py/test-task.git
cd tesk-task
```

Create a Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install Dependencies:
```bash
pip install -r requieremnts.txt 
```

Apply migrations:
```bash
python manage.py migrate
```

Start the development server:
```bash
python manage.py runserver
```
### Postman
[Collection](https://www.postman.com/deliz-py/workspace/test-catspy/collection/39934646-2cf86397-e811-418d-90e8-a934dc906d6f?action=share&creator=39934646)

### Implemented Features

1. Django Setup: The Django project is configured with a base structure.

2. Models: `Cat`, `Mission`, `Target`.

3. Basic CRUD Endpoints:
#### Cats

- `POST /api/cats/create/`  
  Create a new cat.

- `GET /api/cats/`  
  Get a list of all cats.

- `DELETE /api/cats/<int:id>/`  
  Delete a cat by its ID.

- `GET /api/cats/<int:id>/`  
  Get information about a cat by its ID.

- `PUT /api/cats/<int:id>/update-salary/`  
  Update a cat's salary by its ID.

#### Missions

- `GET /api/missions/`  
  Get a list of all missions.

  
## Next Steps 
The following steps need to be implemented to finalize the task:

### 1. Complete CRUD Functionality
     - Implement the create a mission endpoint, delete a mission endpoint, assign a cat endpoint, update a note endpoint. 
     - Validate the cat with cat's breed api.
### 2. Add Unit Tests
    - Write test cases for Cat, Mission views.
### 3. Generate API Documentation
    - Integrate Swagger UI using drf-yasg library.

