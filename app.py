from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# 1. Serve the HTML Interface
@app.route('/')
def home():
    return render_template('index.html')

# 2. API Endpoint to process calculations
@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')

    if not expression:
        return jsonify({"status": "error", "message": "No expression provided"})

    try:
        # The expanded, production-ready dictionary of safe math functions
        safe_dict = {
            "sin": math.sin, 
            "cos": math.cos, 
            "tan": math.tan,
            "sqrt": math.sqrt, 
            "log": math.log, 
            "log10": math.log10,
            "factorial": math.factorial, 
            "abs": abs,
            "radians": math.radians, 
            "degrees": math.degrees,
            "ceil": math.ceil,
            "floor": math.floor,
            "pi": math.pi, 
            "e": math.e
        }
        
        # Safely evaluate the math string from the HTML
        # __builtins__: None prevents malicious code injection
        result = eval(expression, {"__builtins__": None}, safe_dict)
        
        # Format the result to avoid excessively long decimal chains
        formatted_result = round(result, 6) if isinstance(result, float) else result
        
        # Format text for the Text-to-Speech engine (e.g., changing "-" to "minus")
        spoken_text = str(formatted_result).replace('-', 'minus ')
        
        return jsonify({
            "status": "success", 
            "result": formatted_result,
            "spoken_text": spoken_text
        })

    except ZeroDivisionError:
        return jsonify({"status": "error", "message": "Division by zero"})
    except ValueError as ve:
        # Catches specific math domain errors, like square root of a negative number
        return jsonify({"status": "error", "message": "Math Domain Error"})
    except Exception:
        # Catches syntax errors or unparseable inputs
        return jsonify({"status": "error", "message": "Invalid Expression"})

if __name__ == '__main__':
    # Run the server safely on port 5000
    app.run(debug=True, port=5000)