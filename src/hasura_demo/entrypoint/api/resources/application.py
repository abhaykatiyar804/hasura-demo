import falcon
import falcon.asgi


app = falcon.asgi.App()

# Resources are represented by long-lived class instances
things = HealthCheck()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)