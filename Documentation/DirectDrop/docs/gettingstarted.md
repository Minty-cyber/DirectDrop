### Prerequisites

Ensure you have the following installed on your system:

- [Python](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/en/download/prebuilt-installer/current)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Docker & Docker Compose (optional, for containerization)](https://docs.docker.com/desktop/)

### Instructions for setting up locally

#### Backend Setup (FastAPI)

1. **Clone the Repository:**

    ```
    git clone https://github.com/eugeneanokye99/directdrop.git
    ```
    ```
       cd your-cloned-repo
    ```

2. **Set Up Virtual Environment:**

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**

    ```
    pip install -r requirements.txt
    ```

4. **Navigate to Backend Directory:**

    ```
    cd Backend/app
    ```

5. **Run Database Migrations:**

    ```
    alembic upgrade head
    ```
    
6. **Start the backend server with FastAPI CLI:**

    ```
    fastapi run dev
    ```

7.  **View the endpoints with Postman(Optional, but recommended):**

    ```
    http://localhost:8000
    ```


#### Frontend Setup (React with ChakraUI and TailwindCSS)

1. **Navigate to Frontend Directory:**

    ```
    cd Frontend/directdrop
    ```

2. **Install Dependencies:**

    ```
    npm install
    ```

3. **Start the frontend server with Vite:**

    ```
    npm run dev
    ```


#### Asynchronous Tasks (Celery & Redis)

1. **Ensure Redis is Running:**
 
    
    ```
    docker run -d -p 6379:6379 redis
    ```
    or 
    ```
    redis-cli
    ```

2. **Start Celery Worker:**

    ```
    celery -A your_project worker - --loglevel=info
    ```
    ```


#### Environment Variables

Create a `.env` file in the root directory and configure the necessary variables. You can use `.env` as a template.


*Variables used in this project in the `.env` file are given below:*

```

SECRET_KEY=40ed6d187870438c4bf02ed014293b3df00e15888ae915f615ae183b0fb6e7af


```
