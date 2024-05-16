# WOBOT AI TODO RESTAPI SERVICE

## **Note:**
Before running the project, follow these steps:
1. **Prequisites:**
    ```bash
    Docker
    ```
2. **Clone the Repository:**
    ```bash
    git clone https://github.com/OxOv3rH4uL/Wobot-AI-Todo
    ```
3. **If you don't have Docker then follow these steps:**
    ```bash
    cd Wobot-AI-Todo
    pip install -r requirements.txt
    bash start.sh
    ```
4. **If you are having Docker then follow these steps:**
    ```bash
    cd Wobot-AI-Todo
    docker-compose up -d
    ```
5. **Enjoy the RestAPI Service:**
    Open the browser and visit the following link to explore the RESTAPI Service
    ```bash
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/docs
    ```

## **Introduction:**

Wobot-AI-Todo utilized FastAPI and MySQL for Backend Services.

```bash
1. Title - Mandatory
2. Description - Mandatory
3. Status - Mandatory - pending or completed
```

## **Features:**
Authentication Oriented RESTAPI

## **Endpoints:**
1) The First Step is to create user:
    - `/signup` (POST):
      - User details such as username and password is provided

      ```bash
      http://127.0.0.1:8000/signup

      {
        "username":"test",
        "password":"123"
      }
      ```

      **Output:**
      ```bash
      {
        "message":"Account created Successfully!"
      }

2) Now after creating user , go to this link:
    ```bash
    http://127.0.0.1:8000/docs
    ```
    - Authorize the user by giving the created credentials

    - Now you can use the RESTAPI using SwaggerUI

3) **Create Todo**
    - `/todos` (POST):
      - Todos are created
      ```bash
      http://127.0.0.1:8000/todos

      {
        "title":"Todo 1",
        "description":"Todo 1 Description",
        "status":"pending"
      }
      ```

      **Output:**
      ```bash
      {
        "message": "Todo Added Successfully!"
      }
      ``
4) **Get All Todo**
    - `/todos` (GET):
    - List all Todos of the User

    ```bash
    http://127.0.0.1:8000/todos
    ```
    **Output:**
    ```bash
    [
        {
            "id": 1,
            "uid": 1,
            "title": "Todo 1",
            "description": "Todo 1 Description",
            "status": "pending"
        }
    ]
    ```
5) **Get a particular Todo**
    - `/todos/{id}` (GET)
    - List information about a particular todo of the user

    ```bash
    http://127.0.0.1:8000/todos/1
    ```

    **Output:**
    ```bash
    {
        "id": 1,
        "uid": 1,
        "title": "Todo 1",
        "description": "Todo 1 Description",
        "status": "pending"
    }
    ```

6) **Update a Todo**
    - `/todos/{id}` (PATCH)
    - Updates the details of a particular Todo of the User

    ```bash
    https://127.0.0.1:8000/todos/1
    {
        "title":"Todo 1",
        "description":"Updated Description of Todo 1",
        "status":"pending"
    }
    ```
    **Output:**
    ```bash
    {
        "message": "Todo Updated Successfully!"
    }
    ```

7) **Delete a Todo**
    - `/todos/{id}` (DELETE)
    - Deletes a Todo of the User

    ```bash
    https:127.0.0.1:8000/1
    ```

    **Output:**

    ```bash
    {
        "message": "Todo Deleted Successfully!"
    }
    
    ```

## **Conclusion:**
This project was really fun to work with!

