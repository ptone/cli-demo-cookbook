# Preface
Before running any instructions on this application, Read the `MIGRATE.md` file in its entirety.

# Cymbal B&B Application

This document provides an overview of the Cymbal B&B application, its architecture, and how to build and run the different components. This document also provides upgrade instructions.

## Overview

Cymbal B&B is a demonstration web application for a bed and breakfast booking site. It consists of a frontend web user interface and a backend catalog service.

## Architecture

The application follows a microservices architecture with a separate frontend and backend.

### Frontend

-   **Location:** `frontend/`
-   **Language:** Go
-   **Description:** The frontend is a web server written in Go. It serves the HTML pages for the user interface, including the home page with all listings and detailed pages for each listing. It communicates with the backend catalog service to fetch listing data.

### Backend

-   **Location:** `catalog/`
-   **Language:** Java
-   **Framework:** Spring Boot
-   **Build Tool:** Maven
-   **Description:** The backend is a Spring Boot application that provides a RESTful API for the catalog of B&B listings.
-   **APIs:**
    -   `GET /listing`: Returns all listings.
    -   `GET /listing/{id}`: Returns a specific listing by its ID.
    -   `POST /resetcache`: Resets the service's cache.
-   **Database:** It uses a PostgreSQL database on Cloud SQL to store the listing information.

## Project Structure

```
/
├── catalog/         # Java Spring Boot backend service
│   ├── pom.xml      # Maven build configuration
│   └── src/         # Java source code
├── frontend/        # Go frontend web application
│   ├── go.mod       # Go module definition
│   └── main.go      # Main application entrypoint
└── .gemini/
    └── GEMINI.md    # This file
```

## How to Build and Run

### Backend (Catalog Service)

The backend is a standard Maven project.

1.  **Navigate to the catalog directory:**
    ```bash
    cd catalog
    ```
2.  **Build the project using Maven:**
    ```bash
    ./mvnw springboot:run
    ```
    This will create a JAR file in the `target/` directory.

3.  **Run the service:**
    The service is designed to run on Cloud Run. Before running, you need to set the following environment variables as described in `catalog/README.md`:
    -   `STATIC_BUCKET_ID`
    -   `SQL_INSTANCE_NAME`
    -   `DB_NAME`
    -   `DB_PWD`

    You can run the application using the `spring-boot-maven-plugin`:
    ```bash
    ./mvnw spring-boot:run
    ```

### Frontend

The frontend is a Go application.

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```
2.  **Run the application:**
    ```bash
    go run .
    ```
    The frontend server will start, and you can access it in your browser. It can also be built and run inside a Docker container as defined in the `frontend/Dockerfile`.

## Java Upgrade Instructions

Before starting any upgrade steps, refer to the `MIGRATE.md` file in its entirety. If an `.upgrade/upgrade_plan.json` file exists, it represents the state of an in-progress upgrade and its steps should be followed.

For interacting with the remote GitLab repository (e.g., creating merge requests, issues), always prefer using the GitLab tools. For local repository actions like staging and committing, using `git` via `run_shell_command` is acceptable.~