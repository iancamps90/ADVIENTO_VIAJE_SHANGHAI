import reflex as rx

config = rx.Config(
    app_name="adeviento_web",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)
