from flask import Flask, render_template, request, redirect, url_for

# Vercel ke liye template aur static folder specify karna safe rehta hai
app = Flask(__name__, template_folder='templates', static_folder='static')

# Vercel ko 'app' object 'app' ke naam se hi mil jayega, par ye line handle karti hai
app.debug = False 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Yaha aap apna logic daal sakte hain
        print(f"Name: {name}, Email: {email}, Message: {message}")

        # KHAS DHAYAN: Khali return nahi chod sakte, 
        # isliye hum home page par bhej rahe hain ya success page dikha sakte hain
        return redirect(url_for('home')) 

    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Ye line local testing ke liye hai, Vercel ise ignore kar dega
if __name__ == '__main__':
    app.run()
