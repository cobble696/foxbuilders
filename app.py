from flask import Flask, render_template

app = Flask(__name__)

# Define your navbar links dynamically
nav_links = [
    {"name": "Services", "href": "#services"},
    {"name": "Portfolio", "href": "#portfolio"},
    {"name": "About", "href": "#about"},
    {"name": "Team", "href": "#team"},
    {"name": "Contact", "href": "#contact"}
]

# Define Services
services = [
    {"title": "Not Sure Where to Start?", "description": "Tell Kyle your square footage and number of employees—he'll design it.", "icon": "fas fa-shopping-cart"},
    {"title": "Full Catalog", "description": "Get new or pre-owned furniture.", "icon": "fas fa-laptop"},
    {"title": "Reconfiguration", "description": "Redesign your space for efficiency and employee well-being.", "icon": "fas fa-lock"}
]

# Define Portfolio Items
portfolio_items = [
    {"title": "Threads", "category": "Illustration", "image": "1.jpg"},
    {"title": "Explore", "category": "Space Design", "image": "2.jpg"},
    {"title": "Finish", "category": "Identity", "image": "3.jpg"},
    {"title": "Lines", "category": "Foxbuilt", "image": "4.jpg"},
    {"title": "Southwest", "category": "Website Design", "image": "5.jpg"},
    {"title": "Window", "category": "Photography", "image": "6.jpg"}
]

# Define Team Members
team_members = [
    {"name": "Auntie Cyndee", "role": "Operations Manager", "image": "1.jpg"},
    {"name": "Chamele Brothers", "role": "Crew Members", "image": "2.jpg"},
    {"name": "Larry Parker", "role": "Lead Developer", "image": "3.jpg"}
]

# Define Story Timeline
story = [
    {"date": "2009-2011", "title": "Our Humble Beginnings", "description": "The best of times, the worst of times. Also, 2008 sucked.", "image": "1.jpg"},
    {"date": "March 2011", "title": "An Installer is Installed, Not Born", "description": "You can't teach this in a classroom. Try doing 10 cubicles without our help!", "image": "2.jpg"},
    {"date": "December 2015", "title": "Transition to Full Service", "description": "Started with selling products, bought a van, storage units, and now we sell furniture full-time.", "image": "3.jpg"},
    {"date": "August 2095", "title": "Phase Two Expansion", "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente.", "image": "4.jpg"}
]

@app.route('/')
def home():
    return render_template(
        'index.html', 
        nav_links=nav_links, 
        services=services, 
        portfolio_items=portfolio_items, 
        team_members=team_members,
        story=story
    )

if __name__ == '__main__':
    app.run(debug=True)
