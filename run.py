from blog import app
import os


app.secret_key = os.urandom(24)
port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)
#app.run(host='0.0.0.0', port=port)
