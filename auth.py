from opentelemetry import trace

tracer = trace.get_tracer("authenticate_user")

USER_CREDENTIALS = {
    "customer": {"password": "customer", "role": "Customer"},
    "manager": {"password": "manager", "role": "Manager"},
    "admin": {"password": "admin", "role": "Admin"},
}

def authenticate(username, password):
    with tracer.start_as_current_span("checking_credentials") as span:
        span.set_attribute("auth.username", username)
        span.set_attribute("auth.status", "attempted")
        user = USER_CREDENTIALS.get(username)
        if user and user["password"] == password:
            span.set_attribute("auth.status", "success")
            span.set_attribute("auth.role", user["role"])
            return user["role"]
        span.set_attribute("auth.status", "failed")
        return None