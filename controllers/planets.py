from model import Planet

def index():
    try:
        planets = Planet.query.all()
        # planet_text = '<ul>'
        # for planet in planets:
        #     planet_text += f"<li>{planet.name} has {planet.num_moons} moons</li>"
        # planet_text += '</ul>'
        return jsonify({'data': planets}), 200
        
    except Exception as e:
        return jsonify({'err': e})