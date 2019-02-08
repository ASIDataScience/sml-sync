import uuid

import faculty


project_client = faculty.client("project")
account_client = faculty.client("account")


def resolve_project(project):
    """Resolve a project name or ID to a project ID."""
    try:
        project_id = uuid.UUID(project)
        project = project_client.get(project_id)
    except ValueError:
        user_id = account_client.authenticated_user_id()
        projects = [
            p
            for p in project_client.list_accessible_by_user(user_id)
            if p.name == project
        ]
        if len(projects) == 1:
            project = projects[0]
        else:
            raise ValueError("Could not resolve project.")
    return project
