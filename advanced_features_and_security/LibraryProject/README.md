## Permissions and Groups Setup

This application uses Django’s built-in permissions and groups system to control access based on user roles.

### Custom Permissions
- **can_view**: Allows viewing books.
- **can_create**: Allows creating new books.
- **can_edit**: Allows editing books.
- **can_delete**: Allows deleting books.

### Groups
- **Viewers**: Users who can only view books.
- **Editors**: Users who can create and edit books.
- **Admins**: Users who have full control, including viewing, creating, editing, and deleting books.

### Enforcing Permissions
Permissions are enforced using the `permission_required` decorator in views. If a user does not have the required permission, they will receive a 403 Forbidden error.
