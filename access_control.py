from opentelemetry import trace

tracer = trace.get_tracer("permission_and_sensitivity_access")

PERMISSIONS = {
    "Customer": ["view_transactions"],
    "Manager": ["view_transactions", "approve_transactions"],
    "Admin": ["view_transactions", "approve_transactions", "manage_users"],
}

def has_access(role, permission):
    """Check if a user role has the specified permission."""
    with tracer.start_as_current_span("check_permission") as span:
        span.set_attribute("role", role)
        span.set_attribute("permission", permission)
        has_permission = permission in PERMISSIONS.get(role, [])
        span.set_attribute("access_granted", has_permission)
        return has_permission

def can_access_sensitivity(role, sensitivity):
    """Check if a user role can access a specific sensitivity level of data."""
    with tracer.start_as_current_span("check_sensitivity_access") as span:
        span.set_attribute("role", role)
        span.set_attribute("sensitivity", sensitivity)
        
        SENSITIVITY_POLICIES = {
            "Customer": ["Public"],
            "Manager": ["Public", "Confidential"],
            "Admin": ["Public", "Confidential", "Restricted"],
        }
        can_access = sensitivity in SENSITIVITY_POLICIES.get(role, [])
        span.set_attribute("can_access", can_access)
        return can_access