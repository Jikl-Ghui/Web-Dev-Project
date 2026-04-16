# GroupProject

## Members
Aitzhan Almerek, Augambaev Alen, Narbay Yersaiyn

## Description of Project

It is a streamlined coding practice platform designed to help students sharpen their programming skills. It serves as a lightweight alternative to major competitive programming sites, providing a focused environment where users can solve targeted problems and track their progress through a clean, efficient interface.

Core Data Model
The platform is built on four central entities to ensure a structured and scalable workflow:

User (Student): Represents the platform’s learners, handling authentication and personalizing the experience.

Category: Organizes problems into specific domains, such as Algorithms, SQL, or Data Structures.

Task: The core unit of work, containing detailed problem descriptions, constraints, and difficulty levels (e.g., Easy, Medium, Hard).

Submission: Tracks user interactions, storing the code submitted by a student for a specific task.

Database Relationships
The architecture utilizes ForeignKey relationships to maintain data integrity:

Task → Category: Each task is assigned to a specific category for better navigation.

Submission → Task & User: Each submission is linked to the specific problem it addresses and the student who wrote the code.

Key Features & CRUD Functionality
The platform empowers authorized students with full control over their learning journey:

Create: Submit new solutions for any available task.

Read: Access a comprehensive history of previous attempts and review task requirements.

Update: Refine and resubmit code to improve logic or meet deadlines.

Delete: Remove drafts or obsolete submissions to keep the workspace organized.

## Angular

This project was generated using [Angular CLI](https://github.com/angular/angular-cli) version 21.1.4.

## Development server

To start a local development server, run:

```bash
ng serve
```

Once the server is running, open your browser and navigate to `http://localhost:4200/`. The application will automatically reload whenever you modify any of the source files.

## Code scaffolding

Angular CLI includes powerful code scaffolding tools. To generate a new component, run:

```bash
ng generate component component-name
```

For a complete list of available schematics (such as `components`, `directives`, or `pipes`), run:

```bash
ng generate --help
```

## Building

To build the project run:

```bash
ng build
```

This will compile your project and store the build artifacts in the `dist/` directory. By default, the production build optimizes your application for performance and speed.

## Running unit tests

To execute unit tests with the [Vitest](https://vitest.dev/) test runner, use the following command:

```bash
ng test
```

## Running end-to-end tests

For end-to-end (e2e) testing, run:

```bash
ng e2e
```

Angular CLI does not come with an end-to-end testing framework by default. You can choose one that suits your needs.

## Additional Resources

For more information on using the Angular CLI, including detailed command references, visit the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
