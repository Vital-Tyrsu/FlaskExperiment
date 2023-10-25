from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/map')
def display_map():
    # Create a map centered on Brussels
    brussels_map = folium.Map(location=[50.8503, 4.3517], zoom_start=12)

    # Save the map as an HTML file
    brussels_map.save("templates/brussels_map.html")

    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
