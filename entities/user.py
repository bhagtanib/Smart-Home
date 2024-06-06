class User:
    def __init__(self, user_id, name, logger=None):
        self.user_id = user_id
        self.name = name
        self.permissions = []
        self.logger = logger

    def grant_permission(self, permission):
        if permission not in self.permissions:
            self.permissions.append(permission)
            print(f"Permission '{permission}' granted to user {self.name}.")
            if self.logger:  # Check if logger exists before logging
                self.logger.log_event(f"Permission '{permission}' granted to user {self.name}.")

    def revoke_permission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)
            print(f"Permission '{permission}' revoked from user {self.name}.")
            if self.logger:  # Check if logger exists before logging
                self.logger.log_event(f"Permission '{permission}' revoked from user {self.name}.")
