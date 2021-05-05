class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column('planet_id', db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    num_moons = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Planet %r>' % self.name
    
    def __init__(self, name, num_moons):
        self.name = name
        self.num_moons = num_moons