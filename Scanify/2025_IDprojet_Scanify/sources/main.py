#Projet : Scanify
#Auteurs : Antonina Savchenko, Elisa Salignon

from flask import Flask, render_template, url_for, redirect, request, session
import openai
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired
from flask_bcrypt import Bcrypt
import json
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import os
from models.ocr import ImageReader, Language
from werkzeug.utils import secure_filename
from dotenv import load_dotenv




#Activation pour les graphs
matplotlib.use('Agg')

#Cle API
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
openai.api_key=api_key

#Dossier pour les fichiers uploadés
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#Initialisation Flask
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db=SQLAlchemy(app)
app.config['SECRET_KEY'] = 'a2n7t0o3e8f3d6b49c1a4f78b2d9e37c8f5a0e27e13d6f92b8c4a1d5f0b7e6c3d9a8f2b1'





#Creation des comptes
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    shop_name=db.Column(db.String(100))
    date = db.Column(db.String)
    amount = db.Column(db.Float)
    payment_method=db.Column(db.String(100))
    articles = db.Column(db.JSON)
    # onnection des bases de données
    user = db.relationship('User', backref=db.backref('receipts', lazy=True))

class RegisterForm(FlaskForm):
    username= StringField(validators=[InputRequired(), DataRequired(message="Le nom d'utilisateur est obligatoire."), Length(min=4, max=20, message="Le nom d'utilisateur doit contenir au moins 4 caractères.")], render_kw={"placeholder":"Username"})
    password=PasswordField(validators=[InputRequired(), DataRequired(message="Le mot de passe est obligatoire."), Length(min=4, max=20)], render_kw={"placeholder":"Password"})
    submit=SubmitField("Register")
    def validate_username(self, username):
            existing_user_username=User.query.filter_by(username=username.data).first()
            if existing_user_username:
                raise ValidationError("That username already exists. Please choose a different one.")

class LoginForm(FlaskForm):
    username= StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"Username"})
    password=PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"Password"})
    submit=SubmitField("Login")





#API
categories = ("Alimentation", "Hygiène et beauté", "Animaux", "Électronique et multimédia", "Vêtements et accessoires", "Maison et décoration", "Loisirs et papeterie", "Santé", "Emballages", "Transports", "Réduction")
def chat_with_gpt(categories, ticket_brut):
    try:
        response = openai.ChatCompletion.create(
        model="gpt-4",  #aussi "gpt-3.5-turbo"
        messages=[{"role": "user", "content": f"(n'ecris pas d'autres reponse que json format partir de un ticket de caisse avec les infos importantes (inclue 'Nom du magasin'(premiere lettre en majuscule et apres tout en minuscule), 'Date' date sans l'heure sous format %d/%m/%Y UNIQUEMENT pas d'autre format / tu peux changer la date pour que le format soit respecté (exemple si c'est indiquer 25 sur le ticket tu peux changer en 2025!!! ou N/A si aucune date trouvée!!!,   'Total' en float sans caractere speciaux choit bien le bon total (tu peux vérifier en additionnant tous les produits), 'Type de paiement' E pour especes ou CB pour carte bancaire ou CH pour chèque, 'Articles', dans 'Articles' fais un sous dictionnaire avec 'Nom_article' (resume le nom sur le ticket pour qu'il soit comprehensible par une personne), 'Catégorie' (classe l'artcle dans une des catégories suivante : {categories} et informe toi sur les produits vendus dans le magasin), 'Prix', ne fais fait 'quantité' mais ajoute l'article comme tel !!!! et fais tres attention aux remises s'il y en a) voici le ticket de caisse {ticket_brut}  et fais tres attention au nombre de chaque article et s'il y a des articles plusieurs fois dans le ticket, tu dois les mettre dans le disctionnaire séparément / attention s'il y a des réductions pense bien à les enlever du prix"}]
            )
        chat_response = response['choices'][0]['message']['content']
        return chat_response
    except Exception as e:
        return f"An error occurred: {e}"



#Les pages
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/clear_database") #delete at the end
def clear_database():
    db.drop_all()
    db.create_all() 
    return "Database cleared and recreated."

@app.route('/lougout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/register", methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user= User(username=form.username.data, password=hashed_password, receipts=[])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    users = User.query.all()
    print()
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    message_login = None
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(f"User found: {user}") 
        print()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                print("Password is correct")
                print()
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                message_login="Password is incorrect"
        else:
            message_login= "User not found"

    return render_template('login.html', form=form, message_login=message_login)




#Partie la plus importante
@app.route("/dashboard", methods=['GET','POST'])
@login_required
def dashboard():
    #Extraction du texte
    def process_image(filename):
        ir=ImageReader()
        text=ir.extract_text(os.path.join("uploads", filename), lang=Language.EN.value)
        processed_text=' '.join(text.split())
        return str(processed_text)

    upload_message = None 
    ticket_brut=None

    if request.method == 'POST':
        if 'action' in request.form and request.form['action'] == 'upload':
            telecharger=1
        if 'receipt_file' in request.files:
            file = request.files['receipt_file']
            if file:
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                filename = secure_filename(file.filename) 
                file.save(file_path)
                upload_message = f"File '{file.filename}' uploaded successfully!"
                print(f"File saved to: {file_path}")
                print()
                ticket_brut=process_image(filename)
                print(f"Ticket brut after processing: {ticket_brut}")
                print()

                session['ticket_brut'] = ticket_brut


    dernier_somme_ajoute=0
    new_receipt=None
    telecharger=1
    if 'ticket_brut' in session:
        ticket_brut = session['ticket_brut']
    


    print(f"Current user: {current_user.username}")
    print()
    if request.method == 'POST':
        if 'action' in request.form and request.form['action'] == 'analyse' and ticket_brut!=None:
            telecharger=None
            new_receipt = chat_with_gpt(categories, ticket_brut)

            print("texte extrait par l'ocr : ", ticket_brut)
            print()
            print("Chat-GPT answered : ", new_receipt)
            print()
            try:
                new_receipt = json.loads(new_receipt)
            except json.JSONDecodeError:
                print("Error: The string could not be decoded into a dictionary.")
                print()

            receipt = Receipt(user_id=current_user.id, shop_name=new_receipt['Nom du magasin'], date = new_receipt['Date'], amount=new_receipt['Total'], payment_method=new_receipt['Type de paiement'], articles=new_receipt['Articles'] )
            db.session.add(receipt)

            try:
                db.session.commit()  
                db.session.refresh(current_user)  
                print("Commit successful")
                print()
            except Exception as e:
                db.session.rollback() 
                print("Error during commit:", e)
                print()

            if receipt.id:
                print(f"Receipt added successfully to the person :  {current_user}")
                print()
            else:
                print("Failed to add the receipt.")
                print()

    if current_user:
                sum=0
                for receipt in current_user.receipts:
                    sum=float(receipt.amount)+sum
                    if telecharger==None:
                        dernier_somme_ajoute=float(receipt.amount)

    else:
                print(f"No user.")
                print()

    if current_user:
        categories_amount={"Alimentation":0, "Hygiène et beauté":0, "Animaux":0, "Électronique et multimédia":0, "Vêtements et accessoires":0, "Maison et décoration":0, "Loisirs et papeterie":0, "Santé":0, "Emballages":0, "Transports":0, "Réduction":0}
        nom_magasins=[]
        dates={}
        months={}
        especes=0
        cb=0
        #Pas de ticket encore
        if not current_user.receipts:
            print("No receipts found")
            print()
            return render_template('dashboard.html',upload_message=upload_message, current_username=current_user.username.capitalize(), chat_with_gpt_html=None,  chart_url=None,  bar_d_url=None, bar_m_url=None, tab_url=None, chart_pay_url=None, sum=sum, nom_magasins=None)
        else:
                Ttraitement des données
                categories_amount={"Alimentation":0, "Hygiène et beauté":0, "Animaux":0, "Électronique et multimédia":0, "Vêtements et accessoires":0, "Maison et décoration":0, "Loisirs et papeterie":0, "Santé":0, "Emballages":0, "Transports":0, "Réduction":0}
                nom_magasins=[]
                dates={}
                months={}
                especes=0
                cb=0
                ch=0
                derniers_articles=[]

                for receipt in current_user.receipts:
                    for article in receipt.articles: 
                        derniers_articles.append((article.get('Nom_article'),article.get('Prix')))

                        categorie = article.get("Catégorie")
                        print(categorie)
                        prix = article.get("Prix", 0)
                        if categorie in categories_amount:
                            categories_amount[categorie] += prix
                    
                    if receipt.shop_name not in nom_magasins:
                        nom_magasins.append(receipt.shop_name)
                        
                    if receipt.date in dates.keys():
                        dates[receipt.date]=receipt.amount+dates[receipt.date]
                    else:
                        dates[receipt.date]=receipt.amount

                    if receipt.date[3:10] in months.keys():
                        if receipt.date != "N/A":
                            months[receipt.date[3:10]]=receipt.amount+months[receipt.date[3:10]]
                    else:
                        if receipt.date != "N/A":
                            months[receipt.date[3:10]]=receipt.amount

                    if receipt.payment_method == 'E':
                         especes=especes+1
                    elif receipt.payment_method == 'CH':
                         ch=ch+1
                    elif receipt.payment_method == 'CB':
                         cb=cb+1
                         
                
                data_categories=categories_amount
                x = [key for key, value in data_categories.items() if value > 0]
                y = [value for value in data_categories.values() if value > 0]

                plt.rcParams['font.family'] = 'DejaVu Sans'
                colors = ['#b7ccd1', '#6a7998', '#dddee3', '#879a99', '#3f4d58']

                #TABLEAU
                tableau = [["Catégorie", "Montant (€)"]] + [[key, round(value, 4)] for key, value in categories_amount.items()]
                fig, ax = plt.subplots(figsize=(8, 4), facecolor='none')
                ax.axis('tight')
                ax.axis('off')
                table = ax.table(cellText=tableau, cellLoc='center', loc="center", colWidths=[0.5, 0.3])
                table.auto_set_font_size(False)
                table.set_fontsize(12)
                for i, cell in table.get_celld().items():
                    cell.set_edgecolor('#6a7998')
                    cell.set_height(0.1)
                    if i[0] == 0:
                        cell.set_fontsize(14)
                        cell.set_text_props(weight='bold', color='white')
                        cell.set_facecolor('#3f4d58')
                    else:
                        cell.set_facecolor('#262931')
                        cell.set_text_props(color='white')

                #Ajouter votre chemin relatif pour le répertoire graphs
                tab_path = os.path.join('Scanify//2025_IDprojet_Scanify//sources//data//graphs', 'tab_produits_par_categories.png')
                plt.savefig(tab_path)
                plt.close()


                

                #BAR CHART DAYS
                from datetime import datetime
                filtered_dates = {k: v for k, v in dates.items() if v > 0 and k!="N/A"}
                print(filtered_dates)
                sorted_dates = dict(sorted(filtered_dates.items(), key=lambda item: datetime.strptime(item[0], "%d/%m/%Y")))
                keys = list(sorted_dates.keys())
                values = list(sorted_dates.values())

                fig, ax = plt.subplots(figsize=(8, 5), facecolor='none')
                plt.bar(keys, values, color='#6a7998')
                plt.xlabel('Jours', fontsize=12, color='white')
                plt.ylabel('Montant dépensé (€)', fontsize=12, color='white')
                plt.grid(axis='y', linestyle='--', alpha=0.5, color='gray')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['left'].set_color('white')
                ax.spines['bottom'].set_color('white')
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='white')

                bar_d_path = os.path.join('Scanify//2025_IDprojet_Scanify//sources//data//graphs', 'bar_days.png')
                plt.savefig(bar_d_path)
                plt.close()

                #BAR CHART MONTHS
                month_keys = [datetime.strptime(k, "%d/%m/%Y").strftime("%m/%Y") for k in keys]
                fig, ax = plt.subplots(figsize=(8, 5), facecolor='none')
                plt.bar(month_keys, values, color='#b7ccd1')
                plt.xlabel('Mois', fontsize=12, color='white')
                plt.ylabel('Montant dépensé (€)', fontsize=12, color='white')
                plt.grid(axis='y', linestyle='--', alpha=0.5, color='gray')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['left'].set_color('white')
                ax.spines['bottom'].set_color('white')
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='white')

                bar_m_path = os.path.join('Scanify//2025_IDprojet_Scanify//sources//data//graphs', 'bar_months.png')
                plt.savefig(bar_m_path)
                plt.close()

                #PIE CATEGORIES
                explode = [0.08 if val == max(y) else 0.03 for val in y]
                fig, ax = plt.subplots(figsize=(8, 8), facecolor='none')
                wedges, texts, autotexts = ax.pie(
                    y, labels=x, autopct='%1.1f%%', startangle=140, colors=colors,
                    explode=explode, pctdistance=0.85,
                    wedgeprops={'edgecolor': '#fff', 'linewidth': 2, 'alpha': 0.9})
                for text in texts:
                    text.set(fontsize=13, fontweight="bold", color='white')
                for autotext in autotexts:
                    autotext.set(fontsize=13, fontweight="bold", color='#1d1e1d')
                plt.gca().set_facecolor('none')

                chart_path = os.path.join('Scanify//2025_IDprojet_Scanify//sources//data//graphs', 'chart_categories.png')
                plt.savefig(chart_path)
                plt.close()

                #PIE PAY
                fig, ax = plt.subplots(figsize=(8, 8), facecolor='none')
                wedges, texts, autotexts = ax.pie(
                    [especes, cb, ch], labels=["Espèces", "CB", "Chèque"], autopct='%1.1f%%', startangle=140, colors=colors, pctdistance=0.85,
                    wedgeprops={'edgecolor': '#fff', 'linewidth': 2, 'alpha': 0.9})
                
                for text in texts:
                    text.set(fontsize=13, fontweight="bold", color='white')
                for autotext in autotexts:
                    autotext.set(fontsize=13, fontweight="bold", color='#1d1e1d')
                plt.gca().set_facecolor('none')

                chart_pay_path = os.path.join('Scanify//2025_IDprojet_Scanify//sources//data//graphs', 'chart_pay.png')
                plt.savefig(chart_pay_path)
                plt.close()

                derniers_articles.reverse()
                nom_magasins.reverse()


    return render_template('dashboard.html', derniers_articles=derniers_articles, dernier_somme_ajoute=dernier_somme_ajoute, current_username=current_user.username.capitalize(), upload_message=upload_message, chat_with_gpt_html=new_receipt,  chart_url=url_for('static', filename=('chart_categories.png')),  bar_d_url=url_for('static', filename=('bar_days.png')), bar_m_url=url_for('static', filename=('bar_months.png')), tab_url=url_for('static', filename=('tab_produits_par_categories.png')), chart_pay_url=url_for('static', filename=('chart_pay.png')), sum=round(sum, 2), nom_magasins=nom_magasins)




if __name__ == '__main__':
    with app.app_context():
        print("Creating database tables...")
        print()
        db.create_all() 
        print("Database tables created.")
        print()
        print("Tables created:", db.metadata.sorted_tables)
        print()
    app.run(debug=True)


#$env:FLASK_APP = "c:/Users/Eleve/Desktop/Lycée/Première/NSI/Myapp/app.py"
#$env:FLASK_DEBUG = "1"
#python -m flask run

#