# # ┌─────────────────────────────────────────────────────────────────┐
# # │                      SYSTEM STRUCTURE                            │
# # ├─────────────────────────────────────────────────────────────────┤
# # │                                                                  │
# # │                      BaseEntity                                  │
# # │                    (id, timestamps)                              │
# # │                          │                                       │
# # │          ┌───────────────┼───────────────┐                      │
# # │          │               │               │                      │
# # │          ▼               ▼               ▼                      │
# # │        User          Project          Task                      │
# # │    (auth, profile)  (container)   (work items)                  │
# # │                          │               │                      │
# # │                          │               ▼                      │
# # │                          │          TaskComment                 │
# # │                          │         (nested entity)              │
# # │                          │                                       │
# # │                          └──────► has many Tasks                │
# # │                                                                  │
# # └─────────────────────────────────────────────────────────────────┘

# ============ BaseEntity ============
# This is the PARENT class for all entities in the system.
# All other models (User, Project, Task, TaskComment) inherit from this.

# PRIVATE ATTRIBUTES:
# - __id (auto-generated: first 8 chars of uuid4)
# - __created_at (datetime.now())
# - __updated_at (datetime.now())

# READ-ONLY PROPERTIES:
# - id -> returns __id
# - created_at -> returns __created_at
# - updated_at -> returns __updated_at

# METHODS:
# - _mark_updated() -> updates __updated_at to current time (protected method)
# - to_dict() -> returns {"id": ..., "created_at": ..., "updated_at": ...}
#                (timestamps as ISO format strings)
# - __str__() -> returns "BaseEntity(id=abc12345)"

# STATIC METHODS:
# - generate_id() -> returns first 8 chars of uuid4






# ============ User ============
# Represents a user in the system with authentication features.

# CLASS VARIABLES:
# - total_users = 0
# - users_by_role = {"admin": 0, "manager": 0, "member": 0}
# - VALID_ROLES = ["admin", "manager", "member"]

# PRIVATE ATTRIBUTES (in addition to inherited):
# - __password_hash (never exposed)
# - __is_active (default: True)

# PROTECTED ATTRIBUTES:
# - _username
# - _email
# - _role (default: "member")

# CONSTRUCTOR:
# __init__(self, username, email, password, role="member"):
# - Call super().__init__()
# - Validate and set all attributes using property setters
# - Hash the password (simple hash for this exercise)
# - Update class statistics

# PROPERTIES:
# - username (read-write, min 3 chars, alphanumeric + underscore only)
# - email (read-write, must contain @ and ., stored lowercase)
# - role (read-write, must be in VALID_ROLES)
# - is_active (read-write, boolean only)
# - password (WRITE-ONLY - raise AttributeError on read)

# COMPUTED PROPERTIES:
# - display_name -> returns "@{username}"
# - is_admin -> returns True if role == "admin"

# METHODS:
# - verify_password(password) -> returns True if hash matches
# - deactivate() -> sets is_active to False
# - activate() -> sets is_active to True
# - to_dict() -> extends parent's to_dict with user fields (NO password!)
# - __str__() -> returns "User(username={username}, role={role})"

# CLASS METHODS:
# - get_statistics() -> returns dict with total_users, users_by_role
# - create_admin(username, email, password) -> creates user with role="admin"
# - from_dict(data) -> creates User from dictionary

# STATIC METHODS:
# - hash_password(password) -> returns simple hash (use hashlib.sha256)
# - validate_email(email) -> returns True if valid format
# - validate_username(username) -> returns True if valid format






# ============ Project ============
# Represents a project that contains multiple tasks.

# CLASS VARIABLES:
# - total_projects = 0
# - VALID_STATUSES = ["planning", "active", "on_hold", "completed", "archived"]

# PROTECTED ATTRIBUTES:
# - _name
# - _description
# - _status (default: "planning")
# - _owner (User instance who owns the project)
# - _members (list of User instances)
# - _tasks (list of Task instances - starts empty)

# CONSTRUCTOR:
# __init__(self, name, description, owner):
# - Call super().__init__()
# - Validate name (min 3 chars)
# - owner must be a User instance
# - Initialize empty members list (add owner automatically)
# - Initialize empty tasks list
# - Update class statistics

# PROPERTIES:
# - name (read-write, min 3 chars)
# - description (read-write)
# - status (read-write, must be in VALID_STATUSES)
# - owner (read-only)
# - members (read-only, returns copy of list)
# - tasks (read-only, returns copy of list)

# COMPUTED PROPERTIES:
# - member_count -> returns number of members
# - task_count -> returns number of tasks
# - completed_task_count -> returns number of tasks with status "done"
# - progress_percentage -> returns (completed_task_count / task_count * 100) or 0

# METHODS:
# - add_member(user) -> adds User to members (validate it's a User instance)
# - remove_member(user) -> removes User from members (can't remove owner!)
# - add_task(task) -> adds Task to tasks (validate it's a Task instance)
# - get_tasks_by_status(status) -> returns list of tasks with that status
# - to_dict() -> extends parent's to_dict (include owner_id, member_ids, task_ids)
# - __str__() -> returns "Project(name={name}, tasks={task_count})"

# CLASS METHODS:
# - get_total_projects() -> returns total_projects






# ============ Task ============
# Represents a task within a project.

# CLASS VARIABLES:
# - total_tasks = 0
# - tasks_by_priority = {"low": 0, "medium": 0, "high": 0, "urgent": 0}
# - VALID_STATUSES = ["todo", "in_progress", "review", "done"]
# - VALID_PRIORITIES = ["low", "medium", "high", "urgent"]

# PROTECTED ATTRIBUTES:
# - _title
# - _description
# - _status (default: "todo")
# - _priority (default: "medium")
# - _assignee (User instance or None)
# - _comments (list of TaskComment instances)

# PRIVATE ATTRIBUTES:
# - __completed_at (None until status becomes "done")

# CONSTRUCTOR:
# __init__(self, title, description="", priority="medium", assignee=None):
# - Call super().__init__()
# - Validate all fields
# - If assignee provided, must be a User instance
# - Initialize empty comments list
# - Update class statistics

# PROPERTIES:
# - title (read-write, min 3 chars)
# - description (read-write)
# - status (read-write with special logic - see below)
# - priority (read-write, must be valid, update statistics on change)
# - assignee (read-write, must be User or None)
# - completed_at (read-only)
# - comments (read-only, returns copy)

# SPECIAL: status setter should:
# - Validate status is in VALID_STATUSES
# - If new status is "done", set __completed_at to datetime.now()
# - If changing FROM "done" to something else, set __completed_at to None
# - Call _mark_updated()

# COMPUTED PROPERTIES:
# - is_completed -> returns True if status == "done"
# - is_assigned -> returns True if assignee is not None
# - comment_count -> returns number of comments

# METHODS:
# - assign_to(user) -> sets assignee (validate it's a User)
# - unassign() -> sets assignee to None
# - add_comment(comment) -> adds TaskComment to comments
# - complete() -> sets status to "done"
# - reopen() -> sets status to "todo"
# - to_dict() -> extends parent's to_dict with task fields
# - __str__() -> returns "Task(title={title}, status={status})"

# CLASS METHODS:
# - get_statistics() -> returns dict with total_tasks, tasks_by_priority
# - from_dict(data) -> creates Task from dictionary

# STATIC METHODS:
# - validate_priority(priority) -> returns True if valid








# ============ TaskComment ============
# Represents a comment on a task.

# CLASS VARIABLES:
# - total_comments = 0

# PROTECTED ATTRIBUTES:
# - _content
# - _author (User instance)

# PRIVATE ATTRIBUTES:
# - __is_edited (default: False)
# - __edited_at (None until edited)

# CONSTRUCTOR:
# __init__(self, content, author):
# - Call super().__init__()
# - Validate content (min 1 char)
# - author must be a User instance
# - Update class statistics

# PROPERTIES:
# - content (read-write, min 1 char, set __is_edited and __edited_at on change)
# - author (read-only)
# - is_edited (read-only)
# - edited_at (read-only)

# COMPUTED PROPERTIES:
# - preview -> returns first 50 chars of content + "..." if longer

# METHODS:
# - edit(new_content) -> updates content (triggers edited flags)
# - to_dict() -> extends parent's to_dict with comment fields
# - __str__() -> returns "Comment(by={author.username}, preview={preview})"

# CLASS METHODS:
# - get_total_comments() -> returns total_comments








# ============ TEST SCENARIOS ============
# Run these tests to verify your implementation works correctly.

# print("=" * 70)
# print("TASK MANAGEMENT SYSTEM - TEST SUITE")
# print("=" * 70)

# # ============ TEST 1: User Creation ============
# print("\n[TEST 1] User Creation and Validation")
# print("-" * 50)

# # Create users
# admin = User.create_admin("admin_user", "admin@company.com", "adminpass123")
# manager = User("john_manager", "JOHN@COMPANY.COM", "password123", role="manager")
# member1 = User("alice_dev", "alice@company.com", "securepass1")
# member2 = User("bob_dev", "bob@company.com", "securepass2")

# print(f"Created: {admin}")
# print(f"Created: {manager}")
# print(f"Admin's display name: {admin.display_name}")
# print(f"Is admin check: {admin.is_admin}")
# print(f"Email normalized: {manager.email}")  # Should be lowercase

# # Test password
# print(f"Password verify (correct): {manager.verify_password('password123')}")
# print(f"Password verify (wrong): {manager.verify_password('wrongpass')}")

# # Test validation
# try:
#     bad_user = User("ab", "test@test.com", "password123")  # username too short
# except ValueError as e:
#     print(f"✓ Validation caught: {e}")

# # Statistics
# print(f"User stats: {User.get_statistics()}")


# # ============ TEST 2: Project Creation ============
# print("\n[TEST 2] Project Creation")
# print("-" * 50)

# project = Project(
#     name="Website Redesign",
#     description="Redesign the company website with modern UI",
#     owner=manager
# )

# print(f"Created: {project}")
# print(f"Owner: {project.owner.username}")
# print(f"Initial member count: {project.member_count}")

# # Add members
# project.add_member(member1)
# project.add_member(member2)
# print(f"After adding members: {project.member_count}")

# # Try to remove owner
# try:
#     project.remove_member(manager)
# except ValueError as e:
#     print(f"✓ Cannot remove owner: {e}")


# # ============ TEST 3: Task Creation and Management ============
# print("\n[TEST 3] Task Creation and Management")
# print("-" * 50)

# task1 = Task(
#     title="Design Homepage Mockup",
#     description="Create initial design mockups for the homepage",
#     priority="high",
#     assignee=member1
# )

# task2 = Task(
#     title="Implement Header Component",
#     description="Build responsive header with navigation",
#     priority="medium"
# )

# task3 = Task(
#     title="Setup Database",
#     priority="urgent",
#     assignee=member2
# )

# print(f"Created: {task1}")
# print(f"Is assigned: {task1.is_assigned}")
# print(f"Assignee: {task1.assignee.username}")

# # Add tasks to project
# project.add_task(task1)
# project.add_task(task2)
# project.add_task(task3)

# print(f"Project task count: {project.task_count}")
# print(f"Progress: {project.progress_percentage}%")

# # Complete a task
# task1.complete()
# print(f"Task1 completed at: {task1.completed_at}")
# print(f"Progress after completion: {project.progress_percentage}%")

# # Reopen task
# task1.reopen()
# print(f"After reopen - completed_at: {task1.completed_at}")

# # Change priority
# print(f"Task stats before: {Task.get_statistics()}")
# task2.priority = "high"
# print(f"Task stats after priority change: {Task.get_statistics()}")


# # ============ TEST 4: Comments ============
# print("\n[TEST 4] Comments on Tasks")
# print("-" * 50)

# comment1 = TaskComment(
#     content="Looking great! Just a few minor adjustments needed.",
#     author=manager
# )

# comment2 = TaskComment(
#     content="I've updated the colors as requested. Please review.",
#     author=member1
# )

# task1.add_comment(comment1)
# task1.add_comment(comment2)

# print(f"Task1 comment count: {task1.comment_count}")
# print(f"Comment preview: {comment1.preview}")
# print(f"Comment: {comment1}")

# # Edit comment
# comment1.edit("Actually, this looks perfect now!")
# print(f"Is edited: {comment1.is_edited}")
# print(f"Edited at: {comment1.edited_at}")


# # ============ TEST 5: Read-Only Properties ============
# print("\n[TEST 5] Read-Only Properties")
# print("-" * 50)

# try:
#     project.owner = admin  # Should fail
# except AttributeError:
#     print("✓ Cannot change project owner")

# try:
#     task1.completed_at = datetime.now()  # Should fail
# except AttributeError:
#     print("✓ Cannot set completed_at directly")

# try:
#     print(admin.password)  # Should fail
# except AttributeError:
#     print("✓ Cannot read password")


# # ============ TEST 6: to_dict() Methods ============
# print("\n[TEST 6] Serialization (to_dict)")
# print("-" * 50)

# print("User dict:")
# print(manager.to_dict())

# print("\nTask dict:")
# print(task1.to_dict())

# print("\nProject dict:")
# print(project.to_dict())


# # ============ TEST 7: Factory Methods ============
# print("\n[TEST 7] Factory Methods")
# print("-" * 50)

# user_data = {
#     "username": "new_user",
#     "email": "new@company.com",
#     "password": "newpass123",
#     "role": "member"
# }
# new_user = User.from_dict(user_data)
# print(f"Created from dict: {new_user}")

# task_data = {
#     "title": "New Task from Dict",
#     "description": "This task was created from a dictionary",
#     "priority": "low"
# }
# new_task = Task.from_dict(task_data)
# print(f"Created from dict: {new_task}")


# # ============ TEST 8: Project Queries ============
# print("\n[TEST 8] Project Queries")
# print("-" * 50)

# task1.status = "in_progress"
# task2.status = "done"
# task3.status = "in_progress"

# print(f"Tasks in progress: {[t.title for t in project.get_tasks_by_status('in_progress')]}")
# print(f"Completed tasks: {[t.title for t in project.get_tasks_by_status('done')]}")
# print(f"Final progress: {project.progress_percentage:.1f}%")


# # ============ TEST 9: Encapsulation Check ============
# print("\n[TEST 9] Encapsulation Verification")
# print("-" * 50)

# # Verify private attributes are not directly accessible
# try:
#     print(manager._User__password_hash)
#     print("(Note: Can access via name mangling, but shouldn't!)")
# except AttributeError:
#     print("Private attributes properly hidden")

# # Verify lists are copies (encapsulation of collections)
# tasks_copy = project.tasks
# tasks_copy.append("fake task")
# print(f"Original task count unchanged: {project.task_count}")  # Should be same


# # ============ FINAL SUMMARY ============
# print("\n" + "=" * 70)
# print("FINAL STATISTICS")
# print("=" * 70)

# print(f"\nUsers: {User.get_statistics()}")
# print(f"Tasks: {Task.get_statistics()}")
# print(f"Projects: {Project.get_total_projects()}")
# print(f"Comments: {TaskComment.get_total_comments()}")

# print("\n" + "=" * 70)
# print("ALL TESTS COMPLETED!")
# print("=" * 70)