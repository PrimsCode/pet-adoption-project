from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SECRET_KEY']="12345"
app.debug = True
debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)
db.create_all()

@app.route('/')
def pet_listing():
    """Show the pet listing"""

    pets = Pet.query.all()
    print(pets[1])

    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add pet form"""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        avaliable = form.avaliable.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, avaliable=avaliable)
        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name}")
        return redirect('/')
    
    else:
        return render_template('add-pet-form.html', form=form)

@app.route('/<int:pet_id>')
def show_pet(pet_id):
    """Show the pet info"""
    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet-profile.html', pet=pet)


@app.route('/<int:pet_id>/edit', methods=['GET','POST'])
def edit_pet(pet_id):
    """Edit pet info"""

    pet = Pet.query.get_or_404(pet_id)
    
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.avaliable = form.avaliable.data        
        db.session.commit()
        flash(f"{pet.name} has been updated!")
        return redirect(f'/{pet.id}')
    
    else:
        return render_template('edit-pet-form.html', form=form, pet=pet)
    

