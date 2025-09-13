# Permissions and Groups Setup

## Models
- `Book` model has custom permissions:
  - `can_view`
  - `can_create`
  - `can_edit`
  - `can_delete`

## Groups
- `Admin` → all permissions
- `Editors` → can_view, can_create, can_edit
- `Viewers` → can_view

## Views
- Permissions are enforced using the `@permission_required` decorator:
  - `book_list` → `can_view`
  - `create_book` → `can_create`
  - `edit_book` → `can_edit`
  - `delete_book` → `can_delete`

## How to Test
1. Create users and assign them to groups (`Admin`, `Editors`, `Viewers`).
2. Log in as different users and check access to the views.
3. Users without the required permission will get a `403 Forbidden` error.
