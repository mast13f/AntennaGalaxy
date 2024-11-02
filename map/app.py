from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

# Sample data for planets
planets = [
    {"name": "Mercury", "x": 0.4, "y": 0.2, "details": "Closest to the Sun."},
    {"name": "Venus", "x": 0.7, "y": 0.6, "details": "Very hot, thick atmosphere."},
    {"name": "Earth", "x": 1.0, "y": 1.0, "details": "Home planet."},
    {"name": "Mars", "x": 1.5, "y": 1.3, "details": "Red planet, has polar ice caps."},
    # Add more planets if desired
]

@app.route("/")
def index():
    # Create the scatter plot for planets
    fig = go.Figure()

    # Add each planet as a scatter point
    for planet in planets:
        fig.add_trace(go.Scatter(
            x=[planet["x"]],
            y=[planet["y"]],
            mode="markers+text",
            text=planet["name"],
            marker=dict(size=15),
            hovertext=planet["details"],
            hoverinfo="text"
        ))

    # Set layout properties
    fig.update_layout(
        title="Interactive Universe Map",
        xaxis=dict(title="Distance from Sun (AU)", showgrid=False),
        yaxis=dict(title="Vertical Position", showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white")
    )

    # Convert the plotly figure to JSON for rendering in HTML
    graphJSON = pio.to_json(fig)
    return render_template("index.html", graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(debug=True)
