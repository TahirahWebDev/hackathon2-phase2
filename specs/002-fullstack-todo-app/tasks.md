---

description: "Task list for Phase II Full-Stack Todo Application"
---

# Tasks: Phase II Full-Stack Todo Application

**Input**: Design documents from `/specs/002-fullstack-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume web app - adjust based on plan.md structure

## Constitutional Compliance Checks

Before task execution, ensure each task:

- [x] Aligns with Spec-Driven Development: Each task is traceable to approved specification
- [x] Follows Agent-Centric Development: Tasks must be implementable by AI agents without human coding
- [x] Uses Required Technology Stack: Phase I: console only; Phase II: Python REST API, Neon Serverless PostgreSQL, SQLModel, Next.js, Better Auth; Phase III+: AI/agents allowed
- [x] Maintains Phase Governance: No future-phase features included in current phase tasks
- [x] Meets Quality Assurance Standards: Testing and validation requirements included

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create backend directory structure per implementation plan
- [x] T002 Create frontend directory structure per implementation plan
- [ ] T003 [P] Initialize backend project with FastAPI dependencies
- [ ] T004 [P] Initialize frontend project with Next.js dependencies
- [x] T005 Create pyproject.toml for backend project
- [x] T006 Create package.json for frontend project
- [ ] T007 [P] Configure linting and formatting tools for backend (ruff, black, mypy)
- [ ] T008 [P] Configure linting and formatting tools for frontend (ESLint, Prettier)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T009 Setup database schema and migrations framework in backend/src/database/
- [x] T010 [P] Create User model in backend/src/models/user.py
- [x] T011 [P] Create Todo model in backend/src/models/todo.py
- [x] T012 Create database connection service in backend/src/database/database.py
- [x] T013 [P] Implement authentication service in backend/src/services/auth_service.py
- [x] T014 [P] Implement user service in backend/src/services/user_service.py
- [x] T015 Implement todo service in backend/src/services/todo_service.py
- [x] T016 Setup API routing structure in backend/src/api/main.py
- [x] T017 [P] Setup authentication endpoints in backend/src/api/auth.py
- [x] T018 [P] Setup todos endpoints in backend/src/api/todos.py
- [x] T019 Create API response models in backend/src/api/models/
- [x] T020 Setup authentication middleware in backend/src/middleware/
- [x] T021 [P] Create frontend API service in frontend/src/services/api.ts
- [x] T022 [P] Create frontend auth service in frontend/src/services/auth.ts
- [x] T023 Create frontend AuthContext in frontend/src/context/AuthContext.tsx

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - User Registration and Authentication (Priority: P1) 🎯 MVP

**Goal**: Enable new users to create an account and log in to access their todo lists

**Independent Test**: Can be fully tested by creating a new user account, verifying the account creation process works, and then logging in with the new credentials to access the application.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T024 [P] [US1] Contract test for signup endpoint in backend/tests/contract/test_auth.py
- [ ] T025 [P] [US1] Contract test for signin endpoint in backend/tests/contract/test_auth.py
- [ ] T026 [P] [US1] Unit test for auth service in backend/tests/unit/test_auth_service.py
- [ ] T027 [P] [US1] Unit test for user service in backend/tests/unit/test_user_service.py

### Implementation for User Story 1

- [x] T028 [P] [US1] Create signup page in frontend/src/pages/signup.tsx
- [x] T029 [P] [US1] Create signin page in frontend/src/pages/signin.tsx
- [x] T030 [P] [US1] Create AuthForm component in frontend/src/components/AuthForm.tsx
- [x] T031 [US1] Implement signup endpoint in backend/src/api/auth.py
- [x] T032 [US1] Implement signin endpoint in backend/src/api/auth.py
- [x] T033 [US1] Implement signout endpoint in backend/src/api/auth.py
- [x] T034 [US1] Add password hashing to user service in backend/src/services/user_service.py
- [x] T035 [US1] Add JWT token generation to auth service in backend/src/services/auth_service.py
- [x] T036 [US1] Add auth state handling to AuthContext in frontend/src/context/AuthContext.tsx
- [x] T037 [US1] Add navigation after auth to frontend/src/pages/signup.tsx and frontend/src/pages/signin.tsx
- [x] T038 [US1] Add error handling for auth in frontend/src/components/AuthForm.tsx

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Todo Management (Priority: P1)

**Goal**: Allow authenticated users to create, view, update, and delete their todos

**Independent Test**: Can be fully tested by logging in as a user, creating a todo, viewing it in the list, editing it, marking it as complete, and finally deleting it.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T039 [P] [US2] Contract test for todos endpoints in backend/tests/contract/test_todos.py
- [ ] T040 [P] [US2] Unit test for todo service in backend/tests/unit/test_todo_service.py
- [ ] T041 [P] [US2] Integration test for todos functionality in backend/tests/integration/test_todos.py

### Implementation for User Story 2

- [x] T042 [P] [US2] Create dashboard page in frontend/src/pages/dashboard.tsx
- [x] T043 [P] [US2] Create TodoList component in frontend/src/components/TodoList.tsx
- [x] T044 [P] [US2] Create TodoItem component in frontend/src/components/TodoItem.tsx
- [x] T045 [P] [US2] Create TodoForm component in frontend/src/components/TodoForm.tsx
- [ ] T046 [US2] Implement GET /api/todos endpoint in backend/src/api/todos.py
- [ ] T047 [US2] Implement POST /api/todos endpoint in backend/src/api/todos.py
- [ ] T048 [US2] Implement GET /api/todos/{id} endpoint in backend/src/api/todos.py
- [ ] T049 [US2] Implement PUT /api/todos/{id} endpoint in backend/src/api/todos.py
- [ ] T050 [US2] Implement PATCH /api/todos/{id}/toggle endpoint in backend/src/api/todos.py
- [ ] T051 [US2] Implement DELETE /api/todos/{id} endpoint in backend/src/api/todos.py
- [ ] T052 [US2] Add user-scoped data access enforcement to todo service in backend/src/services/todo_service.py
- [x] T053 [US2] Add frontend integration for todo listing in frontend/src/pages/dashboard.tsx
- [x] T054 [US2] Add frontend integration for todo creation in frontend/src/components/TodoForm.tsx
- [x] T055 [US2] Add frontend integration for todo editing in frontend/src/components/TodoItem.tsx
- [x] T056 [US2] Add frontend integration for todo deletion in frontend/src/components/TodoItem.tsx
- [x] T057 [US2] Add frontend integration for todo toggle in frontend/src/components/TodoItem.tsx

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Responsive Todo Interface (Priority: P2)

**Goal**: Provide a responsive UI that works well on both desktop and mobile devices

**Independent Test**: Can be fully tested by accessing the todo application on both desktop and mobile devices and verifying that the interface is usable and functional on both.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T058 [P] [US3] Responsive design tests in frontend/tests/e2e/test_responsive.ts
- [ ] T059 [P] [US3] Component rendering tests for different screen sizes in frontend/tests/unit/test_components.tsx

### Implementation for User Story 3

- [ ] T060 [P] [US3] Add responsive layout to dashboard page in frontend/src/pages/dashboard.tsx
- [ ] T061 [P] [US3] Add responsive layout to signup page in frontend/src/pages/signup.tsx
- [ ] T062 [P] [US3] Add responsive layout to signin page in frontend/src/pages/signin.tsx
- [ ] T063 [P] [US3] Add responsive styles to TodoList component in frontend/src/components/TodoList.tsx
- [ ] T064 [P] [US3] Add responsive styles to TodoItem component in frontend/src/components/TodoItem.tsx
- [ ] T065 [P] [US3] Add responsive styles to TodoForm component in frontend/src/components/TodoForm.tsx
- [ ] T066 [P] [US3] Add responsive styles to AuthForm component in frontend/src/components/AuthForm.tsx
- [ ] T067 [US3] Add mobile navigation to frontend layout
- [ ] T068 [US3] Add responsive breakpoints using Tailwind CSS classes

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Error Handling and Edge Cases

**Goal**: Implement proper error handling and edge case management

- [ ] T069 [P] Add backend error handling middleware in backend/src/middleware/error_handler.py
- [ ] T070 [P] Add frontend error display components in frontend/src/components/ErrorDisplay.tsx
- [ ] T071 [P] Handle unauthorized access errors in frontend/src/services/api.ts
- [ ] T072 [P] Handle invalid input errors in frontend/src/components/TodoForm.tsx
- [ ] T073 Handle empty todo list state in frontend/src/components/TodoList.tsx
- [ ] T074 Handle auth token expiration in frontend/src/context/AuthContext.tsx
- [ ] T075 Add backend validation for all API endpoints
- [ ] T076 Add frontend validation to forms

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T077 [P] Add documentation in docs/
- [ ] T078 Add environment configuration management
- [ ] T079 [P] Performance optimization across all stories
- [ ] T080 [P] Additional unit tests (if requested) in backend/tests/unit/ and frontend/tests/unit/
- [ ] T081 Security hardening
- [ ] T082 Run quickstart.md validation
- [ ] T083 Add README with setup instructions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on User Story 1 (auth required)
- **User Story 3 (P3)**: Can start after User Story 2 (Phase 4) - Can work in parallel but depends on UI components

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, User Stories 1 and 2 can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for signup endpoint in backend/tests/contract/test_auth.py"
Task: "Contract test for signin endpoint in backend/tests/contract/test_auth.py"
Task: "Unit test for auth service in backend/tests/unit/test_auth_service.py"
Task: "Unit test for user service in backend/tests/unit/test_user_service.py"

# Launch all components for User Story 1 together:
Task: "Create signup page in frontend/src/pages/signup.tsx"
Task: "Create signin page in frontend/src/pages/signin.tsx"
Task: "Create AuthForm component in frontend/src/components/AuthForm.tsx"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2 (after US1 auth is available)
   - Developer C: User Story 3 (after UI components are available)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence